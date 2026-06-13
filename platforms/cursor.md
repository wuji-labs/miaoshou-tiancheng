# 妙手天成 · Cursor 适配入口

## 安装

Cursor 通过 `.cursor/rules/` 下的规则文件(`.mdc`)加载行为指令。
把本 skill 的核心原则落成一条 rule:

1. 在项目根建 `.cursor/rules/miaoshou-tiancheng.mdc`。
2. 写入下方模板(指向 SKILL.md 与弹药库,保持单一真源)。

```mdc
---
description: 妙手天成 — 以《黄帝内经》整体框架给健康/养生/调理/食养建议(建议性内容,非医疗诊断)
globs:
alwaysApply: false
---

# 妙手天成 MiaoShou TianCheng

当任务涉及养生、调理、节气起居、食养、性味归经、亚健康调理、健康问诊话术时,
遵循 `labs/skills/miaoshou-tiancheng/SKILL.md` 的四底层原则:

1. 治未病:先问起居/情志/饮食/季节,再谈具体不适;整体观先于对症。
2. 辨证而非辨症:先收寒热虚实表里阴阳维度,缺维度就追问,问不清只给通则。
3. 三因制宜:按体质/节气(见 solar-terms.json)/地域给个体化方向。
4. 以道驭术·知边界:引《黄帝内经》注"《素问·篇名》/《灵枢·篇名》",不确定不杜撰;
   禁健康焦虑式话术;急症/确诊/用药导向执业医师。

弹药库:`labs/skills/miaoshou-tiancheng/reference/huangdi-neijing.md`
本草数据(只读,如实转述传统性味功效,不当疗效):
  shared/daotong/data/materia-alimentaria.json (238 味)
  shared/daotong/data/shengnong-bencao.json (365 味)

每次涉健康建议的输出末尾必挂免责声明:
本内容为建议性养生知识,非医疗诊断/治疗/用药依据,身体不适请咨询执业医师。
```

## 加载机制

- `alwaysApply: false` + `description` → Cursor 在语义相关时按需注入(Agent/Edit 模式)。
- 也可设 `globs` 让规则在编辑特定健康内容文件时自动生效。
- 显式:在 Composer 中 `@miaoshou-tiancheng` 引用该 rule。

## 行为约定

与 Claude Code / Codex 入口一致:整体观 → 辨证 → 三因落地 → 守边界;
引经注"书·篇";末尾挂免责声明;急症导向医师;禁恐吓式驱动。

## 协同

对外文案合规 → `compliance-scan-wuji`;食养 → `subs/shiyi`;营养循证 → `subs/budwig-center`;医道纵深 → `labs/yidao-zhizhong`。
