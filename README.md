# 妙手天成 MiaoShou TianCheng — Healing Hands

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/miaoshou-tiancheng"><img src="https://www.skills.sh/b/wuji-labs/miaoshou-tiancheng" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

这是华夏道脉献给世界开源社区的十件礼物之一(叩兩端·无极樞纽)。
我们不立华夏本位,不主张华夏文明优于任何文明;我们只是先从自己最熟悉的道脉开始,
把它打磨成一件可用的工具,放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来,共同构成十二文明对标的开源能力矩阵。

EN: This is one of ten gifts the Chinese stream of wisdom offers to the world's
open-source community. We make no claim that any civilization is superior; we
simply begin with the lineage we know best, and place it on humanity's shared
toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **上工治未病** — The superior physician treats what is not yet ill.
> — 《素问·四气调神大论》 Huangdi Neijing, Suwen, Ch. "Four Qi Regulate the Spirit"

**Your AI diagnoses symptoms. Teach it to see the whole person.**

Most AI health training maps **symptom → answer**: "insomnia" → "here are 8 sleep tips." Clean, fast, and impersonal — the same checklist for an anxious teenager, a postpartum mother, and an exhausted elder. It treats the complaint, never the person.

**MiaoShou TianCheng** (妙手天成) infuses the integrative framework of the *Huangdi Neijing* (黄帝内经, ~2000 years old) into how AI gives health and wellness advice. Not as a way to prescribe, but as a way to **look** — at season, constitution, emotion, and balance — before it speaks. It draws no symptom-to-cure shortcuts; it asks the right questions, knows its limits, and hands hard cases back to a licensed physician.

## The Problem

```
You: "I've been exhausted and can't sleep lately."

AI without MiaoShou:  "Try: fixed bedtime, no caffeine, no screens,
                       magnesium, meditation, cooler room..."
                       (Same list for everyone. No questions asked.)

AI with MiaoShou:     "When did it start, and in which season?
                       Trouble falling asleep, or waking early?
                       Eating heavily before bed? Carrying worry?
                       — In tradition, sleeplessness from an
                       unsettled stomach and from heart-kidney
                       disharmony point in opposite directions.
                       Let's find which, then adjust gently.
                       (And if this persists, please see a doctor.)"
```

## What It Teaches AI

### 治未病 Treat-What-Is-Not-Yet-Ill — the default move

| Principle | Chinese | What AI Does |
|-----------|---------|--------------|
| Prevent before onset | 未病先防 | Ask about routine/season/mood *before* the complaint |
| See the whole | 整体观 | Map a symptom to a system's imbalance, not a disease label |
| Adjust toward balance | 调和致中 | Aim at restoring the middle, not eliminating a target |
| Know the limit | 知边界 | Hand acute/diagnostic cases to a licensed physician |

### 辨证 Differentiate the Pattern, not the symptom

The core method of the *Neijing* is **辨证论治** — pattern differentiation. The same symptom splits by pattern; different symptoms can share one pattern.

| Axis | Chinese | Why it matters |
|------|---------|----------------|
| Cold / Heat | 寒 / 热 | Opposite directions of adjustment |
| Deficiency / Excess | 虚 / 实 | Nourish vs. drain |
| Exterior / Interior | 表 / 里 | Where the disharmony sits |
| Yin / Yang | 阴 / 阳 | The master coordinate |

> Same cough, four patterns, four directions. **No symptom→cure shortcuts.**

### 三因制宜 Three-Cause Tailoring — one size fits no one

| Cause | Chinese | The advice changes with... |
|-------|---------|----------------------------|
| Person | 因人 | constitution: elder / child / postpartum / deficient-excess |
| Time | 因时 | season & solar term |
| Place | 因地 | geography: damp south vs. dry north |

> Individualization is the floor, not a bonus. 《素问·上古天真论》: *"法于阴阳,和于术数,食饮有节,起居有常"* — pattern yourself on yin-yang, eat with measure, live with regularity.

### 形神合一 Body-and-Spirit as One

The *Neijing* binds emotion to organ system (七情五志): anger↔liver, joy↔heart, worry/pensiveness↔spleen, grief↔lung, fear↔kidney. AI never treats the body while ignoring the mood.

## East Meets West

MiaoShou doesn't replace evidence-based medicine. It **completes** the bedside manner.

| Western | + Chinese | = Complete |
|---------|-----------|------------|
| Symptom checklist | 辨证 pattern view | Advice that fits *this* person |
| Acute-care reflex | 治未病 prevention-first | Care before crisis |
| Generic guidelines | 三因制宜 tailoring | Right for season, body, place |
| Body-only model | 形神合一 body+spirit | Mood and body seen together |

## Installation

### Claude Code plugin (one command)
```bash
# Add the marketplace, then install the plugin
/plugin marketplace add wuji-labs/miaoshou-tiancheng
/plugin install miaoshou-tiancheng
```

### Bare clone (any platform)
```bash
# Copy to your skills directory
cp -r miaoshou-tiancheng ~/.claude/skills/
# or
cp -r miaoshou-tiancheng ~/.codex/skills/
```
See `platforms/claude-code.md` and `platforms/codex.md`.

### Cursor
Copy the rule into `.cursor/rules/`. See `platforms/cursor.md`.

## How to Invoke

| Mode | How | Notes |
|------|-----|-------|
| **Automatic** | Ask any wellness/调理/食养/节气 question, or mention 失眠/上火/亚健康/体质… | The `description` triggers the skill |
| **Manual** | `/miaoshou-tiancheng <your question>` | Explicit entry, fixed status-line output |
| **Subagent** | Delegate to the `tiancheng-physician` agent | Multi-turn intake: 察候→辨证→三因→守边界 |

## Worked Examples

- `examples/01-insomnia-pattern-differentiation.md` — same symptom, opposite patterns.
- `examples/02-seasonal-food-three-cause.md` — person / time / place tailoring.
- `examples/03-health-copy-redline-audit.md` — efficacy/fear red-line audit.

## Benchmark (design only)

`benchmark/scenarios.json` (6 real scenarios) + `benchmark/README_BENCHMARK.md` specify a
baseline-vs-skill evaluation with an explicit scoring rubric. **No results are run or
included — this repo ships zero fabricated numbers.** See the benchmark README.

## Source & Provenance

Every classical quote in `reference/huangdi-neijing.md` is tagged with **book·chapter**
(《素问·…》/《灵枢·…》). Framework descriptions carry no quotation marks and never
impersonate original text. Herbal data is restated as **traditional records, not proven
efficacy**. 中文版见 [README.zh-CN.md](./README.zh-CN.md).

## ⚠️ Important — Advisory Only

This skill produces **advisory wellness content only**. It is **not** medical diagnosis, treatment, prescription, or any professional decision basis. Traditional "effects" recorded in the *Neijing* and herbal data are **cultural knowledge, not clinically proven efficacy**. For any ailment, acute condition, pregnancy, or medication question, **consult a licensed physician**. Under this skill, AI must not diagnose, promise efficacy, prescribe dosage, or discourage seeking care.

## From the Same Stream

- [**TianGong**](https://github.com/wuji-labs/tiangong) — 5000 years of Chinese aesthetic wisdom for AI design.
- [**NoPUA**](https://github.com/wuji-labs/nopua) — drives AI with trust instead of fear.

> **法于阴阳,和于术数。**
> Pattern yourself on yin and yang; harmonize with the arts of measure.
> — 《素问·上古天真论》 Huangdi Neijing, Suwen, Ch. "On the Innate True (Qi) of High Antiquity"

---

## 基本信息

| 项 | 值 |
|----|-----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/miaoshou-tiancheng/` |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/miaoshou-tiancheng |
| 版本 | v1.0 · 2026-06-02 |

*妙手天成 MiaoShou TianCheng — by [WUJI](https://github.com/wuji-labs)*
*Healing begins not with the cure, but with seeing the whole person.*
