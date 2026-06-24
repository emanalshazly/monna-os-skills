#!/usr/bin/env python3
"""
Skill Overlap Detector
======================

A CLI tool for detecting semantic duplication within skill collections.
Uses TF-IDF + cosine similarity for content overlap, and Jaccard similarity
for trigger-phrase collision detection.

Part of the MONNA Open-Source Skill Collection.
License: MIT

Usage:
    python overlap_checker.py --skills-dir <path> [--threshold 0.60] [--output report.md]
    python overlap_checker.py --skills-dir <path> --new-skill <path> [--threshold 0.60]
    python overlap_checker.py --calibrate --labeled-pairs <path>
"""

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path


try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    print("ERROR: scikit-learn is required. Install with: pip install -r requirements.txt")
    sys.exit(1)


# ─── Configuration ──────────────────────────────────────────────────────────

DEFAULT_CONTENT_THRESHOLD = 0.60
DEFAULT_TRIGGER_THRESHOLD = 0.40
DEFAULT_MEDIUM_THRESHOLD = 0.45

SECTION_WEIGHTS = {
    "triggers": 3.0,
    "principles": 2.5,
    "steps": 2.0,
    "anti_patterns": 2.0,
    "examples": 1.5,
    "references": 1.0,
    "body": 1.0,
}

SECTION_PATTERNS = {
    "triggers": re.compile(r"(?i)(trigger|when to use|activate when)"),
    "principles": re.compile(r"(?i)(principle|rule|constraint|core principle)"),
    "steps": re.compile(r"(?i)(step[- ]by[- ]step|process|workflow|how to)"),
    "anti_patterns": re.compile(r"(?i)(anti[- ]pattern|pitfall|don.t|avoid)"),
    "examples": re.compile(r"(?i)(example|use case|scenario)"),
    "references": re.compile(r"(?i)(reference|see also|further reading)"),
}


# ─── Utilities ──────────────────────────────────────────────────────────────

def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter (between --- delimiters)."""
    if text.startswith("---"):
        _, _, body = text.partition("---")
        _, _, body = body.partition("---")
        return body.strip()
    return text.strip()


def extract_sections(text: str) -> dict:
    """
    Extract weighted sections from a SKILL.md body.
    Returns {section_type: [lines_of_text]}.
    """
    sections = {key: [] for key in SECTION_WEIGHTS}
    lines = text.splitlines()
    current_section = "body"

    for line in lines:
        stripped = line.strip().lower()
        # Check if this line indicates a section header
        for section_name, pattern in SECTION_PATTERNS.items():
            if pattern.search(stripped):
                current_section = section_name
                break
        sections[current_section].append(line)

    return sections


def build_weighted_text(sections: dict) -> str:
    """Repeat section text according to weights to bias TF-IDF."""
    weighted_lines = []
    for section_name, lines in sections.items():
        weight = SECTION_WEIGHTS.get(section_name, 1.0)
        repeats = int(weight)
        text_block = "\n".join(lines)
        for _ in range(repeats):
            weighted_lines.append(text_block)
    return "\n".join(weighted_lines)


def extract_trigger_phrases(text: str) -> set:
    """Extract trigger phrases from a skill document."""
    triggers = set()
    # Match bullet lists under trigger sections
    trigger_section = re.search(
        r"(?i)(trigger|when to use|activate when).*?(?=\n##|\n---|$)",
        text,
        re.DOTALL,
    )
    if trigger_section:
        section_text = trigger_section.group(0)
        # Extract bullet items
        for match in re.finditer(r"[-*]\s+(.+)", section_text):
            triggers.add(match.group(1).strip().lower())
    return triggers


def compute_fingerprint(text: str) -> str:
    """Generate a 16-char SHA-256 hash of the semantic content."""
    clean = strip_frontmatter(text).lower()
    clean = re.sub(r"[^\w\s]", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return hashlib.sha256(clean.encode()).hexdigest()[:16]


# ─── Core Logic ─────────────────────────────────────────────────────────────

def parse_skill(skill_path: Path) -> dict:
    """Parse a single SKILL.md file into a structured dict."""
    text = skill_path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    sections = extract_sections(body)
    weighted = build_weighted_text(sections)
    triggers = extract_trigger_phrases(body)
    fingerprint = compute_fingerprint(text)

    return {
        "path": str(skill_path),
        "name": skill_path.parent.name,
        "domain": skill_path.parent.parent.name,
        "fingerprint": fingerprint,
        "trigger_phrases": triggers,
        "weighted_text": weighted,
        "raw_text": body,
    }


def parse_corpus(skills_dir: Path) -> list[dict]:
    """Walk skills_dir and parse all SKILL.md files."""
    corpus = []
    for skill_file in skills_dir.rglob("SKILL.md"):
        try:
            corpus.append(parse_skill(skill_file))
        except Exception as e:
            print(f"WARNING: Failed to parse {skill_file}: {e}", file=sys.stderr)
    return corpus


def compute_similarity_matrix(corpus: list[dict]) -> dict:
    """
    Compute pairwise cosine similarity for all skills in the corpus.
    Returns a dict of (name_a, name_b): similarity_score.
    """
    texts = [skill["weighted_text"] for skill in corpus]
    names = [skill["name"] for skill in corpus]

    vectorizer = TfidfVectorizer(
        min_df=1,
        max_df=0.8,
        ngram_range=(1, 2),
        sublinear_tf=True,
        stop_words="english",
    )
    tfidf_matrix = vectorizer.fit_transform(texts)
    sim_matrix = cosine_similarity(tfidf_matrix)

    similarities = {}
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            similarities[(names[i], names[j])] = sim_matrix[i][j]

    return similarities


def compute_trigger_overlap(skill_a: dict, skill_b: dict) -> float:
    """Compute Jaccard similarity of trigger phrase sets."""
    triggers_a = skill_a["trigger_phrases"]
    triggers_b = skill_b["trigger_phrases"]

    if not triggers_a and not triggers_b:
        return 0.0
    if not triggers_a or not triggers_b:
        return 0.0

    intersection = triggers_a & triggers_b
    union = triggers_a | triggers_b
    return len(intersection) / len(union)


def check_new_skill(new_skill_path: Path, corpus_dir: Path) -> dict:
    """
    Check a single new skill against an existing corpus.
    Returns a report dict with overlap results.
    """
    corpus = parse_corpus(corpus_dir)
    new_skill = parse_skill(new_skill_path)

    # Add new skill to corpus temporarily for TF-IDF computation
    all_texts = [skill["weighted_text"] for skill in corpus] + [new_skill["weighted_text"]]
    all_names = [skill["name"] for skill in corpus] + [new_skill["name"]]

    vectorizer = TfidfVectorizer(
        min_df=1,
        max_df=0.8,
        ngram_range=(1, 2),
        sublinear_tf=True,
        stop_words="english",
    )
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    sim_matrix = cosine_similarity(tfidf_matrix)

    new_idx = len(corpus)
    results = []
    for i in range(len(corpus)):
        content_sim = sim_matrix[i][new_idx]
        trigger_sim = compute_trigger_overlap(corpus[i], new_skill)
        results.append({
            "existing_skill": corpus[i]["name"],
            "similarity": content_sim,
            "trigger_overlap": trigger_sim,
        })

    return {
        "new_skill": new_skill["name"],
        "fingerprint": new_skill["fingerprint"],
        "trigger_count": len(new_skill["trigger_phrases"]),
        "results": results,
    }


# ─── Report Generation ──────────────────────────────────────────────────────

def generate_report(
    corpus: list[dict],
    similarities: dict,
    content_threshold: float,
    trigger_threshold: float,
    medium_threshold: float,
) -> str:
    """Generate a markdown overlap report."""
    lines = []
    lines.append("=" * 80)
    lines.append("SKILL OVERLAP DETECTION REPORT")
    lines.append(f"Generated: {__import__('datetime').datetime.now().isoformat()}")
    lines.append(f"Corpus: {len(corpus)} skills")
    lines.append(f"Threshold: {content_threshold:.2f} (content), {trigger_threshold:.2f} (triggers)")
    lines.append("=" * 80)
    lines.append("")

    # High overlap
    high_pairs = [
        (pair, sim)
        for pair, sim in similarities.items()
        if sim > content_threshold
    ]
    high_pairs.sort(key=lambda x: x[1], reverse=True)

    lines.append("--- HIGH OVERLAP (Action Required) ---")
    lines.append("")
    if high_pairs:
        lines.append("| Skill A | Skill B | Similarity | Recommendation |")
        lines.append("|---------|---------|------------|----------------|")
        for (name_a, name_b), sim in high_pairs:
            lines.append(f"| {name_a} | {name_b} | {sim:.2f} | Differentiate or merge |")
    else:
        lines.append("(no entries)")
    lines.append("")

    # Trigger collisions
    trigger_collisions = []
    for i in range(len(corpus)):
        for j in range(i + 1, len(corpus)):
            overlap = compute_trigger_overlap(corpus[i], corpus[j])
            if overlap > trigger_threshold:
                shared = corpus[i]["trigger_phrases"] & corpus[j]["trigger_phrases"]
                trigger_collisions.append((
                    corpus[i]["name"],
                    corpus[j]["name"],
                    overlap,
                    shared,
                ))
    trigger_collisions.sort(key=lambda x: x[2], reverse=True)

    lines.append("--- TRIGGER COLLISIONS (Warning) ---")
    lines.append("")
    if trigger_collisions:
        lines.append("| Skill A | Skill B | Trigger Jaccard | Shared Triggers |")
        lines.append("|---------|---------|---------------|-----------------|")
        for name_a, name_b, overlap, shared in trigger_collisions:
            shared_str = ", ".join(list(shared)[:3]) + ("..." if len(shared) > 3 else "")
            lines.append(f"| {name_a} | {name_b} | {overlap:.2f} | {shared_str} |")
    else:
        lines.append("(no entries above {:.2f})".format(trigger_threshold))
    lines.append("")

    # Watchlist
    medium_pairs = [
        (pair, sim)
        for pair, sim in similarities.items()
        if medium_threshold < sim <= content_threshold
    ]
    medium_pairs.sort(key=lambda x: x[1], reverse=True)

    lines.append("--- WATCHLIST (Medium Overlap -- Monitor) ---")
    lines.append("")
    if medium_pairs:
        lines.append("| Skill A | Skill B | Similarity | Notes |")
        lines.append("|---------|---------|------------|-------|")
        for (name_a, name_b), sim in medium_pairs:
            lines.append(f"| {name_a} | {name_b} | {sim:.2f} | Monitor for drift |")
    else:
        lines.append("(no entries)")
    lines.append("")

    # Pass list
    all_flagged = set()
    for (name_a, name_b), _ in high_pairs:
        all_flagged.update([name_a, name_b])
    for name_a, name_b, _, _ in trigger_collisions:
        all_flagged.update([name_a, name_b])
    for (name_a, name_b), _ in medium_pairs:
        all_flagged.update([name_a, name_b])

    passed = [skill["name"] for skill in corpus if skill["name"] not in all_flagged]
    lines.append("--- PASS (No Overlap) ---")
    lines.append("")
    for name in passed:
        lines.append(f"{name} ✓")
    lines.append("")
    lines.append(f"({len(passed)}/{len(corpus)} skills have no overlap or warning)")

    return "\n".join(lines)


def generate_pr_report(report: dict, content_threshold: float, trigger_threshold: float) -> str:
    """Generate a markdown report for a single new skill vs. existing corpus."""
    lines = []
    lines.append("=" * 80)
    lines.append("PR OVERLAP DETECTION REPORT")
    lines.append(f"New Skill: {report['new_skill']}")
    lines.append(f"Corpus: {len(report['results'])} existing skills")
    lines.append(f"Threshold: {content_threshold:.2f} (content), {trigger_threshold:.2f} (triggers)")
    lines.append("=" * 80)
    lines.append("")

    lines.append("--- NEW SKILL FINGERPRINT ---")
    lines.append("")
    lines.append(f"Skill ID: {report['new_skill']}")
    lines.append(f"Fingerprint: {report['fingerprint']}")
    lines.append(f"Trigger Count: {report['trigger_count']}")
    lines.append("")

    lines.append("--- OVERLAP WITH EXISTING SKILLS ---")
    lines.append("")
    lines.append("| Existing Skill | Similarity | Trig. Jaccard | Verdict |")
    lines.append("|----------------|------------|---------------|---------|")

    max_sim = 0.0
    max_trigger = 0.0
    blocked = False

    for result in report["results"]:
        sim = result["similarity"]
        trig = result["trigger_overlap"]
        max_sim = max(max_sim, sim)
        max_trigger = max(max_trigger, trig)

        if sim > content_threshold and trig > trigger_threshold:
            verdict = "🔴 BLOCK -- Full collision"
            blocked = True
        elif sim > content_threshold:
            verdict = "🔴 BLOCK -- Body overlap"
            blocked = True
        elif trig > trigger_threshold:
            verdict = "⚠️ Warning -- Trigger collision"
        else:
            verdict = "✅ PASS"

        lines.append(f"| {result['existing_skill']} | {sim:.2f} | {trig:.2f} | {verdict} |")

    lines.append("")
    lines.append(f"Max similarity with any existing skill: {max_sim:.2f}")
    lines.append(f"Max trigger overlap with any existing skill: {max_trigger:.2f}")
    lines.append("")

    lines.append("--- RECOMMENDATION ---")
    lines.append("")
    if blocked:
        lines.append("🔴 BLOCKED -- DO NOT MERGE")
        lines.append("")
        lines.append("The new skill overlaps significantly with existing skills.")
        lines.append("Please differentiate, merge, or family-group before merging.")
    else:
        lines.append("✅ APPROVED FOR MERGE")
        lines.append("")
        lines.append("No overlap detected. The new skill is well-differentiated.")

    return "\n".join(lines)


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Detect semantic overlap in agent skill collections."
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        required=True,
        help="Directory containing skills/<domain>/<skill-name>/SKILL.md files",
    )
    parser.add_argument(
        "--new-skill",
        type=Path,
        help="Path to a single new SKILL.md to check against the corpus (PR mode)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_CONTENT_THRESHOLD,
        help=f"Content overlap threshold (default: {DEFAULT_CONTENT_THRESHOLD})",
    )
    parser.add_argument(
        "--trigger-threshold",
        type=float,
        default=DEFAULT_TRIGGER_THRESHOLD,
        help=f"Trigger overlap threshold (default: {DEFAULT_TRIGGER_THRESHOLD})",
    )
    parser.add_argument(
        "--medium-threshold",
        type=float,
        default=DEFAULT_MEDIUM_THRESHOLD,
        help=f"Medium overlap watchlist threshold (default: {DEFAULT_MEDIUM_THRESHOLD})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("overlap-report.md"),
        help="Output file for the report (default: overlap-report.md)",
    )
    parser.add_argument(
        "--find-new-skills",
        action="store_true",
        help="Automatically find new skills by comparing against git main",
    )

    args = parser.parse_args()

    if not args.skills_dir.exists():
        print(f"ERROR: Skills directory not found: {args.skills_dir}")
        sys.exit(1)

    # PR mode: single new skill
    if args.new_skill:
        if not args.new_skill.exists():
            print(f"ERROR: New skill file not found: {args.new_skill}")
            sys.exit(1)

        report = check_new_skill(args.new_skill, args.skills_dir)
        output = generate_pr_report(report, args.threshold, args.trigger_threshold)
        args.output.write_text(output, encoding="utf-8")
        print(f"PR report written to: {args.output}")

        max_sim = max(r["similarity"] for r in report["results"]) if report["results"] else 0
        if max_sim > args.threshold:
            sys.exit(2)  # Exit code 2 for CI: overlap detected
        sys.exit(0)

    # Full corpus mode
    corpus = parse_corpus(args.skills_dir)
    if len(corpus) < 2:
        print("ERROR: Need at least 2 skills to compute overlap.")
        sys.exit(1)

    similarities = compute_similarity_matrix(corpus)
    report = generate_report(
        corpus,
        similarities,
        args.threshold,
        args.trigger_threshold,
        args.medium_threshold,
    )
    args.output.write_text(report, encoding="utf-8")
    print(f"Report written to: {args.output}")

    # Exit code 2 if any overlap above threshold
    high_overlap = any(sim > args.threshold for sim in similarities.values())
    if high_overlap:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
