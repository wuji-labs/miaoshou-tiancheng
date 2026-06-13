#!/usr/bin/env python3
"""
MiaoShou TianCheng results analyzer.

Reads SCORED result JSON files from results/ and computes paired statistics
(Wilcoxon / Mann-Whitney / Cohen's d) comparing baseline vs skill.

This script NEVER fabricates data. If results/ is empty, or scores are absent,
it exits with an explicit error instead of inventing numbers. All reported
statistics are derived solely from the scored input files.

Scored input format: each result record must include a numeric 'score' field
(e.g. expected_actions hit-rate in [0,1]) added by a human/judge pass. See
README_BENCHMARK.md for the scoring rubric.

Usage:
    python analyze_results.py --input-dir results/
"""

import argparse
import json
import sys
from pathlib import Path


def load_scored(input_dir: Path) -> list[dict]:
    """Load all *.json result files. Require a numeric 'score' on every record."""
    if not input_dir.exists():
        sys.exit(f"ERROR: input dir not found: {input_dir}")
    files = sorted(input_dir.glob("*.json"))
    if not files:
        sys.exit(
            f"ERROR: no result files in {input_dir}. "
            "Run run_benchmark.py first, then score the outputs. "
            "This analyzer does NOT invent results."
        )
    records: list[dict] = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        for rec in data:
            if "score" not in rec or not isinstance(rec["score"], (int, float)):
                sys.exit(
                    f"ERROR: record in {path.name} lacks a numeric 'score'. "
                    "Score the raw outputs per README_BENCHMARK.md before analysis."
                )
            records.append(rec)
    return records


def cohens_d(a: list[float], b: list[float]) -> float:
    """Cohen's d for two independent samples. Requires real samples; no defaults."""
    import statistics
    if len(a) < 2 or len(b) < 2:
        raise ValueError("Cohen's d needs >=2 observations per group.")
    n1, n2 = len(a), len(b)
    v1, v2 = statistics.variance(a), statistics.variance(b)
    pooled = (((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2)) ** 0.5
    if pooled == 0:
        return 0.0
    return (statistics.mean(a) - statistics.mean(b)) / pooled


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze scored benchmark results")
    parser.add_argument("--input-dir", required=True)
    args = parser.parse_args()

    records = load_scored(Path(args.input_dir).resolve())
    by_condition: dict[str, list[float]] = {}
    for rec in records:
        by_condition.setdefault(rec["condition"], []).append(float(rec["score"]))

    if "baseline" not in by_condition or "skill" not in by_condition:
        sys.exit("ERROR: need both 'baseline' and 'skill' conditions to compare.")

    baseline = by_condition["baseline"]
    skill = by_condition["skill"]

    try:
        from scipy import stats
        u_stat, p_value = stats.mannwhitneyu(skill, baseline, alternative="two-sided")
        stat_line = f"Mann-Whitney U={u_stat:.3f}, p={p_value:.4f}"
    except ImportError:
        stat_line = "(scipy not installed — install it for Mann-Whitney/Wilcoxon p-values)"

    import statistics
    print("=== MiaoShou TianCheng results (from real scored data only) ===")
    print(f"baseline: n={len(baseline)}, mean={statistics.mean(baseline):.4f}")
    print(f"skill:    n={len(skill)}, mean={statistics.mean(skill):.4f}")
    print(stat_line)
    print(f"Cohen's d (skill vs baseline): {cohens_d(skill, baseline):.4f}")
    print("\nAll figures above are computed from the scored input files, not pre-baked.")


if __name__ == "__main__":
    main()
