# 妙手天成 · Claude Code 适配入口

## 安装

把本 skill 目录复制到 Claude Code 的 skills 目录:

```bash
cp -r miaoshou-tiancheng ~/.claude/skills/
```

或在项目内放到 `.claude/skills/miaoshou-tiancheng/`(随项目分发)。

## 加载机制

Claude Code 通过 `SKILL.md` 的 frontmatter(`name` / `description`)自动发现并按需加载本 skill。
本 skill 的 `name` 为 `miaoshou-tiancheng`。

当用户提问命中 description 中的语义(养生、调理、节气起居、食养、性味归经、亚健康调理、健康问诊话术设计等)时,
Claude 会先读 `SKILL.md`,据"四底层原则"对齐行为,再据"弹药库导航"调取 `reference/huangdi-neijing.md` 与本草数据源。

## 调用方式

- **隐式**:用户直接问养生/调理类问题,模型据 description 自动援引本 skill。
- **显式**:用户可在对话中点名 "用 miaoshou-tiancheng skill 看一下我的作息" 强制加载。
- **slash**:若注册为 slash 命令,可用 `/miaoshou-tiancheng <你的健康困惑>`。

## 行为约定(Claude 在本 skill 下必须遵守)

1. 先整体观、再辨证、后三因落地、最后守边界(SKILL.md 原则 1-3)。
2. 引《黄帝内经》必注明"《素问·篇名》/《灵枢·篇名》";不确定不杜撰(原则 4)。
3. **每次涉健康建议的输出,末尾必须挂免责声明**:本内容为建议性养生知识,非医疗诊断,身体不适请咨询执业医师。
4. 急症 / 确诊 / 用药 / 剂量类 → 不做诊断断言,直接导向执业医师。
5. 不用健康焦虑/恐吓话术驱动(与 NoPUA 一致)。

## 数据源(只读引用,注明路径)

- `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\materia-alimentaria.json`(238 味本草/食养)
- `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\shengnong-bencao.json`(365 味品级)
- `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\solar-terms.json`(24 节气)

读取这些 JSON 时,如实转述传统性味功效,不得表述为经临床证实的疗效。

## 协同 skill

- 对外健康文案 → 接 `compliance-scan-wuji`(广告法/食药监/中医非医疗用语红线)。
- 食养落地 → 接 `subs/shiyi`(食医);营养循证 → `subs/budwig-center`;医道纵深 → `labs/yidao-zhizhong`。
