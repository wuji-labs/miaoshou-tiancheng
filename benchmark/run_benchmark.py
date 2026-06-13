#!/usr/bin/env python3
"""
MiaoShou TianCheng Benchmark Runner.

Runs an AI agent across the health/wellness scenarios in scenarios.json under two
conditions (baseline, skill) and writes raw results to results/*.json.

This runner PRODUCES NO DATA on its own. With --dry-run it only prints the execution
plan (no API calls). A real run requires a valid API key and produces results derived
solely from that run — this repository ships NO pre-baked numbers.

Usage:
    python run_benchmark.py --model claude-sonnet-4 --condition all --runs 5 --dry-run
    python run_benchmark.py --model claude-sonnet-4 --condition skill --scenario 4 --runs 1
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration (explicit, no magic numbers) -----------------------------

MODELS = {
    "claude-sonnet-4": {"provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    "gpt-4o": {"provider": "openai", "model_id": "gpt-4o"},
    "gemini-2.5-pro": {"provider": "google", "model_id": "gemini-2.5-pro-preview-06-05"},
}
CONDITIONS = ["baseline", "skill"]
DEFAULT_RUNS = 5
DEFAULT_OUTPUT_DIR = "results"

HERE = Path(__file__).resolve().parent
SCENARIOS_PATH = HERE / "scenarios.json"
SKILL_PATH = HERE.parent / "SKILL.md"
REFERENCE_PATH = HERE.parent / "reference" / "huangdi-neijing.md"

BASELINE_SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer the user's health or wellness question."
)


def load_scenarios() -> list[dict]:
    """Load scenarios.json. Fail loudly if missing or malformed (no silent fallback)."""
    if not SCENARIOS_PATH.exists():
        sys.exit(f"ERROR: scenarios file not found: {SCENARIOS_PATH}")
    try:
        data = json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"ERROR: scenarios.json is not valid JSON: {exc}")
    if not isinstance(data, list) or not data:
        sys.exit("ERROR: scenarios.json must be a non-empty JSON array.")
    return data


def build_system_prompt(condition: str) -> str:
    """Compose the system prompt for a condition. 'skill' loads SKILL.md (+reference)."""
    if condition == "baseline":
        return BASELINE_SYSTEM_PROMPT
    if condition == "skill":
        if not SKILL_PATH.exists():
            sys.exit(f"ERROR: SKILL.md not found for skill condition: {SKILL_PATH}")
        parts = [SKILL_PATH.read_text(encoding="utf-8")]
        if REFERENCE_PATH.exists():
            parts.append("\n\n# Reference (huangdi-neijing.md)\n\n")
            parts.append(REFERENCE_PATH.read_text(encoding="utf-8"))
        return "".join(parts)
    sys.exit(f"ERROR: unknown condition '{condition}'. Use one of {CONDITIONS}.")


@dataclass
class BenchmarkResult:
    scenario_id: int
    scenario_name: str
    condition: str
    model: str
    run_number: int
    timestamp: str = ""
    agent_output: str = ""
    error: str = ""
    # Scoring fields are filled by a separate human/judge pass, not invented here.
    expected_actions_hit: list[str] = field(default_factory=list)
    notes: str = ""


def call_model(provider: str, model_id: str, system_prompt: str, user_task: str) -> str:
    """Dispatch one agent call. Raises on missing SDK/key so failures are explicit."""
    if provider == "anthropic":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError("ANTHROPIC_API_KEY is not set.")
        try:
            import anthropic
        except ImportError as exc:
            raise RuntimeError("anthropic SDK not installed: pip install anthropic") from exc
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model=model_id,
            max_tokens=2048,
            system=system_prompt,
            messages=[{"role": "user", "content": user_task}],
        )
        return "".join(block.text for block in resp.content if block.type == "text")
    if provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set.")
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("openai SDK not installed: pip install openai") from exc
        client = OpenAI()
        resp = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_task},
            ],
        )
        return resp.choices[0].message.content or ""
    if provider == "google":
        if not os.environ.get("GOOGLE_API_KEY"):
            raise RuntimeError("GOOGLE_API_KEY is not set.")
        try:
            import google.generativeai as genai
        except ImportError as exc:
            raise RuntimeError("google-generativeai not installed.") from exc
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        model = genai.GenerativeModel(model_id, system_instruction=system_prompt)
        return model.generate_content(user_task).text
    raise RuntimeError(f"Unknown provider: {provider}")


def main() -> None:
    parser = argparse.ArgumentParser(description="MiaoShou TianCheng benchmark runner")
    parser.add_argument("--model", required=True, choices=list(MODELS))
    parser.add_argument("--condition", default="all", choices=CONDITIONS + ["all"])
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    parser.add_argument("--scenario", default="all", help="scenario id or 'all'")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    scenarios = load_scenarios()
    if args.scenario != "all":
        scenarios = [s for s in scenarios if str(s["id"]) == str(args.scenario)]
        if not scenarios:
            sys.exit(f"ERROR: scenario id '{args.scenario}' not found.")

    conditions = CONDITIONS if args.condition == "all" else [args.condition]
    meta = MODELS[args.model]
    out_dir = (HERE / args.output_dir).resolve()

    plan = [
        (s["id"], c, r)
        for c in conditions
        for s in scenarios
        for r in range(1, args.runs + 1)
    ]
    print(f"Model: {args.model} ({meta['model_id']})")
    print(f"Conditions: {conditions} | Scenarios: {[s['id'] for s in scenarios]} | Runs: {args.runs}")
    print(f"Total agent calls: {len(plan)} | Output: {out_dir}")

    if args.dry_run:
        print("\n[DRY RUN] No API calls made, no results written.")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    for condition in conditions:
        system_prompt = build_system_prompt(condition)
        results: list[dict] = []
        for scenario in scenarios:
            for run in range(1, args.runs + 1):
                result = BenchmarkResult(
                    scenario_id=scenario["id"],
                    scenario_name=scenario["name"],
                    condition=condition,
                    model=args.model,
                    run_number=run,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
                try:
                    result.agent_output = call_model(
                        meta["provider"], meta["model_id"], system_prompt, scenario["task"]
                    )
                except Exception as exc:  # surface, don't punt to caller silently
                    result.error = str(exc)
                    print(f"  [error] scenario {scenario['id']} run {run}: {exc}")
                results.append(asdict(result))
                print(f"  done: scenario {scenario['id']} run {run} ({condition})")
        out_file = out_dir / f"{args.model}_{condition}.json"
        out_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {len(results)} records -> {out_file}")

    print("\nRaw outputs written. Scoring (expected_actions hit-rate + dimension scores)")
    print("is a separate human/judge pass — see README_BENCHMARK.md. No scores invented here.")


if __name__ == "__main__":
    main()
