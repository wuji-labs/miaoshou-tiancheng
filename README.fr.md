# 妙手天成 MiaoShou TianCheng — Healing Hands (Des mains prodigieuses que le ciel parachève)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/miaoshou-tiancheng"><img src="https://www.skills.sh/b/wuji-labs/miaoshou-tiancheng" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)** | **[🇪🇸 Español](README.es.md)** | **[🇧🇷 Português](README.pt.md)** | **🇫🇷 Français**

> Ceci est l'un des dix présents que le courant de sagesse chinois offre à la communauté mondiale de l'open source (叩兩端·無極樞紐).
> Nous ne dressons aucun centrisme chinois et ne prétendons pas qu'une civilisation soit supérieure à une autre ; nous partons simplement du courant que nous connaissons le mieux,
> nous le façonnons en un outil utilisable, et nous le posons sur l'étagère à outils open source commune à l'humanité. Viendront ensuite,
> tour à tour, les présents des courants grec, de Nâlandâ, hébraïque et perse, formant ensemble une matrice de capacités open source en dialogue avec douze civilisations.

---

> **上工治未病** — Le médecin supérieur traite ce qui n'est pas encore maladie.
> — *Suwen · Grand traité de l'accord de l'esprit selon les quatre qi* (素问·四气调神大论), Huangdi Neijing, *Inner Canon of the Yellow Emperor*

**Votre IA diagnostique des symptômes. Apprenez-lui à voir la personne tout entière.**

La plupart des entraînements d'IA en santé associent **symptôme → réponse** : « insomnie » → « voici 8 conseils pour dormir ». Net, rapide et impersonnel — la même liste pour un adolescent anxieux, une mère en post-partum et un vieillard épuisé. Cela traite la plainte, jamais la personne.

**MiaoShou TianCheng** (妙手天成) infuse le cadre intégratif du *Huangdi Neijing* (黄帝内经, *Inner Canon of the Yellow Emperor*, vieux d'environ 2000 ans) dans la manière dont l'IA donne ses conseils de santé et de bien-être. Non pour prescrire, mais pour **regarder** — la saison, la constitution, l'émotion et l'équilibre — avant de parler. Elle ne trace aucun raccourci du symptôme au remède ; elle pose les bonnes questions, connaît ses limites et renvoie les cas difficiles à un médecin agréé.

## Le problème

```
Vous : « Ces temps-ci je suis épuisé et je n'arrive pas à dormir. »

IA sans MiaoShou :  « Essayez : heure de coucher fixe, pas de caféine,
                    pas d'écrans, du magnésium, de la méditation, une
                    chambre plus fraîche… »
                    (La même liste pour tous. Sans rien demander.)

IA avec MiaoShou :  « Quand cela a-t-il commencé, et à quelle saison ?
                    Difficulté à vous endormir, ou réveil précoce ?
                    Mangez-vous lourd avant de dormir ? Portez-vous un souci ?
                    — Dans la tradition, l'insomnie née d'un estomac
                    troublé et celle née de la désharmonie cœur-rein
                    pointent en sens opposés.
                    Voyons d'abord laquelle, puis ajustons en douceur.
                    (Et si cela persiste, consultez un médecin, je vous prie.) »
```

## Ce qu'elle enseigne à l'IA

### 治未病 Traiter-ce-qui-n'est-pas-encore-maladie — le geste par défaut

| Principe | Chinois | Ce que fait l'IA |
|----------|---------|------------------|
| Prévenir avant le déclenchement | 未病先防 | Interroge le rythme/la saison/l'humeur *avant* la plainte |
| Voir le tout | 整体观 | Rattache un symptôme au déséquilibre d'un système, non à une étiquette de maladie |
| Ajuster vers l'équilibre | 调和致中 | Vise à restaurer le milieu, non à éliminer une cible |
| Connaître la limite | 知边界 | Oriente les cas aigus/diagnostiques vers un médecin agréé |

### 辨证 Différencier le tableau, non le symptôme

La méthode au cœur du *Neijing* est le **辨证论治** — la différenciation des tableaux. Le même symptôme se scinde selon le tableau ; des symptômes distincts peuvent partager un même tableau.

| Axe | Chinois | Pourquoi cela compte |
|-----|---------|----------------------|
| Froid / Chaleur | 寒 / 热 | Directions d'ajustement opposées |
| Vide / Plénitude | 虚 / 实 | Nourrir contre drainer |
| Surface / Profondeur | 表 / 里 | Où siège la désharmonie |
| Yin / Yang | 阴 / 阳 | La coordonnée maîtresse |

> La même toux, quatre tableaux, quatre directions. **Aucun raccourci du symptôme au remède.**

### 三因制宜 Adaptation aux trois causes — aucune taille unique ne convient à tous

| Cause | Chinois | Le conseil change selon... |
|-------|---------|----------------------------|
| La personne | 因人 | constitution : vieillard / enfant / post-partum / vide-plénitude |
| Le temps | 因时 | la saison et le terme solaire |
| Le lieu | 因地 | la géographie : sud humide contre nord sec |

> L'individualisation est le plancher, non un bonus. *Suwen · Traité de la vérité innée de la haute antiquité* (素问·上古天真论) : « 法于阴阳,和于术数,食饮有节,起居有常 » — règle-toi sur le yin-yang, mange avec mesure, vis avec régularité.

### 形神合一 Le corps et l'esprit ne font qu'un

Le *Neijing* lie l'émotion au système d'organes (七情五志) : colère↔foie, joie↔cœur, rumination↔rate, affliction↔poumon, peur↔rein. L'IA ne traite jamais le corps en ignorant l'humeur.

## L'Orient rencontre l'Occident

MiaoShou ne remplace pas la médecine fondée sur les preuves. Elle **complète** l'art du chevet.

| Occidental | + Chinois | = Complet |
|------------|-----------|-----------|
| Liste de symptômes | 辨证 la vision par tableaux | Un conseil qui convient à *cette* personne |
| Réflexe de soin aigu | 治未病 la prévention d'abord | Un soin avant la crise |
| Recommandations génériques | 三因制宜 l'adaptation | Juste pour la saison, le corps et le lieu |
| Modèle du corps seul | 形神合一 corps+esprit | L'humeur et le corps vus ensemble |

## Installation

### Plugin Claude Code (une commande)
```bash
# Ajoutez le marketplace, puis installez le plugin
/plugin marketplace add wuji-labs/miaoshou-tiancheng
/plugin install miaoshou-tiancheng
```

### Clone direct (toute plateforme)
```bash
# Copiez vers votre répertoire de skills
cp -r miaoshou-tiancheng ~/.claude/skills/
# ou
cp -r miaoshou-tiancheng ~/.codex/skills/
```
Voir `platforms/claude-code.md` et `platforms/codex.md`.

### Cursor
Copiez la règle dans `.cursor/rules/`. Voir `platforms/cursor.md`.

## Comment l'invoquer

| Mode | Comment | Notes |
|------|---------|-------|
| **Automatique** | Posez toute question de bien-être/调理/食养/节气, ou mentionnez 失眠/上火/亚健康/体质… | La `description` déclenche la skill |
| **Manuel** | `/miaoshou-tiancheng <votre question>` | Entrée explicite, sortie en ligne d'état fixe |
| **Sous-agent** | Déléguez à l'agent `tiancheng-physician` | Interrogatoire multi-tours : 察候→辨证→三因→守边界 (observer les signes → différencier le tableau → adapter les trois causes → garder les limites) |

## Exemples travaillés

- `examples/01-insomnia-pattern-differentiation.md` — même symptôme, tableaux opposés.
- `examples/02-seasonal-food-three-cause.md` — adaptation selon la personne / le temps / le lieu.
- `examples/03-health-copy-redline-audit.md` — audit de ligne rouge sur l'efficacité/la peur.

## Benchmark (conception seulement)

`benchmark/scenarios.json` (6 scénarios réels) + `benchmark/README_BENCHMARK.md` spécifient
une évaluation baseline-contre-skill assortie d'une grille de notation explicite. **Aucun résultat n'est
exécuté ni inclus — ce dépôt ne livre aucun chiffre fabriqué.** Voir le README du benchmark.

## Source et provenance

Chaque citation classique dans `reference/huangdi-neijing.md` porte l'étiquette **livre·chapitre**
(《素问·…》/《灵枢·…》). Les descriptions du cadre ne portent pas de guillemets et n'usurpent
jamais le texte original. Les données sur les plantes sont reformulées comme des **consignations
traditionnelles, et non une efficacité prouvée**. La version chinoise est dans [README.zh-CN.md](./README.zh-CN.md).

## ⚠️ Important — À titre indicatif seulement

Cette skill ne produit qu'un **contenu de bien-être à titre indicatif**. Ce n'est **pas** un diagnostic médical, un traitement, une prescription ni un fondement de décision professionnelle quelconque. Les « effets » traditionnels consignés dans le *Neijing* et dans les données sur les plantes relèvent du **savoir culturel, et non d'une efficacité cliniquement prouvée**. Pour toute affection, état aigu, grossesse ou question de médication, **consultez un médecin agréé**. Sous cette skill, l'IA ne doit pas diagnostiquer, promettre une efficacité, prescrire une posologie ni dissuader de recourir aux soins.

## Du même courant

- [**TianGong**](https://github.com/wuji-labs/tiangong) — 5000 ans de sagesse esthétique chinoise pour le design avec IA.
- [**NoPUA**](https://github.com/wuji-labs/nopua) — meut l'IA par la confiance plutôt que par la peur.

> **法于阴阳,和于术数。**
> Règle-toi sur le yin et le yang ; accorde-toi aux arts de la mesure.
> — *Suwen · Traité de la vérité innée de la haute antiquité* (素问·上古天真论), Huangdi Neijing

---

## Informations de base

| Champ | Valeur |
|-------|--------|
| Rattachement | WUJI Labs |
| Répertoire | `labs/skills/miaoshou-tiancheng/` |
| Licence | MIT |
| Amont | github.com/wuji-labs/miaoshou-tiancheng |
| Version | v1.0 · 2026-06-02 |

*妙手天成 MiaoShou TianCheng — 乾元無極實驗室 · WUJI Labs*
*La guérison ne commence pas au remède, mais à voir la personne tout entière.*
