# 妙手天成 MiaoShou TianCheng — Healing Hands (Mãos prodigiosas que o céu aperfeiçoa)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/miaoshou-tiancheng"><img src="https://www.skills.sh/b/wuji-labs/miaoshou-tiancheng" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)** | **[🇪🇸 Español](README.es.md)** | **🇧🇷 Português** | **[🇫🇷 Français](README.fr.md)**

> Este é um dos dez presentes que a corrente de sabedoria chinesa oferece à comunidade mundial de código aberto (叩兩端·無極樞紐).
> Não erguemos um centrismo chinês nem afirmamos que civilização alguma seja superior a outra; apenas partimos da corrente que melhor conhecemos,
> lapidamo-la até se tornar uma ferramenta útil e a colocamos na prateleira comum de ferramentas de código aberto da humanidade. Com o tempo chegarão também,
> um após o outro, os presentes das correntes grega, de Nalanda, hebraica e persa, formando juntos uma matriz de capacidades de código aberto que dialoga com doze civilizações.

---

> **上工治未病** — O médico superior trata o que ainda não é doença.
> — *Suwen · Grande tratado da afinação do espírito segundo os quatro qi* (素问·四气调神大论), Huangdi Neijing, *Inner Canon of the Yellow Emperor*

**Sua IA diagnostica sintomas. Ensine-a a ver a pessoa inteira.**

A maior parte do treinamento de IA em saúde mapeia **sintoma → resposta**: «insônia» → «aqui vão 8 dicas para dormir». Limpo, rápido e impessoal — a mesma lista para um adolescente ansioso, uma mãe no pós-parto e um idoso exausto. Trata a queixa, nunca a pessoa.

**MiaoShou TianCheng** (妙手天成) infunde o arcabouço integrador do *Huangdi Neijing* (黄帝内经, *Inner Canon of the Yellow Emperor*, de cerca de 2000 anos atrás) no modo como a IA dá conselhos de saúde e bem-estar. Não para prescrever, mas para **olhar** — a estação, a constituição, a emoção e o equilíbrio — antes de falar. Não traça atalhos de sintoma a cura; faz as perguntas certas, conhece os próprios limites e devolve os casos difíceis a um médico habilitado.

## O problema

```
Você: «Ultimamente ando exausto e não consigo dormir.»

IA sem MiaoShou:  «Tente: horário fixo para deitar, nada de cafeína,
                  nada de telas, magnésio, meditação, quarto mais
                  fresco…»
                  (A mesma lista para todos. Sem perguntar nada.)

IA com MiaoShou:  «Quando começou, e em que estação?
                  Dificuldade para pegar no sono, ou despertar precoce?
                  Come muito antes de dormir? Carrega alguma preocupação?
                  — Na tradição, a insônia de um estômago inquieto e a
                  que nasce da desarmonia coração-rim apontam para
                  direções opostas.
                  Vejamos primeiro qual é, e então ajustemos com brandura.
                  (E, se isto persistir, procure um médico, por favor.)»
```

## O que ensina à IA

### 治未病 Tratar-o-que-ainda-não-é-doença — a jogada padrão

| Princípio | Chinês | O que a IA faz |
|-----------|--------|----------------|
| Prevenir antes do início | 未病先防 | Pergunta sobre rotina/estação/humor *antes* da queixa |
| Ver o todo | 整体观 | Mapeia um sintoma ao desequilíbrio de um sistema, não a um rótulo de doença |
| Ajustar rumo ao equilíbrio | 调和致中 | Visa restaurar o meio, não eliminar um alvo |
| Conhecer o limite | 知边界 | Encaminha casos agudos/diagnósticos a um médico habilitado |

### 辨证 Diferenciar o padrão, não o sintoma

O método nuclear do *Neijing* é **辨证论治** — a diferenciação de padrões. O mesmo sintoma se reparte conforme o padrão; sintomas distintos podem partilhar um mesmo padrão.

| Eixo | Chinês | Por que importa |
|------|--------|-----------------|
| Frio / Calor | 寒 / 热 | Direções opostas de ajuste |
| Deficiência / Excesso | 虚 / 实 | Nutrir versus drenar |
| Exterior / Interior | 表 / 里 | Onde a desarmonia se assenta |
| Yin / Yang | 阴 / 阳 | A coordenada mestra |

> A mesma tosse, quatro padrões, quatro direções. **Sem atalhos de sintoma→cura.**

### 三因制宜 Adequação segundo as três causas — nenhum tamanho serve a todos

| Causa | Chinês | O conselho muda com... |
|-------|--------|------------------------|
| Pessoa | 因人 | constituição: idoso / criança / pós-parto / deficiência-excesso |
| Tempo | 因时 | estação e termo solar |
| Lugar | 因地 | geografia: sul úmido versus norte seco |

> A individualização é o chão, não um bônus. *Suwen · Tratado da verdade inata da alta antiguidade* (素问·上古天真论): «法于阴阳,和于术数,食饮有节,起居有常» — modela-te pelo yin-yang, come com medida, vive com regularidade.

### 形神合一 Corpo e espírito como um só

O *Neijing* ata a emoção ao sistema de órgãos (七情五志): ira↔fígado, alegria↔coração, cisma↔baço, pesar↔pulmão, medo↔rim. A IA nunca trata o corpo ignorando o humor.

## O Oriente encontra o Ocidente

MiaoShou não substitui a medicina baseada em evidências. **Completa** o trato à beira do leito.

| Ocidental | + Chinês | = Completo |
|-----------|----------|------------|
| Lista de sintomas | 辨证 a visão por padrões | Conselho que se ajusta a *esta* pessoa |
| Reflexo de cuidado agudo | 治未病 a prevenção primeiro | Cuidado antes da crise |
| Diretrizes genéricas | 三因制宜 a adequação | Certo para a estação, o corpo e o lugar |
| Modelo só do corpo | 形神合一 corpo+espírito | Humor e corpo vistos juntos |

## Instalação

### Plugin do Claude Code (um comando)
```bash
# Adicione o marketplace e então instale o plugin
/plugin marketplace add wuji-labs/miaoshou-tiancheng
/plugin install miaoshou-tiancheng
```

### Clone direto (qualquer plataforma)
```bash
# Copie para o seu diretório de skills
cp -r miaoshou-tiancheng ~/.claude/skills/
# ou
cp -r miaoshou-tiancheng ~/.codex/skills/
```
Veja `platforms/claude-code.md` e `platforms/codex.md`.

### Cursor
Copie a regra para `.cursor/rules/`. Veja `platforms/cursor.md`.

## Como invocar

| Modo | Como | Notas |
|------|------|-------|
| **Automático** | Faça qualquer pergunta de bem-estar/调理/食养/节气, ou mencione 失眠/上火/亚健康/体质… | A `description` dispara a skill |
| **Manual** | `/miaoshou-tiancheng <sua pergunta>` | Entrada explícita, saída de linha de status fixa |
| **Subagente** | Delegue ao agente `tiancheng-physician` | Anamnese em vários turnos: 察候→辨证→三因→守边界 (observar os sinais → diferenciar o padrão → adequar as três causas → guardar os limites) |

## Exemplos resolvidos

- `examples/01-insomnia-pattern-differentiation.md` — mesmo sintoma, padrões opostos.
- `examples/02-seasonal-food-three-cause.md` — adequação por pessoa / tempo / lugar.
- `examples/03-health-copy-redline-audit.md` — auditoria de linha vermelha sobre eficácia/medo.

## Benchmark (apenas de projeto)

`benchmark/scenarios.json` (6 cenários reais) + `benchmark/README_BENCHMARK.md` especificam
uma avaliação baseline-vs-skill com uma rubrica de pontuação explícita. **Nenhum resultado é executado
ou incluído — este repositório não entrega números fabricados.** Veja o README do benchmark.

## Origem e proveniência

Cada citação clássica em `reference/huangdi-neijing.md` traz a etiqueta de **livro·capítulo**
(《素问·…》/《灵枢·…》). As descrições do arcabouço não levam aspas e nunca se passam pelo
texto original. Os dados herbais são reformulados como **registros tradicionais, não eficácia comprovada**.
A versão em chinês está em [README.zh-CN.md](./README.zh-CN.md).

## ⚠️ Importante — Apenas de caráter consultivo

Esta skill produz **apenas conteúdo consultivo de bem-estar**. **Não** é diagnóstico médico, tratamento, prescrição nem base de decisão profissional alguma. Os «efeitos» tradicionais registrados no *Neijing* e nos dados herbais são **conhecimento cultural, não eficácia clinicamente comprovada**. Para qualquer enfermidade, condição aguda, gravidez ou dúvida sobre medicação, **consulte um médico habilitado**. Sob esta skill, a IA não deve diagnosticar, prometer eficácia, prescrever dosagem nem desencorajar a busca por atendimento.

## Da mesma corrente

- [**TianGong**](https://github.com/wuji-labs/tiangong) — 5000 anos de sabedoria estética chinesa para o design com IA.
- [**NoPUA**](https://github.com/wuji-labs/nopua) — move a IA com confiança em vez de medo.

> **法于阴阳,和于术数。**
> Modela-te pelo yin e pelo yang; harmoniza-te com as artes da medida.
> — *Suwen · Tratado da verdade inata da alta antiguidade* (素问·上古天真论), Huangdi Neijing

---

## Informações básicas

| Campo | Valor |
|-------|-------|
| Pertencimento | WUJI Labs |
| Diretório | `labs/skills/miaoshou-tiancheng/` |
| Licença | MIT |
| Origem | github.com/wuji-labs/miaoshou-tiancheng |
| Versão | v1.0 · 2026-06-02 |

*妙手天成 MiaoShou TianCheng — 乾元無極實驗室 · WUJI Labs*
*A cura não começa no remédio, mas em ver a pessoa inteira.*
