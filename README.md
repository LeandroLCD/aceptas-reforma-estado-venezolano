# Aceptas — Reforma Integral del Estado Venezolano

> *"Si aceptas, levanta la mano y grita: ¡Lo juro!"*

## ¿Qué es Aceptas?

**Aceptas** es una propuesta técnica y política de **reforma integral del Estado venezolano**, elaborada entre el 10 y el 16 de julio de 2026 con metodología de síntesis comparada (Milei arranque + Singapur método + Chile Solidario red de protección), soporte de **Knowledge Base vectorial con 18.718 chunks** (Qdrant + `multilingual-e5-small`), y anclaje en el **marco constitucional vigente (Constitución de la República Bolivariana de Venezuela (CRBV) 1999)** sin reforma constituyente.

No es un partido. No es un manifiesto ideológico. Es un **artefacto técnico-legislativo** de ~580 KB de texto articulado, 8 pilares orgánicos, 6 leyes orgánicas nuevas y 1 plan de implementación 0–36 meses.

### Lema y convocatoria

> *"Hay mucha gente que no entiende / Que el gobierno / No es el único que debe cambiar / Aquí hace falta leer y usar los cuadernos / Y reconocer que la juventud no es un don eterno."*
> — *Pa' la Calle*, Canservero

**Aceptas = narrativa fundacional, no partido político.** Quien acepta el proyecto es quien pertenece a él. Quien no acepta (por indiferencia o cálculo) está fuera del colectivo Aceptas pero no puede ser excluido como enemigo — ha sido la causa principal de la persistencia del régimen.

### Crítica constitutiva

Aceptas rechaza explícitamente la **oposición angelical**: los "angelitos" que hacen ilusión a políticos de oposición vestidos de santos, que han contribuído a la permanencia del régimen chavista. La cláusula de continuidad del proyecto sólo funciona si **el pueblo vigila**, porque sino la mayoría parlamentaria circunstancial la deshace.

---

## Estructura del repositorio

```
aceptas-reforma-estado-venezolano/
├── README.md                                      ← este archivo
├── LICENSE                                        CC BY-SA 4.0
│
├── prologo/
│   └── resumen-ejecutivo.md                       ← Punto de entrada
├── diagnostico/
│   └── diagnostico-integral.md                    ← Causa-raíz histórica (MEDI 1979-1984 + captura institucional)
├── principios/
│   └── principios-generales.md                    ← 11 principios rectores
│
├── pilares/                                       ← 8 pilares orgánicos (mecanismo central + cláusula 3/4 + referéndum)
│   ├── III.1-servicio-civil-meritocratico.md      CNSC + concursos públicos + meritocracia blindada
│   ├── III.2-seguridad-ciudadana.md               CPNP + CICPC + JNEM + VePass-Firma obligatoria
│   ├── III.3-mied-lam.md                          Ministerio del Desarrollo de la Inteligencia, Educación y Deporte
│   ├── III.4-reforma-fiscal-financiamiento.md     LOBCV + dolarización mes 18 + cronograma monetario
│   ├── III.5-reforma-economica-productiva.md      PDVSA 51% + FOSEIP + FNIP + privatización Corpoelec/CANTV/HIDROVEN
│   ├── III.6-justicia-anticorrupcion.md           TSJ meritocrático + DNA-RB + Defensor del Pueblo + MP unificado
│   ├── III.7-gobierno-digital-identidad.md        BND + VePass + Cédula-RUT + SNI + RUI + RUP
│   └── III.8-planificacion-estrategica-prospectiva.md   DNPEP + Plan Quinquenal vinculante + Presupuesto Plurianual
│
├── implementacion/                                ← Plan operativo
│   ├── plan-implementacion-0-36-meses.md          IV Plan de implementación (10 secciones + 100 KPIs)
│   └── comision-carmen-navas-verdad-memoria.md    IV.K CEV-CN — Verdad, Memoria y Reparación
│
├── articulado/
│   └── texto-articulado-clausula-continuidad.md   V Texto articulado + 17 Títulos + Arts. 121-184
│
├── documento/
│   └── documento-final-v0.1.md                    Documento compilatorio único (833 líneas, publicable)
│
├── referencias/                                   ← Documentos históricos consolidados (v0)
│   ├── marco-comparativo-milei-singapur.md        Doc. 2: Milei + Singapur + CRBV
│   └── propuesta-reforma.md                       Doc. 3: Propuesta por dimensión
│
└── docs/
    └── memoria-proyecto.md                        Bitácora técnica del proyecto (KB, decisiones, ingestas)
```

---

## Mapa de lectura rápida

| Si querés... | Empezá por |
|---|---|
| Entender qué es Aceptas en 5 minutos | [`prologo/resumen-ejecutivo.md`](prologo/resumen-ejecutivo.md) |
| Ver el diagnóstico completo del Estado venezolano actual | [`diagnostico/diagnostico-integral.md`](diagnostico/diagnostico-integral.md) |
| Conocer los principios rectores del proyecto | [`principios/principios-generales.md`](principios/principios-generales.md) |
| Leer un pilar específico | [`pilares/`](pilares/) |
| Ver el plan de ejecución 0–36 meses | [`implementacion/plan-implementacion-0-36-meses.md`](implementacion/plan-implementacion-0-36-meses.md) |
| Leer la Comisión Carmen Navas (verdad + memoria + reparación) | [`implementacion/comision-carmen-navas-verdad-memoria.md`](implementacion/comision-carmen-navas-verdad-memoria.md) |
| Consultar el texto articulado del proyecto de ley | [`articulado/texto-articulado-clausula-continuidad.md`](articulado/texto-articulado-clausula-continuidad.md) |
| Leer el documento final compilatorio | [`documento/documento-final-v0.1.md`](documento/documento-final-v0.1.md) |
| Auditar el marco comparativo internacional | [`referencias/marco-comparativo-milei-singapur.md`](referencias/marco-comparativo-milei-singapur.md) |
| Revisar la bitácora técnica del proyecto | [`docs/memoria-proyecto.md`](docs/memoria-proyecto.md) |

---

## 8 Pilares — Resumen ejecutivo

### III.1 Servicio Civil Meritocrático
Concurso público obligatorio para todo cargo directivo del Estado. **CNSC** (Comisión Nacional del Servicio Civil) independiente con 9 miembros designados por jurado mixto. Carrera profesional con VePass-Firma obligatoria. Salarios indexados USD 500–7.000 (ratio 14:1 alineado con Organización para la Cooperación y el Desarrollo Económicos (OCDE)).

### III.2 Seguridad Ciudadana y Restauración del Orden Público
**CPNP** civil (Cuerpo de Policía Nacional Profesional) + CICPC + JNEM. VePass-Firma obligatoria en todos los actos. Reconversión (no derogación) de PNB + policías estadales + municipales. Rechazo explícito al modelo Bukele: estado de excepción indefinido, militarización y opacidad presupuestaria están prohibidos. Cifras OVV 2023: 26,8 muertes violentas / 100K habitantes.

### III.3 MIED-LAM Constitucional
Ministerio del Desarrollo de la Inteligencia, Educación y Deporte Dr. Luis Alberto Machado. Constitucionalización de los programas del MEDI 1979-1984 que fueron desmontados por Lusinchi. Rango constitucional vía art. 237 CRBV. Educación cognitiva prenatal–preescolar + escolar + deportiva como política de Estado continua.

### III.4 Reforma Fiscal y Financiamiento Territorial
**Cronograma monetario 18 meses**: mes 1 apertura de banda cambiaria (±15%), mes 3-6 sanción Ley Orgánica del Banco Central de Venezuela (LOBCV), mes 12 autonomía plena BCV + crawling-peg ≤2%, mes 12-15 acumulación de reservas, **mes 18 dolarización oficial** (modelo Panamá 1904). Reforma tributaria no petrolera. Situado Constitucional Municipal 25%.

### III.5 Reforma Económica y Productiva
**Petróleos de Venezuela S.A. (PDVSA) matriz** 51% estatal / 49% privado vía Oferta Pública Inicial (OPI) (NYSE/LSE/BVC). Filiales mixtas cotizan en bolsa. **Ley Orgánica del Régimen de Adquisición Forzosa de Acciones de Empresas Estratégicas (LORAFEE)** con cláusula *pay-before-take* 90 días + reversión automática + golden share sellada. Privatización 100% de Corpoelec + Compañía Anónima Nacional Teléfonos de Venezuela (CANTV) + 9 hidrológicas regionales con régimen 20 años exoneración → solo IVA en año 21. **FOSEIP** (modelo Noruega/GPFG) + **Fondo Nacional de Inversión Productiva (FNIP)** con banca de desarrollo sectorial.

### III.6 Justicia Independiente y Anticorrupción
**Tribunal Supremo de Justicia (TSJ) meritocrático** (jueces por concurso público + Asamblea Nacional (AN) 3/5, 9 años no reelegibles). **Dirección Nacional Anticorrupción y Recuperación de Bienes (DNA-RB)** investigación penal especializada anticorrupción (modelo Corrupt Practices Investigation Bureau (CPIB) Singapur). **Defensor del Pueblo** independiente. **Ministerio Público unificado** (6 años único no reelegible). Investigación activa del Corte Penal Internacional (CPI) caso Venezuela I. Cooperación Organización Internacional de Policía Criminal (INTERPOL) + GAFI.

### III.7 Gobierno Digital, Identidad y Soberanía de Datos
**BND** (Banco Nacional de Datos) arquitectura federada tipo X-Road estonio con 11 bases sectoriales. **Clave Única de Identidad Digital (VePass)** 4 niveles (Lite, Plus, Fuerte, Firma) + **Cédula con Rol Único Tributario (Cédula-RUT)** con chip biométrico + NFC + QR. **Sistema Nacional de Identidad (SNI)** con captura hospitalaria 24h post-nacimiento (ADN + huellas plantares). **RUI** (Registro Único de Inmuebles, modelo Conservador chileno + e-Land Register estonio). **RUP** (Registro Único Vehicular). Trampa genética anti-robo de niños + CDF (Certificado de Defunción Fetal).

### III.8 Planificación Estratégica y Prospectiva
**Dirección Nacional de Planificación Estratégica y Prospectiva (DNPEP)** con rango constitucional. **Plan Quinquenal vinculante** aprobado por mayoría absoluta de la AN; toda inversión ≥ USD 50M debe estar explícitamente en él. **Presupuesto Plurianual 3 años** anclado al art. 314 CRBV. **UPE** (Unidad de Prospectiva Estratégica) modelo Singapur CSF. Cláusula expresa de **no injerencia de las Fuerza Armada Nacional (FAN)** en prospectiva civil.

---

## Innovaciones arquitectónicas

1. **Cláusula de continuidad transversal** (3/4 AN + referéndum ratificatorio en 90 días) aplicable a 16 materias estructurales encadenadas. El poder constituyente derivado **NO puede abolir garantía fundamental** sin cumplir el procedimiento. Límite absoluto.

2. **Veeduría Internacional Permanente**: panel mixto Oficina del Alto Comisionado de las Naciones Unidas para los Derechos Humanos (OACNUDH) + CIDH + ACNUR + Agencia Europea de la Guardia de Fronteras y Costas (FRONTEX) UE durante 8 años con poder de investigación en CPNP, CICPC, JNEM, DNPEP.

3. **VePass-Firma obligatoria** en todos los actos del CPNP, CICPC, JNEM, DNA-RB, DNPEP, CNSC, CPNP — "vigilancia sobre la vigilancia".

4. **LORAFEE pay-before-take 90 días**: el Estado NO toma el control de las acciones hasta haber pagado el 100%. Reversión automática si el Estado incumple. La garantía más fuerte contra la expropiación indirecta.

5. **Régimen RTER** (3 exámenes rigurosos consecutivos con reexaminación periódica) — sin asumir presunción de idoneidad sobre los cuerpos preexistentes.

6. **CEV-CN Carmen Navas**: mecanismo ejecutivo de revisión de expedientes + lista nominada vinculante al Ejecutivo con plazos de 60 días + habeas corpus colectivo si incumplimiento.

7. **Plan Quinquenal vinculante** + Presupuesto Plurianual 3 años + rating anual A–D público de planes/programas.

8. **Trazabilidad fetal que cierra el fraude**: el BND retiene 75 años el ADN de todo óbito fetal. Ningún nacido vivo puede coincidir con ese perfil sin orden judicial previa — y el intento fraudulento deja huella indeleble.

---

## Versión y estado

- **Versión actual**: v0.1 — 2026-07-16
- **Cobertura**: 8 pilares, Plan IV, Comisión Carmen Navas IV-K, Sección V Cláusula de Continuidad, Documento Final Compilatorio
- **Total texto**: ~580 KB, ~42.940 palabras en borradores
- **Knowledge Base**: 18.718 chunks indexados (Qdrant `kb_gobierno`)
- **KB stack**: Qdrant 1.18.2 + `intfloat/multilingual-e5-small` (384 dim, cosine)

## Hitos del proyecto (Plan 2026-07-15)

| Hito | Entregable | Cerrado |
|---|---|---|
| H1 | Renumeración + extracción + limpieza KB | 2026-07-15 ✅ |
| H2 | Pilar III.2 Seguridad ciudadana | 2026-07-16 ✅ |
| H3 | Pilar III.5 Reforma económica | 2026-07-16 ✅ |
| H4 | Pilar III.8 Planificación estratégica | 2026-07-16 ✅ |
| H5 | Separación Prólogo+Diagnóstico+Principios | 2026-07-16 ✅ |
| H6 | Plan de Implementación + Comisión Carmen Navas | 2026-07-16 ✅ |
| H7 | Sección V Cláusula de Continuidad | 2026-07-16 ✅ |
| H8 | Documento Final Compilatorio v0.1 | 2026-07-16 ✅ |
| H9 | Reingesta del documento final en KB | 2026-07-16 ✅ |

---

## Cómo citar

```
Aceptas — Reforma Integral del Estado Venezolano (v0.1).
Repositorio público: https://github.com/LeandroLCD/aceptas-reforma-estado-venezolano
Cerrado el 16 de julio de 2026.
```

## Licencia

Este repositorio se distribuye bajo **Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)**. Ver [`LICENSE`](LICENSE).

El proyecto Aceptas es una **propuesta técnica abierta**. Puede ser usado, modificado y distribuido libremente, incluso para fines comerciales, siempre que se mantenga la atribución y se comparta bajo la misma licencia.

## Contribuciones

Aceptas es una obra abierta. Pull requests bienvenidos. Para cambios sustantivos, abrí primero un *issue* con la propuesta.

## Contacto y comunidad

| Canal | Identificador |
|---|---|
| **X (Twitter)** | [@aceptas_ve](https://x.com/aceptas_ve) |
| **Email** | aceptas.ve@gmail.com |

Las cuentas de Instagram, TikTok y Facebook están en planificación — ver [`docs/memoria-proyecto.md`](docs/memoria-proyecto.md) sección "Plan de redes sociales" para más detalle.

**Firma del proyecto:**

> *"Si aceptas, levanta la mano y grita: '¡Lo juro!' / '¡Lo juro!' / ¡Más duro! / '¡Lo juro!' los angelitos no son bienvenidos a este colectivo."*

---

## Glosario de siglas

| Sigla | Nombre completo |
|---|---|
| **ACNUR** | Alto Comisionado de las Naciones Unidas para los Refugiados |
| **AN** | Asamblea Nacional |
| **BCV** | Banco Central de Venezuela |
| **BND** | Banco Nacional de Datos |
| **CANTV** | Compañía Anónima Nacional Teléfonos de Venezuela |
| **CDF** | Certificado de Defunción Fetal |
| **CICPC** | Cuerpo de Investigaciones Científicas, Penales y Criminalísticas |
| **CIDH** | Comisión Interamericana de Derechos Humanos |
| **CNSC** | Comisión Nacional del Servicio Civil |
| **CPI** | Corte Penal Internacional |
| **CPIB** | Corrupt Practices Investigation Bureau |
| **CPNP** | Cuerpo de Policía Nacional Profesional |
| **CRBV** | Constitución de la República Bolivariana de Venezuela |
| **Cédula-RUT** | Cédula con Rol Único Tributario |
| **DNA-RB** | Dirección Nacional Anticorrupción y Recuperación de Bienes |
| **DNPEP** | Dirección Nacional de Planificación Estratégica y Prospectiva |
| **FAN** | Fuerza Armada Nacional |
| **FNIP** | Fondo Nacional de Inversión Productiva |
| **FOSEIP** | Fondo Soberano de Estabilización e Inversión Productiva |
| **FRONTEX** | Agencia Europea de la Guardia de Fronteras y Costas |
| **GAFI** | Grupo de Acción Financiera Internacional |
| **INTERPOL** | Organización Internacional de Policía Criminal |
| **JNEM** | Junta Nacional de Evaluación Médica |
| **LOBCV** | Ley Orgánica del Banco Central de Venezuela |
| **LORAFEE** | Ley Orgánica del Régimen de Adquisición Forzosa de Acciones de Empresas Estratégicas |
| **MEDI** | Ministerio del Desarrollo de la Inteligencia |
| **MIED-LAM** | Ministerio del Desarrollo de la Inteligencia, Educación y Deporte Dr. Luis Alberto Machado |
| **OACNUDH** | Oficina del Alto Comisionado de las Naciones Unidas para los Derechos Humanos |
| **OCDE** | Organización para la Cooperación y el Desarrollo Económicos |
| **OPI** | Oferta Pública Inicial |
| **PDVSA** | Petróleos de Venezuela S.A. |
| **RTER** | Régimen de Tres Exámenes Rigurosos |
| **RUI** | Registro Único de Inmuebles |
| **RUP** | Registro Único de Profesionales |
| **SNI** | Sistema Nacional de Identidad |
| **TSJ** | Tribunal Supremo de Justicia |
| **VePass** | Clave Única de Identidad Digital |

