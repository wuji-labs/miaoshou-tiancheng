# 妙手天成 · Codex 适配入口

## 安装

复制本 skill 目录到 Codex 的 skills 目录:

```bash
cp -r miaoshou-tiancheng ~/.codex/skills/
```

集团内 Codex 默认走 app-server 长连接(ADR-0008),skill 文件随工作区可见即可加载。

## 加载机制

Codex 以 `SKILL.md` 为入口规范文件。会话开始处理养生/调理/食养类请求时,
agent 先读 `SKILL.md` 的"四底层原则"与"弹药库导航",再据需要读取:
- `reference/huangdi-neijing.md`(典源框架)
- 本草 JSON 数据源(查具体食材性味归经)

建议在 Codex 的项目级 instructions / `AGENTS.md` 中加一行指针:

```
健康/养生/调理/食养类请求 → 先读 labs/skills/miaoshou-tiancheng/SKILL.md,按其四底层原则作答。
```

## 调用方式

- **隐式**:命中 description 语义时自动援引。
- **显式**:在 prompt 中点名 "依 miaoshou-tiancheng skill 给出因人因时的调理思路"。

## 行为约定(Codex 在本 skill 下必须遵守)

1. 流程顺序:整体观 → 辨证 → 三因落地 → 守边界。
2. 引《黄帝内经》必注"书·篇";不确定不杜撰原文/篇名。
3. 涉健康建议的输出**末尾必挂免责声明**(非医疗诊断,身体不适请咨询执业医师)。
4. 急症/确诊/用药/剂量 → 不诊断、不开方,导向执业医师。
5. 禁健康焦虑/恐吓式驱动(与 NoPUA 一致)。

## 数据源(只读引用,注明路径)

- `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\materia-alimentaria.json`(238 味)
- `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\shengnong-bencao.json`(365 味)
- `\\192.168.8.112\Projects\qianyuan-wuji\shared\daotong\data\solar-terms.json`(24 节气)

转述传统性味功效,不得表述为经临床证实的疗效。

## 协同

- 对外文案合规 → `compliance-scan-wuji`
- 食养落地 → `subs/shiyi` · 营养循证 → `subs/budwig-center` · 医道纵深 → `labs/yidao-zhizhong`
