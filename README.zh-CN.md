# 妙手天成 MiaoShou TianCheng — Healing Hands

这是华夏道脉献给世界开源社区的十件礼物之一(叩兩端·无极樞纽)。
我们不立华夏本位,不主张华夏文明优于任何文明;我们只是先从自己最熟悉的道脉开始,
把它打磨成一件可用的工具,放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来,共同构成十二文明对标的开源能力矩阵。

> **上工治未病** — 最好的医者,治的是"还没病"。
> — 《素问·四气调神大论》

---

## 一句话

**你的 AI 在"对症查病";教它"看见整个人"。**

多数健康类训练把回答做成 **症状→方案** 的直连:问"失眠"就甩八条助眠贴士——
干净、快、却没有人。同一张清单发给焦虑的少年、产后的母亲、疲惫的老人。
它接住了"主诉",却从没接住"这个人"。

**妙手天成**把《黄帝内经》(约两千年)的整体框架,注入 AI 给健康/养生建议的方式里——
不是为了"开方",而是为了在开口前**先看**:看季节、看体质、看情志、看平衡。
它不走"症状→疗法"的捷径;它先问对问题,守得住边界,把超范围的难题诚实交还执业医师。

## 它教 AI 什么

| 原则 | 一句话 | AI 的动作 |
|------|--------|-----------|
| 治未病 | 未病先防、整体观、调和致中、知边界 | 先问起居/季节/情志,再谈不适;该就医就转诊 |
| 辨证而非辨症 | 同病异治、异病同治 | 先收寒热/虚实/表里/阴阳,不做"失眠=助眠"直连 |
| 三因制宜 | 因人/因时/因地 | 同一建议按体质/节气/地域给出不同方向 |
| 形神合一 | 七情五志连着五脏 | 谈躯体必带一句情志询问 |
| 以道驭术 | 用信任替代恐惧 | 禁健康焦虑营销、禁疗效承诺、禁诊断断言 |

## Before / After

```
用户:我最近总是疲乏失眠,怎么办?

未用本 skill: "固定作息、别看手机、少喝咖啡、补镁、冥想……"(千人一面,无追问)

用本 skill:   "先别急着列清单——同样睡不着,在《内经》里可能是相反两个方向。
              几时起的、什么季节?入睡难还是早醒?睡前是否过饱?最近多思还是郁怒?
              『胃不和则卧不安』与心肾不交,调法相反,得先分清。
              (若已持续数周、影响白天,请就医——本回答不能替代执业医师。)"
```

## 安装

### Claude Code 插件(一条命令)
```bash
/plugin marketplace add wuji-labs/miaoshou-tiancheng
/plugin install miaoshou-tiancheng
```

### 裸 clone(任意平台)
```bash
cp -r miaoshou-tiancheng ~/.claude/skills/
# 或 ~/.codex/skills/
```
详见 `platforms/claude-code.md` · `platforms/codex.md` · `platforms/cursor.md`。

## 调用方式

| 模式 | 怎么用 | 说明 |
|------|--------|------|
| 自动 | 直接问养生/调理/食养/节气,或提及 失眠/上火/亚健康/体质… | 由 frontmatter 触发条件激活 |
| 手动 | `/miaoshou-tiancheng <你的问题>` | 显式入口,固定状态行输出 |
| 子代理 | 委派给 `tiancheng-physician` 问诊导师 | 多轮:察候→辨证→三因→守边界 |

## 工作样例

- `examples/01-insomnia-pattern-differentiation.md` — 同症异证。
- `examples/02-seasonal-food-three-cause.md` — 因人/因时/因地。
- `examples/03-health-copy-redline-audit.md` — 疗效/恐吓红线审查。

## 评测(仅设计,无数字)

`benchmark/scenarios.json`(6 个真实场景)+ `benchmark/README_BENCHMARK.md`
给出 baseline vs skill 的对照设计与评分 rubric。
**结果待真实运行,本仓不含任何编造的 before/after 数字。**

## 溯源

`reference/huangdi-neijing.md` 中每条经典引文均标**书·篇**(《素问·…》/《灵枢·…》);
框架描述不加引号、不冒充原文;本草数据如实转述**传统记载**,非经证实的疗效。

## ⚠️ 重要 — 仅建议性

本 skill 输出为**建议性养生文化内容**,**不构成**医疗诊断、治疗、用药或任何专业决策依据。
《内经》与本草数据所载"功效"为**传统文化知识,非临床证实的疗效**。
任何身体不适、急症、孕产、用药问题,**请咨询执业医师**。本 skill 下,AI 不得做诊断断言、
不得承诺疗效、不得开具剂量、不得阻止用户就医。对外健康文案须另过 `compliance-scan-wuji`。

## 同源之作

- [**TianGong 天工**](https://github.com/wuji-labs/tiangong) — 五千年华夏美学,注入 AI 设计。
- [**NoPUA**](https://github.com/wuji-labs/nopua) — 用信任而非恐惧驱动 AI。

---

| 项 | 值 |
|----|-----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/miaoshou-tiancheng/` |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/miaoshou-tiancheng |
| 版本 | v1.0.0 · 2026-06-02 |

*妙手天成 MiaoShou TianCheng — by [WUJI](https://github.com/wuji-labs)*
*治愈不始于药,而始于看见整个人。*
