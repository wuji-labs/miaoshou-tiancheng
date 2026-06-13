# 妙手天成 MiaoShou TianCheng — Healing Hands (Manos prodigiosas que el cielo perfecciona)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/miaoshou-tiancheng"><img src="https://www.skills.sh/b/wuji-labs/miaoshou-tiancheng" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)** | **🇪🇸 Español** | **[🇧🇷 Português](README.pt.md)** | **[🇫🇷 Français](README.fr.md)**

> Este es uno de los diez regalos que la corriente de sabiduría china ofrece a la comunidad mundial de código abierto (叩兩端·無極樞紐).
> No alzamos un centrismo chino ni sostenemos que civilización alguna sea superior a otra; sencillamente partimos de la corriente que mejor conocemos,
> la pulimos hasta volverla una herramienta útil y la colocamos en el estante común de herramientas de código abierto de la humanidad. Con el tiempo llegarán también,
> uno tras otro, los regalos de las corrientes griega, de Nalanda, hebrea y persa, formando juntos una matriz de capacidades de código abierto que dialoga con doce civilizaciones.

---

> **上工治未病** — El médico superior trata lo que aún no es enfermedad.
> — *Suwen · Gran tratado de la afinación del espíritu según los cuatro qi* (素问·四气调神大论), Huangdi Neijing, *Inner Canon of the Yellow Emperor*

**Tu IA diagnostica síntomas. Enséñale a ver a la persona entera.**

La mayor parte del entrenamiento de IA en salud asigna **síntoma → respuesta**: «insomnio» → «aquí tienes 8 consejos para dormir». Limpio, rápido e impersonal — la misma lista para un adolescente ansioso, una madre en posparto y un anciano agotado. Trata la queja, nunca a la persona.

**MiaoShou TianCheng** (妙手天成) infunde el marco integrador del *Huangdi Neijing* (黄帝内经, *Inner Canon of the Yellow Emperor*, de hace unos 2000 años) en el modo en que la IA da consejo de salud y bienestar. No para prescribir, sino para **mirar** —la estación, la constitución, la emoción y el equilibrio— antes de hablar. No traza atajos de síntoma a cura; hace las preguntas justas, conoce sus límites y devuelve los casos difíciles a un médico colegiado.

## El problema

```
Tú: «Últimamente estoy agotado y no puedo dormir.»

IA sin MiaoShou:  «Prueba: hora fija de acostarte, nada de cafeína,
                  nada de pantallas, magnesio, meditación, cuarto
                  más fresco…»
                  (La misma lista para todos. Sin preguntar nada.)

IA con MiaoShou:  «¿Cuándo empezó, y en qué estación?
                  ¿Te cuesta conciliar el sueño o despiertas pronto?
                  ¿Cenas copiosamente? ¿Cargas con alguna preocupación?
                  — En la tradición, el insomnio por un estómago
                  inquieto y el que nace de la desarmonía
                  corazón-riñón apuntan en direcciones opuestas.
                  Veamos primero cuál es, y luego ajustemos con suavidad.
                  (Y si esto persiste, acude por favor a un médico.)»
```

## Qué le enseña a la IA

### 治未病 Tratar-lo-que-aún-no-es-enfermedad — la jugada por defecto

| Principio | Chino | Lo que hace la IA |
|-----------|-------|-------------------|
| Prevenir antes del inicio | 未病先防 | Pregunta por rutina/estación/ánimo *antes* de la queja |
| Ver el todo | 整体观 | Asigna un síntoma al desequilibrio de un sistema, no a una etiqueta de enfermedad |
| Ajustar hacia el equilibrio | 调和致中 | Apunta a restaurar el medio, no a eliminar un blanco |
| Conocer el límite | 知边界 | Deriva los casos agudos/diagnósticos a un médico colegiado |

### 辨证 Diferenciar el patrón, no el síntoma

El método nuclear del *Neijing* es **辨证论治** — la diferenciación de patrones. El mismo síntoma se escinde según el patrón; síntomas distintos pueden compartir un mismo patrón.

| Eje | Chino | Por qué importa |
|-----|-------|-----------------|
| Frío / Calor | 寒 / 热 | Direcciones opuestas de ajuste |
| Deficiencia / Exceso | 虚 / 实 | Nutrir frente a drenar |
| Exterior / Interior | 表 / 里 | Dónde se asienta la desarmonía |
| Yin / Yang | 阴 / 阳 | La coordenada maestra |

> La misma tos, cuatro patrones, cuatro direcciones. **Sin atajos de síntoma→cura.**

### 三因制宜 Adecuación según las tres causas — ninguna talla sirve a todos

| Causa | Chino | El consejo cambia con... |
|-------|-------|--------------------------|
| Persona | 因人 | constitución: anciano / niño / posparto / deficiencia-exceso |
| Tiempo | 因时 | estación y término solar |
| Lugar | 因地 | geografía: sur húmedo frente a norte seco |

> La individualización es el suelo, no un extra. *Suwen · Tratado de la verdad innata de la alta antigüedad* (素问·上古天真论): «法于阴阳,和于术数,食饮有节,起居有常» — modélate sobre el yin-yang, come con medida, vive con regularidad.

### 形神合一 Cuerpo y espíritu como uno

El *Neijing* ata la emoción al sistema de órganos (七情五志): ira↔hígado, alegría↔corazón, cavilación↔bazo, aflicción↔pulmón, miedo↔riñón. La IA nunca trata el cuerpo ignorando el ánimo.

## Oriente se encuentra con Occidente

MiaoShou no reemplaza la medicina basada en la evidencia. **Completa** el trato junto al lecho.

| Occidental | + Chino | = Completo |
|------------|---------|------------|
| Lista de síntomas | 辨证 la visión por patrones | Consejo que se ajusta a *esta* persona |
| Reflejo de cuidado agudo | 治未病 la prevención primero | Cuidado antes de la crisis |
| Guías genéricas | 三因制宜 la adecuación | Acertado para la estación, el cuerpo y el lugar |
| Modelo de solo cuerpo | 形神合一 cuerpo+espíritu | Ánimo y cuerpo vistos juntos |

## Instalación

### Plugin de Claude Code (un comando)
```bash
# Añade el marketplace y luego instala el plugin
/plugin marketplace add wuji-labs/miaoshou-tiancheng
/plugin install miaoshou-tiancheng
```

### Clon directo (cualquier plataforma)
```bash
# Copia a tu directorio de skills
cp -r miaoshou-tiancheng ~/.claude/skills/
# o
cp -r miaoshou-tiancheng ~/.codex/skills/
```
Véase `platforms/claude-code.md` y `platforms/codex.md`.

### Cursor
Copia la regla en `.cursor/rules/`. Véase `platforms/cursor.md`.

## Cómo invocarla

| Modo | Cómo | Notas |
|------|------|-------|
| **Automático** | Haz cualquier pregunta de bienestar/调理/食养/节气, o menciona 失眠/上火/亚健康/体质… | La `description` dispara la skill |
| **Manual** | `/miaoshou-tiancheng <tu pregunta>` | Entrada explícita, salida de línea de estado fija |
| **Subagente** | Delega en el agente `tiancheng-physician` | Anamnesis multironda: 察候→辨证→三因→守边界 (observar los signos → diferenciar el patrón → adecuar las tres causas → guardar los límites) |

## Ejemplos resueltos

- `examples/01-insomnia-pattern-differentiation.md` — mismo síntoma, patrones opuestos.
- `examples/02-seasonal-food-three-cause.md` — adecuación por persona / tiempo / lugar.
- `examples/03-health-copy-redline-audit.md` — auditoría de línea roja sobre eficacia/miedo.

## Benchmark (solo de diseño)

`benchmark/scenarios.json` (6 escenarios reales) + `benchmark/README_BENCHMARK.md` especifican
una evaluación baseline-vs-skill con una rúbrica de puntuación explícita. **No se ejecuta ni incluye
resultado alguno: este repositorio no entrega cifras fabricadas.** Véase el README del benchmark.

## Origen y procedencia

Cada cita clásica en `reference/huangdi-neijing.md` lleva etiqueta de **libro·capítulo**
(《素问·…》/《灵枢·…》). Las descripciones del marco no llevan comillas y nunca suplantan el
texto original. Los datos herbales se reformulan como **registros tradicionales, no eficacia probada**.
La versión en chino está en [README.zh-CN.md](./README.zh-CN.md).

## ⚠️ Importante — Solo carácter orientativo

Esta skill produce **únicamente contenido orientativo de bienestar**. **No** es diagnóstico médico, tratamiento, prescripción ni base de decisión profesional alguna. Los «efectos» tradicionales registrados en el *Neijing* y en los datos herbales son **conocimiento cultural, no eficacia clínicamente probada**. Para cualquier dolencia, condición aguda, embarazo o duda sobre medicación, **consulta a un médico colegiado**. Bajo esta skill, la IA no debe diagnosticar, prometer eficacia, prescribir dosis ni disuadir de buscar atención.

## De la misma corriente

- [**TianGong**](https://github.com/wuji-labs/tiangong) — 5000 años de sabiduría estética china para el diseño con IA.
- [**NoPUA**](https://github.com/wuji-labs/nopua) — mueve a la IA con confianza en lugar de miedo.

> **法于阴阳,和于术数。**
> Modélate sobre el yin y el yang; armonízate con las artes de la medida.
> — *Suwen · Tratado de la verdad innata de la alta antigüedad* (素问·上古天真论), Huangdi Neijing

---

## Información básica

| Campo | Valor |
|-------|-------|
| Pertenencia | WUJI Labs |
| Directorio | `labs/skills/miaoshou-tiancheng/` |
| Licencia | MIT |
| Origen | github.com/wuji-labs/miaoshou-tiancheng |
| Versión | v1.0 · 2026-06-02 |

*妙手天成 MiaoShou TianCheng — 乾元無極實驗室 · WUJI Labs*
*La cura no empieza en el remedio, sino en ver a la persona entera.*
