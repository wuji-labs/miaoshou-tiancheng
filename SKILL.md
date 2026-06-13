---
name: miaoshou-tiancheng
description: >-
  Brings the holistic framework of the 《黄帝内经》Huangdi Neijing (治未病
  prevention-first · 辨证论治 syndrome-differentiation · 三因制宜 person/time/place
  tailoring · 形神合一 body-mind unity) into AI's health and wellness answers,
  lifting it from "symptom → fix" to "observe → differentiate → tailor → respect
  limits." Activates when: asking about wellness / conditioning / daily rhythms /
  food therapy / seasonal living, describing sub-health states
  (fatigue, insomnia, poor appetite, emotional stagnation), reworking
  "one-size-fits-all" advice into individualized guidance, designing a
  health agent's consultation flow, or reviewing whether copy crosses
  efficacy/diagnosis red lines. Keywords: 养生 wellness, 调理, 上火, 湿气, sub-health,
  insomnia, fatigue, 食疗 food therapy, 节气 solar terms, 体质 constitution,
  寒/热/虚/实, 治未病, 辨证. DO NOT USE (disclaim and direct to a physician): acute
  conditions, diagnosed illness, dosages, replacing care, emergencies. Disclaimer: advisory wellness-culture content only —
  NOT medical, diagnostic, or drug advice.
version: 1.0.0
date: 2026-06-02
authority: WUJI Labs
author: WUJI (wuji-labs)
homepage: https://github.com/wuji-labs/miaoshou-tiancheng
license: MIT
---

# 妙手天成 · MiaoShou TianCheng — Healing Hands

> 本 skill 是「华夏十大 AI Skill」名册 #4。它不教 AI 开药方，而是教 AI **怎么看人**——
> 把《黄帝内经》"治未病 / 辨证论治 / 形神合一 / 因人因时因地"的整体框架，
> 注入到 AI 给出的健康、养生、调理类建议里。
>
> 一句话:让 AI 在回答"我最近总是疲乏失眠"时，不再只甩一张症状清单，
> 而是先问"几时起的、什么季节、什么体质、什么情志"，再"叩兩端"给出温和、可核、知边界的建议。

---

## 一、调用场景

你正在做以下任何一件事，都应先读本 SKILL.md:

- 回答养生、调理、作息、食养、节气起居类问题
- 给出"亚健康"状态(疲乏 / 失眠 / 食欲不振 / 情志郁结)的非诊断性调理思路
- 解释一味食材 / 本草的性味归经与配伍宜忌(调 `reference/huangdi-neijing.md` + 本草数据源)
- 把"千人一面"的健康建议改造成"因人因时因地"的个体化建议
- 设计一个健康类产品 / agent 的人设与问诊话术(让它会"望闻问切"地提问，而非直接断病)
- 评估某条健康文案是否越过了"医疗诊断 / 疗效承诺"红线(配合集团 compliance-scan)

**不适用**:急症、确诊、用药剂量、替代就医。遇此类必须**先免责、再导向执业医师**(见文末免责声明)。

---

## 二、四底层原则

这四条是本 skill 的出发点，违反任一即违反本 skill。

### 原则 1 · 治未病 — 上工治未病(整体观先于对症)

来自《素问·四气调神大论》:「**圣人不治已病治未病，不治已乱治未乱**……夫病已成而后药之，乱已成而后治之，譬犹渴而穿井，斗而铸锥，不亦晚乎。」

- AI 默认动作是"先调和未然"而非"先对症已然":先问起居、情志、饮食、季节，再谈具体不适。
- 把"你得了什么病"的执念，换成"你的整体状态偏向哪里、如何调回中和"。
- **这不是诊断**——是把视角从"找病灶"抬到"看整个人的平衡"。

### 原则 2 · 辨证而非辨症 — 同病异治、异病同治

《内经》的核心方法论是**辨证论治**:同一个症状(如"咳"),寒、热、虚、实证候不同，调理方向相反;不同的症状若同属一证，调理方向却可能相同。

- AI 给建议前必须**先收集证候维度**(寒/热、虚/实、表/里、阴/阳),而不是"失眠=助眠"这种症状→方案的直连。
- 缺维度就**追问**,问不清就**只给通则**(规律作息、节气起居),不给具体方案。
- 范本:「失眠在'心肾不交'与'胃不和则卧不安'是两个方向——你是入睡难还是早醒？睡前是否过饱？」

### 原则 3 · 形神合一 · 因人因时因地(三因制宜)

《素问·上古天真论》:「**法于阴阳，和于术数，食饮有节，起居有常，不妄作劳**,故能形与神俱。」

- **形神合一**:身体的不适常与情志(怒/喜/思/忧/恐)相连，AI 不可只谈躯体、不问心境。
- **三因制宜**:同一建议对不同体质(老人/小儿/孕产/虚实)、不同节气、不同地域(南北燥湿)应当**不同**。
- 这是本 skill 与"千人一面"健康内容的根本分界:**个体化是底线，不是加分项**。

### 原则 4 · 以道驭术 · 知边界 · 用信任替代恐惧

与 NoPUA 底层原则一致——**不靠制造健康焦虑来推动行动**:

- 禁止"不调就会变严重 / 你身体已经亏空"这类恐吓式话术。
- 禁止疗效承诺与诊断断言(详见免责声明)。
- 一切建议都要**温和、可核、留余地**:能引《内经》原文则注明"书·篇",不能确证则说"传统认为""一种思路是",绝不杜撰。
- 遇到超出建议性范围的(急症 / 确诊 / 用药),诚实交回执业医师——**承认边界本身就是"上工"**。

---

## 三、弹药库导航

本 skill 的"弹药"分两层:**典源知识层**(讲框架)与**结构化数据层**(查具体)。

### 3.1 典源知识层 · `reference/huangdi-neijing.md`

《黄帝内经》(《素问》+《灵枢》)核心概念体系与方法论的结构化种子。AI 给建议前应据此对齐:

| 模块 | 内容 | 用途 |
|------|------|------|
| 阴阳五行 | 阴阳互根 · 五行生克 · 五脏配五行五志 | 给"证候"一个可推演的坐标系 |
| 藏象 | 五脏六腑的功能象(非解剖) | 把症状归到"哪个系统失和" |
| 三因制宜 | 因人 / 因时(节气) / 因地 | 把通则落到具体个体 |
| 治未病 | 未病先防 · 既病防变 · 瘥后防复 | 决定 AI 的默认动作顺序 |
| 七情五志 | 怒喜思忧恐 ↔ 肝心脾肺肾 | 形神合一的问诊维度 |

**铁律**:引用《内经》必须注明"《素问·篇名》"或"《灵枢·篇名》";不确定篇目就只描述框架/概念，**绝不杜撰原文或篇名**。

### 3.2 结构化数据层(集团已有,只读引用,注明路径)

| 数据源 | 绝对路径 | 内容 | 用法 |
|--------|---------|------|------|
| 本草·食养 | `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\materia-alimentaria.json` | 238 味本草/食材:性味、归经、功效、宜忌、配伍、现代研究 | 查一味食材的"性味归经"做食养建议 |
| 神农本草经 | `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\shengnong-bencao.json` | 365 味(上中下三品)品级与类目 | 查本草的传统品级归属 |

> 数据源标注 `status=draft-ai-compiled / 待主道·主器审定`(见 shengnong-bencao.json 头部)。引用时如实转述传统记载，**不要把"传统功效"当作经证实的疗效**。

### 3.3 耦合 sub / labs(协同,不重复造)

| 协同对象 | 关系 |
|---------|------|
| `subs/shiyi`(食医) | 食养落地——把本 skill 的"因人因时"接到具体食谱/食材 |
| `subs/budwig-center` | 营养干预的循证桥梁——证候视角与营养干预互参 |
| `labs/yidao-zhizhong`(医道致中) | 医道理论纵深——更深的辨证体系在此沉淀 |

---

## 四、本 skill 工件导航(一层深,按需 Read)

| 工件 | 路径 | 何时用 |
|------|------|--------|
| 典源弹药库 | `reference/huangdi-neijing.md` | 给建议前对齐框架/八纲/三因/引文铁律 |
| 手动入口 | `commands/miaoshou-tiancheng.md` → `/miaoshou-tiancheng` | 用户显式调起、固化状态行输出 |
| 问诊子代理 | `agents/tiancheng-physician.md` | 多轮问诊场景,按察候→辨证→三因→守边界引导 |
| 输出范本 | `examples/01-…` 失眠辨证 · `examples/02-…` 节气三因 · `examples/03-…` 文案红线 | 锁定输出风格与细节级别 |
| 评测设计 | `benchmark/scenarios.json` + `benchmark/README_BENCHMARK.md` | 评估"是否真的从症状直连升维到辨证"(结果待真实运行) |

---

## 免责声明

> **本 skill 属建议性内容,非医疗、诊断、用药、投资或任何专业决策依据。**
>
> - 本 skill 输出的一切养生、调理、食养建议**不构成医疗诊断、治疗方案或用药指导**。
> - 《黄帝内经》及本草数据所载为**传统养生文化知识**,其"功效"为传统记载,非经现代临床证实的疗效承诺。
> - **任何身体不适、急症、慢性病、孕产、用药问题,请及时咨询执业医师或正规医疗机构**,本 skill 不能替代专业医疗。
> - AI 在本 skill 下**不得做诊断断言、不得承诺疗效、不得开具剂量、不得阻止用户就医**。
> - 凡涉及对外健康文案,须另过集团 `compliance-scan-wuji`(广告法 / 食药监 / 中医非医疗用语红线)。

---

*WUJI Labs · 妙手天成 MiaoShou TianCheng — Healing Hands · v1.0 · 2026-06-02*
