# Tarea pendiente — Ampliación del catálogo a 11 ministerios

**Estado**: ABIERTA  
**Fecha apertura**: 2026-07-26  
**Origen**: sesión de revisión del proyecto Aceptas; el usuario identificó dos ministerios faltantes en el catálogo actual de 9 ministerios.

## Contexto

El catálogo definitivo del Estado reformado (consolidado 25-jul-2026, ampliado 26-jul-2026) tiene actualmente **9 ministerios**:

1. Interior y Seguridad (FT.1)
2. MIED-LAM (FT.2)
3. Economía y Finanzas (FT.3)
4. Energía y Minas (FT.4, incluye INGEOMIN)
5. Infraestructura y Servicios (FT.5)
6. Planificación Estratégica y Prospectiva (FT.6)
7. Gobierno Digital (FT.7)
8. Relaciones Exteriores (FT.8)
9. Ambiente (FT.9)

Faltan 2 ministerios críticos que el usuario marcó como necesarios:

10. **Salud** (crear ficha técnica ministerial FT.10)
11. **Trabajo** (crear ficha técnica ministerial FT.11)

Esto implicará renombrar las fichas actuales 10 y 11 (Consejo Nacional de Defensa + Poder Ciudadano ampliado) a 12 y 13 (o ajustar la numeración).

## Tareas a ejecutar en la próxima sesión

- [ ] Decidir si el catálogo definitivo pasa de 9 a 11 ministerios, manteniendo el resto del Estado (Consejo Nacional de Defensa + Poder Ciudadano) sin cambios de numeración
- [ ] Crear ficha técnica `FT.X-ministerio-salud.md` con:
  - Resumen ejecutivo + mandato constitucional
  - Marco constitucional/legal (CRBV Arts. 83-85, 156.9, Ley Orgánica de Salud, etc.)
  - Estructura orgánica (Viceministerios de Atención Primaria + Hospitalaria + Epidemiología + Regulación Sanitaria + Salud Mental + Recursos Humanos + etc.)
  - Entes adscritos (red hospitalaria nacional, INSALUD, etc.)
  - Régimen de personal meritocrático (concursos CNSC + VePass-Firma)
  - Presupuesto estimado (% PIB) y cronograma
  - Indicadores + Riesgos + Cláusula de continuidad
- [ ] Crear ficha técnica `FT.X-ministerio-trabajo.md` con:
  - Resumen ejecutivo + mandato constitucional
  - Marco constitucional/legal (LOTTT actual, Ley Orgánica del Trabajo propuesta, CRBV Arts. 86-97, etc.)
  - Estructura orgánica (Viceministerios de Relaciones Laborales, Seguridad Social, Formación Profesional, Inspección, etc.)
  - Entes adscritos (INPSASEL, CVAL, etc.)
  - Régimen de personal meritocrático
  - Presupuesto estimado + cronograma
  - Indicadores + Riesgos + Cláusula de continuidad
  - Libertad bilateral de terminación laboral (Principio #10) + mochila austríaca 8,33% + seguro cesantía 1,2%
- [ ] Actualizar el catálogo del Estado reformado en TODOS los archivos:
  - `README.md` (raíz): tabla "Estado reformado — 12 fichas técnicas ministeriales" → 14 fichas
  - `fichas-tecnicas/README.md`: índice con 14 entradas
  - `pilares/README.md`: índice (sin cambios)
  - `documento/documento-final-v0.1.md`: secciones 0.1, IV.7, ARTICULACIÓN DOCUMENTAL
  - Frontmatter YAML de cada ficha técnica afectada (`parte`, `ente` con número)
- [ ] Renumerar las fichas 10 y 11 (Consejo Defensa + Poder Ciudadano) a 12 y 13, o ajustar el esquema
- [ ] Re-ingestar la base vectorial (no pública): `cd ~/qdrant-kb && python3 ingest.py --input-dir ./data/venezuela/borrador_reforma/2026 --collection kb_gobierno`
- [ ] Actualizar `~/qdrant-kb/memory.md` con la decisión final del catálogo de 11 ministerios + 1 Defensa + 5 Poder Ciudadano = **17 instituciones del Estado central ejecutivo + Poder Ciudadano**
- [ ] Commit + push siguiendo el flujo estándar: rama feature → PR a develop → merge con --admin → sync a main

## Decisiones pendientes

1. ¿El catálogo pasa a 11 ministerios (Salud + Trabajo), o se mantiene en 9 con menciones específicas de Salud/Trabajo dentro de otros ministerios?
2. ¿Salud se adscribe al Ministerio del Interior (Viceministerio), o se mantiene como ministerio separado?
3. ¿Trabajo se adscribe a Economía y Finanzas, o se mantiene como ministerio separado?
4. Si pasan a 11 ministerios, ¿la numeración de las fichas 10 y 11 (actuales Defensa + Poder Ciudadano) se mantiene o se corre?

## Referencias

- Catálogo actual: `fichas-tecnicas/README.md`
- Documento final: `documento/documento-final-v0.1.md` (sección 0.1, IV.7, Articulación Final)
- Frontmatter del Estado: ya documenta `ministerios: 9` y `ente_presidencial_defensa: 1`

---

**Pendiente de la sesión 2026-07-26. No avanzar sin OK explícito del usuario.**
