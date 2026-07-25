# Anexos del Proyecto de Reforma Integral del Estado Venezolano

Documentación complementaria organizada por eje temático. Cada anexo está respaldado por la base vectorial `kb_gobierno` (Qdrant, 19.125 puntos al 2026-07-25).

## Inventarios administrativos (Pilar III)

| Anexo | Descripción | Tamaño |
|---|---|---|
| [`inventario-estructura-actual.md`](./inventario-estructura-actual.md) | Inventario vigente 2026 de los ministerios del Poder Popular venezolano, con tabla de rattachación a los 9 ministerios del Estado reformado. Sintetiza el Decreto N° 6.670/2009 (entes adscritos), Wikipedia snapshot 2026-07-25 (ministerios vigentes), LOAP 2014 y Decreto N° 1.612/2015 (organigrama). | ~34 KB / 286 líneas |
| [`inventario-ministerios-2009-decreto-6670.md`](./inventario-ministerios-2009-decreto-6670.md) | Catálogo exhaustivo de los 26 ministerios del Poder Popular y ~385 entes adscritos conforme al Decreto N° 6.670 (Gaceta Oficial N° 39.163, 22-abr-2009). Sirve de línea base histórica para medir la hipertrofia 2009-2026. | ~43 KB / 460 líneas |

## Cómo citar

> **Citación interna del proyecto**: cada anexo lleva frontmatter YAML con `titulo`, `version`, `fecha`, `fuentes_principales`, `relevancia_proyecto` y `estado`. La sección final «Gaps identificados» documenta explícitamente las piezas pendientes o no disponibles.

> **Citación académico-política**: para uso externo, citar como *Aceptas Aceptas (2026), Anexo A: Inventario de la Administración Pública Venezolana vigente 2026, Proyecto Reforma Integral del Estado Venezolano v0.1, repositorio público github.com/LeandroLCD/aceptas-reforma-estado-venezolano*.

## Mantenimiento

- **Ingesta KB**: cada anexo se ingesta automáticamente en `kb_gobierno` (colección Qdrant) tras creación/modificación (`python3 ingest.py --input-dir ../kb/borrador_reforma/2026/anexos --collection kb_gobierno`).
- **Issues / Pull Requests**: abrir PR contra `main` siguiendo el formato `feat/anexo-{pilar}-{descripcion}`.
- **Lint no-CJK**: ejecutar `grep -P '[\x{4e00}-\x{9fff}]'` antes de cada commit (prohibido por convención del proyecto).
