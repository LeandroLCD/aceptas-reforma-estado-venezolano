# H12 — Sistema de Seguridad Social (LOSSS + diseño previsional)

**Estado**: ABIERTA
**Fecha apertura**: 2026-10-14
**Origen**: revisión posterior a H11 (catálogo ampliado a 11 ministerios). Al separar la seguridad social contributiva (Ministerio de Trabajo, FT.11) de la no contributiva (Ministerio de Salud, FT.10) aparece un hueco de diseño: el proyecto tiene las dos fichas, pero no tiene el sistema previsional escrito.

## Por qué hace falta

La seguridad social está repartida en cinco lugares del repositorio (propuesta-reforma, FT.10, FT.11, marco comparativo y BND) y **no tiene un artefacto propio**. Las fichas la describen; nadie la diseña. Hoy hay que reconstruir el régimen previsional leyendo dos ministerios.

## Identified gaps

1. **No existe la Ley Orgánica del Sistema de Seguridad Social (LOSSS)**. Solo se menciona como "reforma LOTSS" en FT.11 §1.2. Es la pieza central ausente.
2. **No hay sección previsional en el texto articulado**. Hoy el Título IV es salud y el Título V es laboral; falta un Título previsional.
3. **El sistema de fondos de pensión no tiene diseño**. "Pilar estatal fijo más fondos privados" es una sola línea: sin nombre del régimen, sin tablas actuariales, sin reglas de portabilidad, sin tratamiento del pasivo, sin costo de transición (la propuesta solo estima USD 200-400M de capitalización inicial, sin fuente).
4. **No hay chiffrado del pasivo previsional** (obligaciones derivadas del IVSS y del fondo de pensiones vigente). Sin ese número no se puede defender el pilar mixto ni evaluar la sostenibilidad de la PBU.
5. **No hay ficha técnica del sistema previsional** como tal, ni KPIs de cobertura, de densidad de beneficiarios, ni metas de formalización.

## Tareas

- [ ] **H12.1** Chiffrar el pasivo previsional vigente (IVSS + fondo de pensiones), con fuentes verificables en `kb_gobierno` y declare de supuestos. Es el insumo de todo lo demás.
- [ ] **H12.2** Redactar la **LOSSS**: régimen contributivo (IVSS reformado, ~(A) arity de cotización), régimen no contributivo (LPSM, PBU), señales clear de competencia ministerial y régimen de transición entre ambos.
- [ ] **H12.3** Diseñar el **régimen de fondos** de pensión (pilar mixto): nombre, esquema de contribuciones, tablas actuariales, portabilidad entre fondos, gobernanza independiente y reglas anti-captura política.
- [ ] **H12.4** Añadir el **Título previsional** al texto articulado (hoy Títulos I-V: el nuevo encaja como Título VI) y articularlo con la cláusula de continuidad (3/4 + referéndum sobre el derecho a la pensión).
- [ ] **H12.5** Propagar a `README.md`, `fichas-tecnicas/README.md`, `documento/documento-final-v0.1.md` y `referencias/propuesta-reforma.md`.
- [ ] **H12.6** Reingerar con `ingest_limpio.py --append` y actualizar `~/qdrant-kb/memory.md`.

## Decisiones pendientes (resolver antes de redactar)

1. ¿**Nombre del régimen** de fondos? (cuentas individuales tipo Chile/AFP, o cuentas individuales complementarias al pilar público — decisión que define si se duplica o se sustituye el sistema actual).
2. ¿El **pilar privado es obligatorio** u opcional? Si es opcional, el pilar público tiene que ser suficiente por sí solo (y su costo hay que sackarlo).
3. ¿La PBU **se financiera con recursos hidráulicos** del BCV, con impuesto de solidsaridad, o con el excedente del sistema contributivo reformado?
4. ¿Se **reconoce el pasivo** como deuda soberana (como se hizo con la deuda pública en LOAFSP) o se asume por ley una pesificación gradual? Condiciona el costo fiscal de todo el sistema.

## Coherencia ya resuelta (2026-10-14)

- PBU fijada en **USD 500/beneficiario/año**; el presupuesto LPSM de **550 M USD/año** financia **1,1 M de beneficiarios** (0,6 M en año 3). Cobertura universal en el derecho, por etapas en el universo; ampliación por ley especial (régimen FAN). Registrado en FT.10 §7 y en `referencias/propuesta-reforma.md` §8.3.2.
- Eliminada la contradicción de FT.10 §3 sobre el IVSS: el IVSS **completo** va al Ministerio de Trabajo como ente autónomo; la seguridad social no contributiva **permanece** en Salud sin entidad propia (Art. 86 CRBV reformado).

## Referencias

- `fichas-tecnicas/FT.10-ministerio-salud.md` §1.2 (LPSM) y §3 (ente no contributivo)
- `fichas-tecnicas/FT.11-ministerio-trabajo.md` §1.2 (LOTSS), §2.2.3 (IVSS, mochila, seguro) y §3 (ente #1 y #3)
- `referencias/propuesta-reforma.md` §8.3.2 (escala salarial y PBU)
- `referencias/marco-comparativo-milei-singapur.md` (mochila austríaca, seguro de cesantía chileno Ley 19.728)
- Art. 86, 87, 91, 92 CRBV (texto verificado en `data/venezuela/constitucion/1999/crbv_1999.pdf`)
- LOT vigente (2012) en `data/venezuela/ley/2012/lottt_2012.pdf`