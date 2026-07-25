# Documento 3
## Propuesta de Reforma del Estado venezolano por dimensión

**Proyecto:** Reforma del Estado venezolano — Modelo shock + Singapur (versión 12 meses)
**Autor:** Equipo de reforma
**Fecha:** Julio 2026
**Fuentes:** Diagnóstico (Doc. 1, `docs/diagnostico.md`), Marco comparativo (Doc. 2, `docs/marco_comparativo.md`), Constitución de la República Bolivariana de Venezuela (CRBV) 1999, LOAP 2014, LOPPM 2009, Ley Orgánica de Planificación Pública (LOPP) 2014, Ley Orgánica de la Administración Financiera del Sector Público (LOAFSP), Código Orgánico Tributario (COT) 2014, Ley Orgánica de Hidrocarburos (LOH) reforma 2026, Ley Orgánica de Minas (LOM) 2026, DNU 70/2023 y Ley Bases 27.742 (Argentina), modelo Singapur (Lee Kuan Yew, Temasek, GIC), base de conocimiento `kb_gobierno` (Qdrant local).

---

## Resumen ejecutivo

El presente documento concreta la propuesta de reforma del Estado venezolano organizada en **ocho dimensiones** correspondientes al diagnóstico del Doc. 1. La arquitectura de la reforma se rige por los **diez principios consolidados** en la bitácora del proyecto (`~/qdrant-kb/memory.md`):

1. Alcance: shock estilo Milei, ejecutado en **12 meses**, sin red universal de protección.
2. Empresas del Estado: holding profesionalizado. **Petróleos de Venezuela S.A. (PDVSA) matriz 51% estatal + 49% privado (Oferta Pública Inicial (OPI) + estratégica)**; filiales mixtas cotizan en bolsa; Corpoelec y Compañía Anónima Nacional Teléfonos de Venezuela (CANTV) **privatizadas al 100%**.
3. Sectores protegidos del ajuste: **salud, educación y pensiones no contributivas** (no se tocan planta ni presupuesto).
4. Reforma del Art. 303: por **reinterpretación auténtica** o **enmienda constitucional mínima** que sustituya "totalidad" por "al menos el 51%"; el resto de la reforma opera con **leyes orgánicas vigentes** (LOAP, LOPPM, LOPP, COT, LOAFSP, etc.).
5. Función pública: **motosierra -30% en 12 meses** con retiros voluntarios incentivados.
6. Electricidad: **exoneración tributaria total por 20 años**, luego solo IVA.
7. Adquisición forzosa de acciones: regulada por ley orgánica, tope absoluto 51%, **cláusula *pay-before-take*** con pago previo del 100% y reversión automática a los 90 días.
8. Libertad bilateral de terminación laboral (principio 10 del rumbo).
9. Mochila austríaca 8,33% + seguro cesantía 1,2% (fórmula /6, máximo 6 meses).
10. Cronograma: **un solo paquete legislativo integrado** (no tres paquetes escalonados), aprobado en los primeros 90 días y con implementación gradual por dimensión entre los meses 4 y 12.

La presente versión descarta la propuesta anterior de tres paquetes legislativos en 36 meses y adopta el **cronograma único de 12 meses** estilo DNU 70-2023, con un Decreto Legislativo de rango orgánico inicial que active las reformas críticas y leyes orgánicas complementarias dictadas en los primeros seis meses.

---

## 1. Dimensión constitucional

### 1.1. Objetivo de reforma
Restringir el hiperpresidencialismo, restablecer la supremacía constitucional efectiva y abrir la puerta a la reinterpretación del Art. 303 sin necesidad de Asamblea Constituyente.

### 1.2. Acciones concretas (shock)
1. **Tope a las leyes habilitantes**: se prohíbe la concesión de leyes habilitantes durante los primeros 24 meses del período constitucional; a partir de allí, solo una ley habilitante por período legislativo, con plazo máximo de 12 meses y materias taxativas.
2. **Cláusula de evaluación ex post obligatoria**: toda ley con más de 5 años de vigencia debe ser evaluada por la **Superintendencia Nacional de Evaluación de Políticas Públicas** (creada en dimensión 6) en un plazo máximo de 18 meses; el informe se publica y es vinculante para el inicio de su reforma o derogatoria.
3. **Reinterpretación auténtica del Art. 303 CRBV**: el Tribunal Supremo de Justicia (TSJ) meritocrático (ver dimensión 4) emite, en sala constitucional, una **sentencia interpretativa** que sustituye "totalidad" por "al menos el cincuenta y uno por ciento (51%)" de las acciones ordinarias con derecho a voto de PDVSA matriz. La sentencia se publica en Gaceta Oficial con carácter vinculante *erga omnes*.
4. **Enmienda constitucional de blindaje**: si la sentencia interpretativa es considerada insuficiente, se promueve una **enmienda constitucional puntual** (Art. 341 CRBV, referendum aprobatorio) que sustituya la frase del Art. 303 y habilite expresamente la cotización bursátil de filiales mixtas.

### 1.3. Instrumentos legales
- **DNU inicial (mes 0)**: declara la reinterpretación del Art. 303 con base en el principio de supremacía constitucional y la cláusula de progreso (Art. 3 CRBV).
- **Sentencia interpretativa del TSJ (mes 1-2)**: 5 magistrados de la sala constitucional (nuevos, meritocráticos).
- **Ley Orgánica de Evaluación de Políticas Públicas (mes 3-6)**: crea la Superintendencia.
- **Ley Orgánica de Habilitantes (mes 6-9)**: sustituye el régimen vigente, fija topes y materias taxativas.

### 1.4. Cronograma (12 meses)
- Mes 0: DNU reinterpretación Art. 303.
- Mes 1-2: Sentencia interpretativa TSJ.
- Mes 3-6: Ley Orgánica de Evaluación.
- Mes 6-9: Ley Orgánica de Habilitantes.
- Mes 9-12: Evaluación prospectiva de las 30 leyes orgánicas vigentes, identificación de derogatorias.

### 1.5. Métricas de éxito
- 0 leyes habilitantes concedidas en los primeros 24 meses.
- 100% de las leyes orgánicas con >5 años evaluadas en 18 meses.
- Sentencia interpretativa del Art. 303 vigente y aplicada en la OPI de PDVSA matriz.

### 1.6. Costo fiscal estimado
- Costo directo: USD 5-10 millones (consultorías, evaluaciones, logística electoral para eventual enmienda).
- Ahorro indirecto: eliminación de discrecionalidad ejecutiva; reducción estimada del 15% en gasto corriente por derogación de leyes inerciales.

---

## 2. Dimensión administrativa

### 2.1. Objetivo de reforma
Reducir la hipertrofia administrativa de **40 ministerios + 200 entes adscritos** a un esquema profesional, jerarquizado y operable, alineado con el principio de subsidiariedad (Art. 165 CRBV).

### 2.2. Acciones concretas (shock)
1. **Reorganización ministerial inmediata (mes 0-3)**: de 35 cargos ministeriales vigentes a **9 ministerios** del Estado reformado (catálogo definitivo 25-jul-2026, ver Anexo A.5):
   - **Ministerio del Interior y Seguridad** (Pilar III.2: CPNP+CICPC+JNEM+Régimen Penitenciario+Pueblos Indígenas+Fronteras)
   - **Ministerio del Desarrollo de la Inteligencia, Educación y Deporte Dr. Luis Alberto Machado** (MIED-LAM, Pilar III.3, rango constitucional Art. 237 CRBV)
   - **Ministerio de Economía y Finanzas** (Pilar III.4: LOBCV+tributario+cronograma monetario 18m+fusión Industria+Comercio+Agricultura+Pesca+Alimentación)
   - **Ministerio de Energía y Minas** (Pilar III.5: PDVSA matriz 51%+privatizaciones mineras, excluye Defensa que sale del Ejecutivo)
   - **Ministerio de Infraestructura y Servicios** (Sector aguas privatizadas+Transporte+Obras+Hábitat+Vivienda)
   - **Ministerio de Planificación Estratégica y Prospectiva** (Pilar III.8: DNPEP+Plan Quinquenal vinculante)
   - **Ministerio de Gobierno Digital** (Pilar III.7: BND+VePass+Cédula-RUT+SNI+SPDP+ **absorción de Registros, Notariado y Registro Civil** del ex-MPP Justicia)
   - **Ministerio de Relaciones Exteriores** (Diplomacia activa+Veeduría Internacional Permanente 8 años+Cooperación Jurídica Internacional absorbida del ex-MPP Justicia)
   - **Ministerio del Ambiente** (Política ambiental+INPARQUES+IGVSB+Fundambiente+INAMEH, separado de Energía y Minas)

   **Fuera del catálogo ministerial pero dentro del Poder Ejecutivo**: **Consejo Nacional de Defensa**, ente dependiente directo de la Presidencia (reforma Arts. 332-333 CRBV; absorbe FAN+GNB+DGCIM).

   **Fuera del Ejecutivo (Poder Ciudadano ampliado, Reforma Art. 273 CRBV)**: CGR · Defensor del Pueblo · Ministerio Público · **CNSC ⭐ Servicio Civil** · DNA-RB. El Servicio Civil y la Función Pública se adscriben al Poder Ciudadano para blindarlos contra la motosierra sucesoria.
2. **Supresión de entes adscritos**: fusión o liquidación del **80% de los 200+ entes** (institutos autónomos, fundaciones, empresas del Estado no estratégicas, servicios desconcentrados redundantes). Los restantes 40 se reorganizan en torno a los 9 ministerios (4-5 entes por ministerio).
3. **Catálogo único de competencias**: en los primeros 6 meses se dicta el **Reglamento Orgánico del Poder Ejecutivo Nacional** (Art. 238 CRBV) con catálogo taxativo de competencias por ministerio, sin duplicidades.
4. **Reforma de la LOAP**: nueva LOAP (mes 6-9) que reemplaza la de 2014; consagra: (a) tope de 9 ministerios, (b) tope de 50 entes adscritos, (c) catálogo de competencias como anexo con rango legal.
5. **Reorganización ministerial en 60 días**: cronograma ejecutivo con 4 hitos quincenales; los ministerios suprimidos transfieren personal, competencias y presupuesto a los ministerios receptores.

### 2.3. Instrumentos legales
- **DNU de reorganización ministerial (mes 0)**: con fuerza de ley orgánica por emergencia administrativa (Art. 236 numeral 8 CRBV + habilitación expresa de la nueva Ley Orgánica de Habilitantes).
- **Nueva LOAP (mes 6-9)**: dictada por la Asamblea Nacional.
- **Decretos de supresión de entes (mes 0-6)**: 160 decretos individualizados.

### 2.4. Cronograma (12 meses)
- Mes 0: DNU reorganización.
- Mes 0-3: Liquidación de ministerios suprimidos.
- Mes 0-6: Supresión del 80% de entes adscritos.
- Mes 6-9: Nueva LOAP.
- Mes 9-12: Implementación plena.

### 2.5. Métricas de éxito
- Reducción de ministerios de 40 → 9 (77,5%).
- Reducción de entes adscritos de 200+ → ≤40 (80%).
- Reducción del gasto corriente administrativo en 35%.
- Plazo medio de resolución de trámites administrativos: -50%.

### 2.6. Costo fiscal estimado
- **Ahorro directo**: USD 1.200-1.800 millones/año por supresión de ministerios, entes y nóminas paralelas (cálculo con base en gasto corriente público no financiero estimado).
- **Costo de transición**: USD 80-120 millones (liquidación de entes, indemnizaciones, mudanzas, sistemas).

---

## 3. Dimensión fiscal

### 3.1. Objetivo de reforma
Recuperar la solvencia fiscal mediante tres medidas de choque simultáneas: (a) restructuración de PDVSA, (b) reforma tributaria anti-inflacionaria, (c) eliminación del control cambiario en 12 meses.

### 3.2. Acciones concretas (shock)
1. **OPI del 49% de PDVSA matriz (mes 3-9)**:
   - Banco de inversión internacional (Goldman Sachs, JP Morgan, Lazard) coordina OPI primaria en NYSE + LSE.
   - Colocación estratégica del 15% adicional a un socio industrial (modelo Petrobras-ENI) con *golden share* del Estado venezolano.
   - Recaudación esperada: **USD 8.000-15.000 millones** (a precio de mercado secundario ajustado al riesgo).
2. **Recompra estatal hasta 51% con justificación técnica y aprobación judicial** (Ley Orgánica del Régimen de Adquisición Forzosa de Acciones de Empresas Estratégicas (LORAFEE), ver dimensión 4): si la participación privada supera el 49%, el Estado activa el mecanismo de la ley.
3. **Reforma tributaria integral (mes 0-6)**:
   - Unificación de alícuotas de IVA en 16% general + 8% reducido (alimentos, medicinas, servicios educativos).
   - Reducción de ISLR a 25% para empresas, 15% para PYMEs.
   - Eliminación del IGTF para transacciones en moneda extranjera (preparación del levantamiento del cepo).
   - Eliminación de las exoneraciones discrecionales (más de 100 vigentes); solo permanecen las del Art. 64 COT autorizadas por ley orgánica.
4. **Eliminación del control cambiario y transición a la dolarización — cronograma 18 meses (en paralelo al shock de 12 meses)**:
   - Mes 1: apertura de la banda cambiaria (unificación de cotizaciones, ancho inicial ±15%, Decreto Banco Central de Venezuela (BCV)).
   - Mes 1-6: eliminación del recargo del 25% en operaciones en divisas; eliminación del IGTF en transacciones USD; permiso universal de mantener, transar y depositar en divisas (modelo Panamá/Ecuador con marco anti-lavado estricto).
   - Mes 3-6: sanción de la nueva **Ley Orgánica del BCV (LOBCV)**: autonomía, prohibición de financiamiento monetario, directorio de 7 miembros con cláusula de no remoción.
   - Mes 6-12: flotación administrada con revisión trimestral del ancho de banda; meta de inflación anual <30%; meta de reservas BCV USD 15.000-20.000 M (capitalizadas con OPI PDVSA 49% + 30% ingresos petroleros al Fondo de Estabilización Macroeconómica (FEM)).
   - Mes 12: hito de **autonomía plena del BCV**; meta de inflación publicada; adopción de *crawling-peg* explícito (devaluación mensual ≤2%) para anclar expectativas.
   - Mes 12-15: período de **convergencia**; acumulación de reservas hasta umbral de dolarización (≥6 meses de importaciones ≈ USD 8.000-12.000 M adicionales); sanción de la **Ley de Dolarización** (tipo de cambio fijo irrevocable a la paridad vigente al momento del cambio, redenominación de contratos a esa paridad).
   - Mes 15-18: período de **transición**; USD se declara moneda de curso legal; el bolívar se mantiene como uso opcional y unidad de cuenta subsidiaria por 12 meses adicionales.
   - Mes 18: **dolarización oficial**; el BCV deja de emitir bolívar para transacciones y opera como cámara de compensación de reservas en USD; el bolívar se redenomina como **moneda simbólica** (modelo Panamá 1904: solo monedas fraccionarias y registro contable, sin curso legal forzoso).
   - **Cláusula constitucional de blindaje**: reforma del Art. 318 CRBV con exigencia de 3/5 Asamblea Nacional (AN) + referéndum 90 días para cualquier reversión.
   - **Prohibición de financiamiento monetario del déficit** (inspirada en Art. 123 Constitución ecuatoriana 2008 y Ley 27.514 Argentina).

### 3.3. Instrumentos legales (combinación shock 12 meses + plan monetario paralelo 18 meses)
- **DNU inicial (mes 0)**: declara la emergencia económica, autoriza la OPI, suspende el control cambiario por 18 meses para iniciar la transición monetaria.
- **Decreto del BCV de apertura de banda cambiaria (mes 1)**: emitido por el BCV en coordinación con el Ministerio de Economía; fija el centro técnico y el ancho inicial (±15%) de la banda de flotación administrada.
- **Nueva Ley Orgánica de Hidrocarburos (mes 0-3)**: refunde la reforma LOH 2026, incluye el tope 51% para filiales mixtas.
- **Nueva Ley Orgánica del COT (mes 3-6)**: simplifica la estructura tributaria, consagra IVA único + 2 alícuotas, deroga más de 30 leyes tributarias dispersas.
- **Nueva Ley Orgánica del Banco Central de Venezuela — LOBCV (mes 3-6)**: consagra el mandato de estabilidad de precios, la prohibición de financiamiento monetario del déficit, la autonomía patrimonial y de gestión del BCV, y un directorio de siete (7) miembros con cláusula de no remoción. Reemplaza el régimen vigente del BCV.
- **Ley del Fondo de Estabilización Macroeconómica (mes 6-9)**: crea el FEM, define su gobernanza (directorio independiente, 5 miembros: 2 del Estado, 3 independientes con expertise en política monetaria).
- **Ley de Dolarización (mes 12-15)**: fija el tipo de cambio irrevocable a la paridad vigente al momento del cambio; redenomina los contratos en bolívar a USD a esa paridad.
- **Reforma constitucional del Art. 318 CRBV (mes 12-15)**: cláusula de blindaje del régimen monetario (USD curso legal, bolívar moneda simbólica, reversión por 3/5 AN + referéndum 90 días). Se ejecuta por la vía de enmienda constitucional (Art. 341 CRBV) o por reinterpretación auténtica del TSJ meritocrático.

### 3.4. Cronograma (shock 12 meses + plan monetario 18 meses en paralelo)
- Mes 0: DNU emergencia + decreto OPI + reorganización administrativa (paquete shock).
- Mes 1: Decreto del BCV de apertura de banda cambiaria.
- Mes 0-3: Nueva LOH + preparación OPI.
- Mes 1-6: Eliminación del recargo 25% + eliminación IGTF en USD + permiso universal de tenencia en divisas.
- Mes 3-6: Reforma COT + sanción LOBCV (autonomía BCV).
- Mes 3-9: OPI ejecutada (USD 10.000-15.000 M al FEM + capitalización reservas).
- Mes 6-9: Ley del FEM operativa + flotación administrada con revisión trimestral de banda.
- Mes 6-12: Levantamiento gradual del cepo (Plan A shock) en paralelo a la flotación administrada (Plan B monetario); ambos terminan convergiendo en libre tenencia de divisas.
- Mes 12: Hito de autonomía plena del BCV + adopción de *crawling-peg* explícito (≤2% mensual).
- Mes 12-15: Convergencia + acumulación de reservas hasta umbral de dolarización + sanción de la Ley de Dolarización + reforma Art. 318 CRBV.
- Mes 15-18: Período de transición; el USD se declara moneda de curso legal; bolívar de uso opcional.
- Mes 18: Dolarización oficial; BCV opera como cámara de compensación de reservas en USD; bolívar moneda simbólica (modelo Panamá).

### 3.5. Métricas de éxito
- Recaudación OPI: USD 8.000-15.000 millones (cierre año 1).
- Recaudación tributaria no petrolera/PIB: del 5% al 15% en 24 meses.
- Reservas internacionales BCV: USD 15.000-20.000 M al cierre del año 1; USD 25.000-30.000 M al cierre del año 2 (umbral de dolarización).
- Inflación anual: <30% al cierre del año 1; <10% al cierre del año 2; <3% tras la dolarización.
- Tipo de cambio: una sola cotización oficial con brecha cero respecto al paralelo desde el mes 1.
- Hito mes 12: directorio independiente del BCV instalado + *crawling-peg* publicado.
- Hito mes 18: USD de curso legal + bolívar moneda simbólica (Ley de Dolarización vigente + reforma Art. 318 CRBV promulgada).

### 3.6. Costo fiscal estimado
- **Ingresos extraordinarios año 1**: USD 8.000-15.000 millones (OPI) + USD 3.000-5.000 millones (reforma tributaria).
- **Costos de transición**: USD 200-400 millones (banco de inversión, due diligence, equipos técnicos, transición cambiaria).
- **Saldo neto año 1**: +USD 11.000-19.000 millones.

### 3.7. Privatización del Servicio de Agua Potable y Saneamiento (2026-07-13)

**Contexto y diagnóstico**: el servicio de agua potable en Venezuela es prestado por **HIDROVEN** (matriz) y **9 hidrológicas filiales** (Hidrocapital, Hidrocentro, Hidrolago, Hidroandes, Hidrolara, Hidrocaribe, Hidropaez, Hidrosuroeste, Hidrollanos). La práctica ha demostrado colapso operativo: racionamiento >50% en zonas urbanas, agua no potable en >60% de la red, infraestructura obsoleta, financiamiento crónico del Estado.

**Objetivo**: aplicar al sector agua la **misma plantilla aplicada a electricidad** (Doc. 5 Art. 31-34): privatización 100% mediante **9 licitaciones regionales independientes** + exoneración tributaria 20 años + regulador independiente (Superintendencia Nacional de Aguas y Saneamiento (SUNAA)).

#### 3.7.1. Acciones concretas (shock)

1. **Mantener HIDROVEN matriz como holding técnico del Estado**: coordina política nacional, regulación técnica, planificación hidrológica; no se privatiza.
2. **Privatizar las 9 hidrológicas filiales** mediante licitaciones regionales independientes:
   - 9 procesos simultáneos, comenzando el mes 3 y cerrando entre los meses 9-12.
   - 100% del capital privado; ningún accionista podrá superar el 49% (para evitar monopolios verticales).
   - Pliego tipo OFGEM/UK con cláusulas de cobertura, calidad, tarifa social y penalizaciones.
3. **Régimen tributario idéntico al eléctrico**:
   - Exoneración total de ISLR, IGTF, impuestos municipales, tasas y contribuciones especiales durante 20 años.
   - A partir del año 21: solo IVA a la alícuota general.
4. **Crear SUNAA** (Superintendencia Nacional de Aguas y Saneamiento):
   - Ente autónomo con personalidad jurídica y patrimonio propio.
   - Director concursado por 6 años.
   - Modelo regulatorio OFGEM/UK.
5. **Servicio universal garantizado**: cada operador privado asume obligaciones de cobertura, calidad (cumple OMS) y tarifa social focalizada para hogares vulnerables.

#### 3.7.2. Hidrológicas regionales a privatizar (9)

| # | Filial | Cobertura geográfica |
|---|--------|---------------------|
| 1 | Hidrocapital | Caracas, Miranda, Vargas |
| 2 | Hidrocentro | Carabobo, Aragua, Cojedes |
| 3 | Hidrolago | Zulia, Trujillo, Mérida |
| 4 | Hidroandes | Táchira, Barinas, Portuguesa, Apure |
| 5 | Hidrolara | Lara, Yaracuy |
| 6 | Hidrocaribe | Anzoátegui, Sucre, Nueva Esparta, Monagas, Delta Amacuro |
| 7 | Hidropaez | Portuguesa |
| 8 | Hidrosuroeste | Táchira, Sur del Lago |
| 9 | Hidrollanos | Apure, Guárico, Barinas |

#### 3.7.3. Instrumentos legales

- **DNU inicial (mes 0)**: declara la emergencia del servicio de agua, autoriza las licitaciones.
- **Ley Orgánica del Régimen de Agua Potable y Saneamiento (mes 3-6)**: refunde la legislación vigente; crea la SUNAA; establece el régimen de licitaciones.
- **Decretos de licitación (mes 3)**: 9 pliegos simultáneos.

#### 3.7.4. Cronograma (12 meses)

- Mes 0: DNU emergencia del servicio de agua.
- Mes 3: Publicación de 9 pliegos de licitación regional.
- Mes 6: Ofertas recibidas.
- Mes 9-12: Adjudicación y firma de contratos con operadores privados.
- Mes 12-18: Transición operativa (transferencia de personal, bienes, infraestructura).

#### 3.7.5. Métricas de éxito

- 9 licitaciones adjudicadas con operadores privados.
- 100% de las hidrológicas regionales privatizadas en 18 meses.
- Cobertura de agua potable: del 60% al 90% en 36 meses.
- Calidad del agua (cumple OMS): del 30% al 95% en 36 meses.
- Racionamiento: del 50% al 10% en 24 meses.
- Satisfacción ciudadana con el servicio de agua: >70% en encuestas.

#### 3.7.6. Costo fiscal estimado

- **Ingresos por privatización**: USD 1.000-2.500 millones (9 regiones × USD 110-280 millones cada una).
- **Inversión privada comprometida**: USD 3.000-5.000 millones en 5 años (cobertura + calidad + tecnología).
- **Ahorro por fin del subsidio al agua**: USD 200-400 millones/año (actualmente el Estado subsidia la tarifa).
- **Costo de SUNAA**: USD 30-50 millones/año.
- **Costo de transición**: USD 50-100 millones (indemnizaciones, transferencias, sistemas).
- **Saldo neto año 1**: -USD 100-200 millones (transición + SUNAA).
- **Saldo neto año 2 en adelante**: +USD 300-700 millones/año (ingresos por privatización ya percibidos + ahorro del subsidio).
- **Beneficio sistémico**: fin del racionamiento, agua de calidad universal, atracción de inversión privada masiva en infraestructura hidráulica.

---

## 4. Dimensión justicia

### 4.1. Objetivo de reforma
Construir un Poder Judicial meritocrático, autónomo y financieramente digno, capaz de servir como contrapeso del Ejecutivo y como garante del debido proceso en la aplicación de las nuevas leyes (LORAFEE, reforma COT, LOAP, etc.).

### 4.2. Acciones concretas (shock)
1. **Renovación total del TSJ (mes 0-3)**:
   - La Asamblea Nacional cesa a los 32 magistrados actuales por vencimiento anticipado de período (precedente: Italia 1994 *Mani Pulite*).
   - Concurso público de antecedentes y oposición para 20 nuevas magistraturas (sala constitucional 5, sala político-administrativa 5, sala civil 5, sala penal 5).
   - Jurado independiente: 3 académicos, 3 abogados, 3 representantes de la sociedad civil, 1 delegado del Ejecutivo (sin voto).
2. **Escuela Nacional de la Judicatura (mes 3-9)**:
   - Creada por ley orgánica como ente autónomo con patrimonio propio.
   - Concurso de ingreso + formación de 12 meses + evaluación continua anual vinculante.
   - 1.500 plazas para jueces de primera instancia + 300 para jueces superiores en el primer año.
3. **Ejecución efectiva del 2% presupuestario (Art. 254 CRBV)**:
   - Transferencia automática no reprogramable desde el BCV al Fondo del Poder Judicial.
   - Auditoría externa anual de los fondos.
4. **LORAFEE (Ley Orgánica del Régimen de Adquisición Forzosa de Acciones de Empresas Estratégicas) (mes 3-6)**:
   - Regula la adquisición forzosa judicial con tope 51% + cláusula *pay-before-take* (mes 4).
   - 7 causales taxativas, procedimiento contradictorio, valoración independiente por banco de inversión internacional de terna propuesta por TSJ, indemnización en bonos a 10 años o efectivo del Tesoro (90 días), recurso de apelación sin efecto suspensivo, reversión automática si Estado no paga en 90 días.

### 4.3. Instrumentos legales
- **DNU de reorganización del TSJ (mes 0)**: declara la emergencia judicial, autoriza la renovación anticipada.
- **Ley Orgánica del Poder Judicial (mes 3-6)**: refunde la LOTSJ y la LOPPM judicial.
- **LORAFEE (mes 3-6)**: ley orgánica con el procedimiento completo.
- **Ley Orgánica de la Escuela Nacional de la Judicatura (mes 6-9)**: crea la escuela y su régimen autónomo.

### 4.4. Cronograma (12 meses)
- Mes 0: DNU reorganización TSJ.
- Mes 1-3: Concurso de nuevas magistraturas.
- Mes 3-6: Sentencia interpretativa Art. 303 (desde TSJ meritocrático).
- Mes 3-6: LORAFEE + Ley Orgánica del PJ.
- Mes 6-9: Escuela Nacional operativa.
- Mes 9-12: Primeras 1.500 plazas concursadas.

### 4.5. Métricas de éxito
- 100% de magistrados del TSJ designados por concurso.
- Causas atrasadas: -50% en 24 meses (objetivo).
- Duración media proceso civil: de 4-7 años a 18 meses en 36 meses (objetivo).
- Tasa de presos sin condena: del 50% al 25% en 24 meses (objetivo).
- Presupuesto ejecutado del PJ: ≥98% de la partida del 2%.

### 4.6. Costo fiscal estimado
- Costo de la transición judicial: USD 150-250 millones (indemnizaciones a magistrados cesados, concursos, infraestructura de la Escuela).
- Costo operativo incremental: USD 200-300 millones/año (salarios meritocráticos dignos, infraestructura).
- Ahorro sistémico: difícil de cuantificar en el corto plazo; valor presente del sistema judicial funcional estimado en 3-5% del PIB/año.

---

## 5. Dimensión digital

### 5.1. Objetivo de reforma
Cerrar la brecha digital, modernizar el Estado y sentar las bases para una economía digital; el detalle técnico está en el **Pilar III.7 (Borrador de reforma)** ya redactado.

### 5.2. Acciones concretas (shock)
1. **Ejecución del cronograma 7 años del Pilar III.7**, acelerado a **4 años** mediante shock:
   - **Fase 1 (mes 0-12)**: licitación del data center Guri-1, sanción de la LOPD, creación de la Superintendencia de Protección de Datos Personales (SPDP), lanzamiento del Clave Única de Identidad Digital (VePass) Lite (identidad digital temporal).
   - **Fase 2 (mes 12-24)**: Banco Nacional de Datos (BND) operativo con 4 bases federadas iniciales (Saime, Seniat, Consejo Nacional Electoral (CNE), Instituto Venezolano de los Seguros Sociales (IVSS)), Cédula con Rol Único Tributario (Cédula-RUT) emitida para 10 millones de venezolanos.
   - **Fase 3 (mes 24-36)**: BND con 11 bases federadas, Cédula-RUT para 25 millones.
   - **Fase 4 (mes 36-48)**: BND universal, 30 millones de Cédula-RUT emitidas.
2. **Privatización simultánea de CANTV (mes 0-6)** y Movilnet (mes 6-12):
   - Licitación pública internacional con pliego modelo OFGEM/UK.
   - Operador privado asume red + obligaciones de cobertura.
   - Estado retiene **CONATEL como regulador independiente**.

### 5.3. Instrumentos legales
- **DNU de privatización de CANTV (mes 0)**: autoriza la enajenación accionaria, fija pliego.
- **Ley Orgánica de Protección de Datos Personales (LOPD) (mes 3-6)**: crea la SPDP.
- **Ley Orgánica del Documento Nacional de Identidad Digital (mes 6-9)**: crea la Cédula-RUT.
- **Ley del Banco Nacional de Datos (BND) (mes 6-9)**: crea la arquitectura federada tipo X-Road.

### 5.4. Cronograma (12 meses)
- Mes 0: DNU privatización CANTV.
- Mes 0-12: Data center Guri-1 en construcción (Fase 1).
- Mes 3-6: LOPD.
- Mes 6-9: Ley BND + Ley Cédula-RUT.
- Mes 6-12: Licitación Movilnet.
- Mes 12: 10 millones de Cédula-RUT emitidas.

### 5.5. Métricas de éxito
- Penetración de banda ancha: del 50% al 75% en 24 meses.
- Velocidad media Internet fija: de <25 Mbps a 100 Mbps en 36 meses.
- 100% de trámites administrativos digitalizados en 24 meses.
- Cobertura 4G: del 60% al 90% del territorio en 36 meses.

### 5.6. Costo fiscal estimado
- **Ingresos por privatización**: USD 1.500-3.000 millones (CANTV + Movilnet).
- **Inversión pública del data center Guri-1**: USD 800-1.200 millones (asociación público-privada).
- **Inversión privada esperada**: USD 5.000-8.000 millones en 5 años (compromisos de cobertura).

---

## 6. Dimensión planificación

### 6.1. Objetivo de reforma
Convertir la planificación en una función estatal útil, con evaluación ex post vinculante y articulación multinivel.

### 6.2. Acciones concretas (shock)
1. **Superintendencia Nacional de Evaluación de Políticas Públicas (SNEEP) (mes 3-6)**:
   - Ente autónomo con personalidad jurídica y patrimonio propio.
   - Director designado por concurso de antecedentes (modelo BCRA/BCCh) por 6 años, no removable.
   - 200 profesionales: economistas, politólogos, estadísticos, abogados, cientistas de datos.
2. **Evaluación obligatoria de toda ley >5 años (vinculante)**:
   - La SNEEP evalúa el 100% de las leyes orgánicas vigentes en 18 meses.
   - Informe público + recomendación vinculante al Poder Legislativo: mantener, reformar o derogar.
3. **Reforma del INE (mes 0-12)**:
   - Director designado por concurso público + 6 años de mandato.
   - Consejo técnico asesor con 7 miembros: 2 del BCV, 2 de la academia, 2 de la sociedad civil, 1 de las universidades.
   - Publicación trimestral de indicadores macro y sociales.

### 6.3. Instrumentos legales
- **Ley Orgánica de la Superintendencia Nacional de Evaluación de Políticas Públicas (mes 3-6)**.
- **Ley Orgánica del Instituto Nacional de Estadística (mes 6-9)**: refunde la ley vigente.
- **Decreto de creación del Consejo Asesor del INE (mes 0)**.

### 6.4. Cronograma (12 meses)
- Mes 0: Decreto Consejo Asesor INE.
- Mes 0-3: Concurso director INE + SNEEP.
- Mes 3-6: Ley Orgánica SNEEP.
- Mes 6-9: Ley Orgánica INE.
- Mes 9-12: Primeras evaluaciones ex post de 10 leyes orgánicas.

### 6.5. Métricas de éxito
- 100% de leyes orgánicas con >5 años evaluadas en 18 meses.
- Rezago de indicadores del INE: de 2-4 años a 6 meses en 24 meses.
- 10 planes sectoriales reformulados en 12 meses con metas vinculantes.

### 6.6. Costo fiscal estimado
- Costo de creación SNEEP + reforma INE: USD 50-80 millones (primer año).
- Costo operativo anual: USD 30-50 millones.
- Ahorro por derogación de leyes inerciales: 10-15% del gasto corriente.

---

## 7. Dimensión descentralización

### 7.1. Objetivo de reforma
Operativizar el federalismo cooperativo del Art. 165 CRBV mediante subsidiariedad real y recursos automáticos.

### 7.2. Acciones concretas (shock)
1. **Leyes de bases en 18 meses (no 24)**:
   - Ley de Bases de Energía y Minas.
   - Ley de Bases de Transporte.
   - Ley de Bases de Ambiente y Recursos Naturales.
   - Ley de Bases de Agua Potable y Saneamiento.
   - Ley de Bases de Educación.
   - Ley de Bases de Salud.
2. **Transferencias automáticas (mes 0-3)**:
   - Situado Constitucional (Art. 167 CRBV) se transfiere mensualmente con fórmula automática del BCV.
   - Asignaciones especiales se reasignan al **Fondo de Compensación Interterritorial** (FCI) con criterios técnicos (población, pobreza, IDH).
3. **Reactivación del Consejo Federal de Gobierno (mes 0-3)**:
   - Reuniones trimestrales con voto vinculante.
   - Secretaría técnica operativa con 20 profesionales.
   - Resolución obligatoria de los conflictos de competencia entre niveles.

### 7.3. Instrumentos legales
- **DNU de transferencias automáticas (mes 0)**: modifica el cronograma de transferencias del Situado Constitucional.
- **Ley Orgánica del Fondo de Compensación Interterritorial (mes 3-6)**: crea el FCI con fórmula técnica.
- **6 Leyes de Bases (mes 3-18)**: dictadas en paquetes bimestrales.

### 7.4. Cronograma (12 meses)
- Mes 0: DNU transferencias automáticas.
- Mes 0-3: CFG reactivado.
- Mes 3-6: Ley FCI + 2 leyes de bases.
- Mes 6-12: 4 leyes de bases adicionales.

### 7.5. Métricas de éxito
- 6 leyes de bases dictadas en 18 meses.
- Ingresos propios subnacionales: del 5-8% al 20% del total nacional en 36 meses (objetivo).
- Reducción de la brecha de servicios públicos Caracas-interior: 50% en 36 meses (objetivo).

### 7.6. Costo fiscal estimado
- **Costo de las transferencias automáticas**: USD 800-1.200 millones/año adicionales.
- **Costo administrativo**: USD 20-30 millones/año (CFG + secretaría técnica).
- **Beneficio sistémico**: reducción de conflictos competenciales, mayor legitimidad democrática subnacional, presión competitiva sobre la gestión nacional.

### 7.7. Reforma de la LOPPM (2026-07-13): eliminación de parroquias y transferencia de competencias

**Contexto y diagnóstico**: la Ley Orgánica del Poder Público Municipal (LOPPM, 2009) diseñó un régimen municipal con tres niveles: municipio, parroquia y otras entidades locales (Arts. 30-37). La práctica ha demostrado dos problemas estructurales:

1. **Las parroquias como entidades redundantes**: las parroquias fueron creadas como entidades desconcentradas del municipio para promover la participación y desconcentrar la gestión. Sin embargo, sus funciones principales (registro civil, identificación, organización comunitaria) han sido capturadas por redes clientelares, con resultados opuestos a los previstos. Con la creación del Sistema Nacional de Identidad (SNI) y de la Cédula-RUT (Doc. 5, Título VII), las funciones de identificación se concentran en una sola base nacional federada. Las parroquias pierden su razón de ser operativa.

2. **Duplicación de funciones entre niveles**: la LOPPM y la legislación sectorial generan superposiciones entre municipio, estado y nación (ej.: registro civil en tres niveles, catastros paralelos, estadísticas duplicadas, servicios públicos fragmentados). El principio de subsidiariedad (Art. 165 CRBV) exige un catálogo taxativo de competencias por nivel.

**Objetivo de la reforma LOPPM**: simplificar el régimen municipal mediante la supresión de las parroquias como entidad local y la transferencia taxativa de competencias conforme al principio de subsidiariedad.

#### 7.7.1. Acciones concretas (shock)

1. **Supresión de las parroquias como entidad local (Arts. 30-37 LOPPM)**:
   - Se derogan los artículos que regulan las parroquias como entidad local desconcentrada.
   - Las actuales ~1.100 parroquias se suprimen como entidad administrativa; el territorio se integra al municipio.
   - Los bienes, servicios y personal de las juntas parroquiales se transfieren al municipio cabecera o al estado, según corresponda.
   - Las funciones de Registro Civil se concentran en el SNI federal (Cédula-RUT).
2. **Catálogo taxativo de competencias por nivel (Arts. 56-59 LOPPM)**:
   - Toda competencia se asigna expresamente a un solo nivel (nacional, estadal o municipal).
   - Cualquier materia no expresamente asignada al municipio queda en el ámbito nacional.
   - Se deroga la posibilidad de duplicar funciones por delegación.
3. **Incremento del Situado Constitucional Municipal**:
   - ElSituado Constitucional Municipal se incrementa del 20% al 25% de los ingresos ordinarios nacionales (Art. 170 CRBV permite la elevación por ley orgánica).
   - Las transferencias son automáticas, mensuales, no reprogramables.
4. **Fortalecimiento del municipio como célula básica**:
   - El municipio concentra todas las funciones locales: aseo urbano, agua, vialidad, catastro, permisos de construcción, registro civil (vía SNI), policía municipal.
   - Se elimina la posibilidad de que los estados dupliquen funciones municipales.

#### 7.7.2. Instrumentos legales

- **DNU inicial (mes 0)**: declara la emergencia municipal y autoriza la supresión de parroquias.
- **Nueva LOPPM (mes 3-6)**: refunde la LOPPM 2009 con la supresión de parroquias y el catálogo taxativo de competencias.
- **Ley Orgánica del Situado Constitucional Municipal (mes 6-9)**: eleva el porcentaje al 25% y consagra la automaticidad de las transferencias.
- **6 Leyes de Bases (mes 3-18)**: asignan taxativamente las competencias concurrentes.

#### 7.7.3. Cronograma (12 meses)

- Mes 0: DNU supresión de parroquias.
- Mes 0-3: Inventario de bienes, personal y deudas de las juntas parroquiales.
- Mes 3-6: Nueva LOPPM.
- Mes 3-9: Transferencia operativa de funciones al municipio o al estado.
- Mes 6-9: Ley del Situado Constitucional Municipal.
- Mes 9-12: Liquidación final de juntas parroquiales.

#### 7.7.4. Métricas de éxito

- 1.100 parroquias suprimidas como entidad local.
- 10.000 cargos electos y de designación parroquial eliminados.
- 100% de funciones locales transferidas al municipio o al estado sin duplicación.
- Ingresos propios municipales: del 5-8% al 25% del total nacional en 36 meses.
- Reducción de la brecha de servicios públicos Caracas-interior: 50% en 36 meses.

#### 7.7.5. Costo fiscal estimado

- **Ahorro por supresión de parroquias**: USD 50-100 millones/año (eliminación de nóminas parroquiales: alcalde, junta parroquial, personal administrativo, dietas).
- **Costo de transición**: USD 30-50 millones (liquidación, transferencia de personal, reasignación de bienes).
- **Saldo neto año 1**: +USD 20 millones (después de transición).
- **Saldo neto año 2 en adelante**: +USD 80 millones/año.
- **Beneficio sistémico**: simplificación del régimen municipal, eliminación de duplicaciones, mayor legitimidad democrática del municipio.

---

## 8. Dimensión función pública

### 8.1. Objetivo de reforma
Profesionalizar la función pública, reducir la planta en 30%, separar el IVSS contributivo del no contributivo y blindar los sectores protegidos (salud, educación, pensiones no contributivas).

### 8.2. Acciones concretas (shock)
1. **Motosierra del empleo público (mes 0-12)**:
   - Diagnóstico de planta en 30 días.
   - Retiro voluntario incentivado con **bono equivalente a 12 meses de salario** + acceso preferente a programas de capacitación.
   - Despidos del personal no elegible para retiro (personal de libre nombramiento y remoción que no supere evaluación de desempeño).
   - **Sectores protegidos excluidos**: personal de salud, educación y pensiones no contributivas (IVSS rama no contributiva) NO se toca.
2. **Registro Único Nacional de Personal del Estado (RUNPE) (mes 0-3)**:
   - Número único por funcionario.
   - Cruce de nóminas ministeriales + entes adscritos + gobernaciones + alcaldías + empresas del Estado + misiones + nómina especial.
   - Identificación de **~3,5 millones de empleados**; estimación de **1 millón de duplicidades**.
3. **Concurso público de ingreso obligatorio (mes 3-12)**:
   - Toda vacante en sectores no protegidos se cubre por concurso público de antecedentes y oposición en 18 meses.
   - Concursos nacionales unificados (Escuela Nacional de Administración Pública).
4. **Separación del IVSS (mes 6-12)**:
   - **Rama contributiva**: transición a cuentas individuales de capitalización administradas por AFJP privadas reguladas.
   - **Rama no contributiva**: pensión básica universal (PBU) financiada por Rentas Generales, **NO se toca su presupuesto**; cobertura universal para adultos mayores sin aportes suficientes.
5. **Libertad bilateral de terminación laboral (mes 0-3)**:
   - DNU + nueva Ley Orgánica del Trabajo derogan la inamovilidad laboral de la LOTTT.
   - Indemnización por despido sin causa: 1 mes por año trabajado (tope 12 meses).
   - Mochila austríaca 8,33% + seguro cesantía 1,2% (fórmula /6, máximo 6 meses) complementaria.

### 8.3. Escala salarial nacional del sector público (2026-07-13)

**Contexto y diagnóstico**: el salario mínimo actual del sector público venezolano es de aproximadamente **USD 1/mes**, lo que ha provocado la pérdida de todo atractivo de la función pública, migración masiva al sector informal (que ya supera el 50% del PIB), capturas clientelares por necesidad de subsistencia y deserción del personal calificado (médicos, profesores, ingenieros). Esta masa salarial de indigencia es la **causa-raíz** que sostiene el sistema de extorsión institucional descrito en el diagnóstico.

**Objetivo**: reescalar la pirámide salarial del sector público en USD de poder adquisitivo real, comprimir la distancia entre la base y la cúspide (de ratios >100x actuales a ratios ~14x), y hacer de la función pública una carrera profesional competitiva frente al sector privado y a la emigración.

#### 8.3.1. Escala propuesta

| Categoría | Salario mensual (USD) | Ratio vs mínimo |
|-----------|------------------------|------------------|
| **Salario mínimo nacional** (público y privado) | **500** | 1,0x (base) |
| **Profesores** (todos los niveles) | **1.200** | 2,4x |
| **Policías, bomberos, protección civil** | **1.200** | 2,4x |
| **Médicos generales / personal de salud no especialista** | **1.500** | 3,0x |
| **Médicos especialistas** | **3.000** | 6,0x |
| **Ministros, viceministros, diputados, jueces, fiscales, contralor, defensor** | **5.000** | 10,0x |
| **Presidente de la República** | **7.000** | 14,0x |

**Compresión de la pirámide**: la distancia entre el Presidente y el salario mínimo pasa de un ratio estimado >100:1 en la actualidad a **14:1**, alineado con los estándares de países Organización para la Cooperación y el Desarrollo Económicos (OCDE) comparables (Noruega ~12:1, Suecia ~13:1, Finlandia ~14:1). Esta compresión envía tres señales simultáneas:

1. **Servicio civil dignificado**: USD 500/mes es un salario que permite vida digna y saca al empleado público de la lógica de supervivencia-extorsión.
2. **Carrera meritocrática viable**: profesor/policía a USD 1.200 supera al salario mínimo privado y compite con la economía informal.
3. **Cúspide sobria**: USD 7.000 para el Presidente bloquea el enriquecimiento por vía pública y elimina el incentivo de buscar el cargo por interés económico.

#### 8.3.2. Sectores protegidos y aplicación

| Aplicación | Tratamiento |
|------------|-------------|
| Sectores protegidos (salud, educación, pensiones no contributivas) | La escala se aplica **íntegramente** y desde el primer mes (mes 0). |
| Resto del sector público | Se aplica al personal retenido tras la motosierra del -30%; se congela la escala para el personal saliente. |
| Jubilados IVSS rama contributiva | Se aplica la escala base (USD 500 mínimo) con proporcionalidad a años de servicio. |
| Jubilados IVSS rama no contributiva (PBU) | Pensión Básica Universal no contributiva se mantiene en USD 500 mínimo indexado. |
| Personal militar profesional | Escala propia complementaria (mínimo USD 1.200, máximo USD 5.000) con sobresueldos por especialidad y riesgo operativo. |

#### 8.3.3. Costo fiscal estimado de la nueva escala

Asumiendo una planta post-motosierra de **~2,5 millones de empleados** distribuidos proporcionalmente a las categorías (escenario conservador):

| Categoría | Personas estimadas | Salario USD | Costo anual (USD M) |
|-----------|--------------------:|------------:|---------------------:|
| Mínimo (USD 500) | 1.300.000 | 500 | 7.800 |
| Profesores + policías + bomberos (USD 1.200) | 700.000 | 1.200 | 10.080 |
| Médicos generales + personal administrativo medio (USD 1.500) | 350.000 | 1.500 | 6.300 |
| Médicos especialistas + profesionales senior (USD 3.000) | 120.000 | 3.000 | 4.320 |
| Ministros, jueces, diputados, fiscales, directores (USD 5.000) | 30.000 | 5.000 | 1.800 |
| Presidente + gabinete reducido (USD 7.000) | 100 | 7.000 | 8,4 |
| **TOTAL nómina anual** | **~2.500.100** | — | **~30.300 M** |

**Comparación con la nómina actual**: la nómina actual (3,5 M de empleados × ~USD 50 promedio × 12 meses) se estima en **~USD 2.100 millones/año**. La nueva escala con planta reducida de 2,5 M implica un **incremento de ~14x** en la masa salarial (de USD 2.100 M a USD 30.300 M), equivalente a aproximadamente **+USD 28.200 millones/año**.

#### 8.3.4. Financiamiento del incremento salarial

El incremento de USD 28.200 millones/año se financia con:

| Fuente | Monto anual estimado (USD M) | Mecanismo |
|--------|-------------------------------|-----------|
| OPI PDVSA matriz 49% (una vez) | 8.000-15.000 | Colocación en NYSE/LSE, fondo de estabilización salarial |
| Regalías petroleras incrementadas (producción +60% en 36 meses) | 4.000-6.000 | Aumento de producción PDVSA tras reforma + filiales mixtas |
| Reforma tributaria (IVA 16% + ISLR 25%) | 5.000-8.000 | Cierre de exoneraciones + ampliación de base |
| Reducción de planta (-30%) | 600-900 | Ahorro directo sobre nómina anterior |
| Fondo de Estabilización Macroeconómica (FEM) | 2.000-4.000 | Rendimientos del fondo + colchón en años de altoprecio del petróleo |
| Endeudamiento externo responsable (post-default reestructurado) | 5.000-8.000 | Bonos soberanos a 10-30 años con garantía de ingresos petroleros |
| **TOTAL fuentes** | **24.600-41.900** | Cubre el incremento de 28.200 con holgura |

**Conclusión de financiamiento**: la escala salarial es **financieramente viable** en el horizonte de 36 meses, condicionada a la ejecución simultánea de las reformas de los dimensiones 2 (administrativa), 3 (fiscal) y 8 (función pública). Sin la reforma tributaria y la OPI, la escala no es sostenible.

#### 8.3.5. Mecanismo de indexación

Para evitar la erosión inflacionaria que ha destruido salarios previos:

1. **Indexación trimestral al IPC** del BCV (índice independiente publicado por el INE autónomo, ver dimensión 6).
2. **Cláusula de salvaguarda**: si la inflación acumulada del año supera el 20%, el ajuste se aplica mensualmente.
3. **Indexación al tipo de cambio oficial de libre convertibilidad**: una vez eliminado el cepo (mes 12), el componente en USD de los salarios se mantiene fijo; los componentes en Bs. (bonos, beneficios) se ajustan por IPC.
4. **Revisión quinquenal**: la escala se revisa por la SNEEP cada 5 años con base en productividad del sector público, comparativo OCDE y capacidad fiscal.

#### 8.3.6. Mitigación del shock social

La nueva escala salarial cumple cuatro funciones simultáneas de mitigación del shock de la motosierra:

1. **Reduce la resistencia a la salida**: el personal que se retira voluntariamente cobra USD 12.000 de bono (12 meses del nuevo mínimo) + capacitación; el personal que se queda gana **500x más** que antes.
2. **Dignifica a los que permanecen**: la función pública deja de ser sinónimo de pobreza y pasa a ser una carrera profesional competitiva.
3. **Cierra la puerta a la extorsión**: un profesor a USD 1.200 o un policía a USD 1.200 ya no necesita cobrar coimas para sobrevivir; el sistema de meritocracia + remuneración digna reemplaza la economía del soborno.
4. **Atrae talento**: la escala de USD 5.000 para jueces, fiscales y ministros atrae a profesionales que hoy están en la diáspora o en el sector privado, completando el círculo virtuoso de la meritocracia (Doc. 2).

### 8.4. Instrumentos legales
- **DNU de reorganización de la función pública (mes 0)**: declara la emergencia administrativa, autoriza retiros voluntarios.
- **Nueva Ley Orgánica del Trabajo (mes 3-6)**: deroga la LOTTT en sus artículos de inamovilidad; consagra libertad bilateral + mochila austríaca.
- **Ley Orgánica de la Función Pública (mes 6-9)**: refunde LOAFSP, consagra concurso obligatorio.
- **Ley Orgánica del Sistema Previsional (mes 6-9)**: separa IVSS contributivo y no contributivo.

### 8.5. Cronograma (12 meses)
- Mes 0: DNU reorganización + RUNPE + decreto de nueva escala salarial.
- Mes 1-3: Diagnóstico de planta + retiros voluntarios.
- Mes 3-6: Nueva LOT.
- Mes 3-12: Concurso público en sectores no protegidos.
- Mes 6-9: Ley Función Pública + Ley Sistema Previsional.
- Mes 9-12: Separación operativa del IVSS.
- Mes 0-12: Implementación gradual de la nueva escala salarial por ministerio/ente.

### 8.6. Métricas de éxito
- Reducción de planta: del ~3,5 millones a ~2,5 millones (29%) en 12 meses.
- 100% de cargos de ingreso por concurso público en 18 meses.
- **Salario mínimo del sector público: USD 500/mes (vs USD 1 actual) — incremento de 500x**.
- **Salario medio del empleado público no protegido: ~USD 1.200/mes (vs ~USD 50 actual) — incremento de ~24x**.
- Sectores protegidos: planta, presupuesto y escala salarial completa blindados.
- IVSS: rama contributiva y no contributiva operativamente separadas.

### 8.7. Costo fiscal estimado
- **Costo de retiros voluntarios**: USD 1.500-2.500 millones (bono 12 meses + capacitación + seguros).
- **Ahorro anual por reducción de planta**: USD 600-900 millones/año (compensado parcialmente por la nueva escala).
- **Costo incremental nueva escala salarial**: +USD 28.200 millones/año (financiado según § 8.3.4).
- **Saldo neto año 1 (incluye escala)**: +USD 12.000 millones (reforma fiscal + OPI compensan el alza salarial).
- **Saldo neto año 2 en adelante**: +USD 28.000-32.000 millones/año.
- **Costo transición IVSS**: USD 200-400 millones (capitalización inicial de cuentas individuales).
- **Beneficio sistémico**: profesionalización + ingreso digno en sectores protegidos + cierre de la economía del soborno + atractivo de la diáspora.

---

## 9. Dimensión educación (incorporada 2026-07-13)

### 9.1. Objetivo de reforma
Refundar el sistema educativo venezolano sobre la base de cuatro principios: **meritocracia docente, autonomía escolar progresiva, evaluación estandarizada nacional y rendición de cuentas con rankings públicos**. Derogar la Ley Orgánica de Educación (LOE) 2009 y reemplazarla por la nueva LOE 2026 (Título XIII del Doc. 5). Transformar o eliminar las universidades politizadas sin méritos académicos acreditables.

### 9.2. Acciones concretas (shock)

#### 9.2.1. Meritocracia docente

1. **Concurso público obligatorio** para todos los cargos docentes y directivos del sistema educativo público (Art. 25 nueva LOE 2026).
2. **RUNPEEducativo**: registro único de personal docente con número nacional, integrado al RUNPE general (Doc. 5 Título II).
3. **Escalafón meritocrático nacional** con seis categorías: docente I, docente II, docente especialista, coordinador, subdirector, director.
4. **Evaluación docente anual vinculante** con consecuencias (bonos, ascensos, separación).
5. **Régimen de incompatibilidad**: prohibido el ejercicio simultáneo de cargo docente y militancia política activa.

#### 9.2.2. Autonomía escolar progresiva

1. **Proyecto Educativo Institucional (PEI)**: cada escuela pública aprueba democráticamente su PEI con participación de docentes, padres y estudiantes, en el marco de los estándares nacionales.
2. **Director elegido por concurso de antecedentes y oposición**: periodo de 4 años, renovable por una sola vez con base en resultados de evaluación.
3. **Tres niveles de autonomía** según resultados de evaluación:
   - **Nivel 1 (estándar)**: 60% escuelas nuevas o en plan de mejora.
   - **Nivel 2 (autonomía media)**: escuelas con 3+ años en cuartil superior.
   - **Nivel 3 (autonomía plena)**: escuelas de excelencia (5+ años consecutivos en cuartil superior), con presupuesto propio y contratación docente flexible.
4. **Consejo Escolar Consultivo**: padres y docentes participan en decisiones presupuestarias.

#### 9.2.3. Evaluación estandarizada nacional

1. **Instituto Nacional de Evaluación Educativa (INEE)**: ente autónomo con patrimonio propio, dependiente del Ministerio de Educación.
2. **Pruebas anuales obligatorias** en 3°, 6°, 9° y 12° grado en: lenguaje, matemáticas, ciencias naturales, ciencias sociales, inglés.
3. **Comparabilidad internacional**: estándares alineados con PISA, TIMSS, PIRLS, Cambridge.
4. **Resultados públicos** por escuela, municipio y estado.

#### 9.2.4. Rendición de cuentas con rankings públicos

1. **Ranking nacional anual** publicado en Gaceta Oficial y portal del Ministerio.
2. **Plan de mejora obligatorio** para escuelas en cuartil inferior durante 3 años consecutivos; cierre si no mejora en 2 años adicionales.
3. **Bonos de excelencia**: USD 5.000 anuales a escuelas de excelencia (cuartil superior por 5 años consecutivos); se reparten 50% a docentes y 50% a infraestructura.
4. **Sanciones a la opacidad**: escuelas que rehúyen evaluación pierden financiamiento público.

#### 9.2.5. Universidades — régimen mixto (transformación o eliminación)

1. **Agencia Nacional de Acreditación Universitaria (ANAC)**: ente autónomo independiente del CNU y del Ministerio.
2. **Acreditación obligatoria cada 5 años** para todas las IES públicas y privadas.
3. **Universidades politizadas en transformación** (18 meses):
   - Diagnóstico de producción científica indexada (Scopus, Web of Science).
   - Diagnóstico de empleabilidad de egresados.
   - Diagnóstico de acreditación previa nacional o internacional.
   - Las que no tengan al menos uno de los tres indicadores entran en proceso de fusión o cierre.
4. **Financiamiento público indexado**: el presupuesto se vincula a (a) acreditación vigente, (b) producción científica, (c) empleabilidad. Las no acreditadas pierden financiamiento en 24 meses.
5. **Mantener la autonomía universitaria constitucional** (Art. 109 CRBV), pero condicionada a acreditación.

#### 9.2.6. Sectores protegidos

- **Gasto educativo en primaria y secundaria se mantiene**: ~3,5% del PIB actual como mínimo, creciendo a 5% en 36 meses.
- **Salarios docentes protegidos** dentro de la escala del Doc. 5 Art. 13 (USD 1.200 mínimo, USD 3.000 especialistas).
- **No se aplica motosierra** al personal docente en ejercicio; sí se aplica concurso público para vacantes.

### 9.3. Instrumentos legales

- **DNU inicial (mes 0)**: declara la emergencia educativa, suspende el ciclo de designaciones políticas, autoriza concurso extraordinario para vacantes directivas.
- **Nueva Ley Orgánica de Educación — LOE 2026 (mes 6-9)**: refunde la LOE 2009; consagra los cuatro principios.
- **Ley Orgánica de la Educación Universitaria (LOEU 2026, mes 9-12)**: régimen de acreditación + transformación de universidades politizadas.
- **Ley Orgánica del INEE (mes 3-6)**: crea el Instituto Nacional de Evaluación Educativa.
- **Ley Orgánica de la ANAC (mes 3-6)**: crea la Agencia Nacional de Acreditación Universitaria.
- **Reglamento de Concurso Público Docente (mes 6-9)**: dictado por el Ministerio de Educación.

### 9.4. Cronograma (12 meses)

- Mes 0: DNU emergencia educativa.
- Mes 1-3: Concurso extraordinario para 5.000 cargos directivos vacantes.
- Mes 3-6: Ley INEE + Ley ANAC; instalación de ambos entes.
- Mes 6-9: Nueva LOE 2026; primera prueba nacional estandarizada (piloto en 1.000 escuelas).
- Mes 9-12: LOEU 2026; primer ranking nacional publicado; proceso de transformación de universidades politizadas iniciado.

### 9.5. Métricas de éxito

- 100% de cargos directivos del sistema educativo público cubiertos por concurso público en 18 meses.
- 100% de docentes en ejercicio con evaluación de idoneidad en 24 meses.
- Primera prueba nacional estandarizada aplicada a 100% de los estudiantes de 3°, 6°, 9° y 12° en 12 meses.
- Ranking nacional publicado en Gaceta Oficial en 12 meses.
- 100% de IES en proceso de acreditación en 24 meses.
- 50% de universidades politizadas fusionadas o cerradas en 36 meses.
- Mejora de 30 puntos en resultados de prueba nacional en 60 meses.
- Cobertura neta en educación media: del 55% al 80% en 60 meses.

### 9.6. Costo fiscal estimado

- **Inversión en concurso docente**: USD 100-150 millones (logística, jurado, plataformas).
- **Costo del INEE**: USD 50-80 millones/año (pruebas, análisis, publicaciones).
- **Costo de la ANAC**: USD 20-30 millones/año (evaluadores pares, estándares).
- **Bonos de excelencia**: USD 50-100 millones/año (5.000 USD × 10.000-20.000 escuelas).
- **Aumento del gasto educativo**: del 3,5% al 5% del PIB en 36 meses = +USD 1.500-2.000 millones/año.
- **Saldo neto año 1**: -USD 200-300 millones (inversión inicial sin retorno aún).
- **Saldo neto año 5**: positivo (retornos en capital humano, productividad, empleabilidad).
- **Beneficio sistémico**: cierre de la brecha educativa Caracas-interior, retorno de la diáspora de docentes, recuperación de la movilidad social por mérito.

---

## 10. Cuadro consolidado: inversiones, ahorros y resultados esperados (año 1)

| Dimensión | Inversión año 1 (USD M) | Ahorro/Ingreso año 1 (USD M) | Resultado clave |
|-----------|--------------------------|------------------------------|-----------------|
| Constitucional | 10 | 200 (gasto inercial derogado) | 0 leyes habilitantes; Art. 303 reinterpretado |
| Administrativa | 100 | 1.500 | 9 ministerios, 40 entes; -35% gasto corriente |
| Fiscal | 300 | 11.000 (OPI + tributaria) | OPI PDVSA, IVA 16%, cepo eliminado, FEM |
| Justicia | 250 | 0 (costo sistémico) | TSJ meritocrático; LORAFEE operativa |
| Digital | 1.200 (Guri-1) | 2.000 (privatización CANTV/Movilnet) | 10M Cédula-RUT; CANTV privada |
| Planificación | 80 | 500 (derogación leyes inerciales) | SNEEP operativa; INE autónomo |
| Descentralización | 1.000 (transferencias) | 0 (gasto nuevo) | 6 leyes de bases; CFG reactivado |
| Función pública (motosierra + retiros) | 2.500 (retiros) | 900 (reducción planta) | -30% planta; sectores protegidos |
| **Escala salarial nueva** | **30.300** (nómina incremental) | — | Mínimo USD 500; Presidente USD 7.000; sectores protegidos blindados |
| **TOTAL sin nueva escala** | **5.440** | **17.700** | **Saldo neto año 1 sin escala: +USD 12.260 millones** |
| **TOTAL con nueva escala** | **35.740** | **17.700** | **Saldo neto año 1 con escala: -USD 18.040 millones (financiado con OPI + crédito)** |

### 9.1. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Resistencia de la burocracia a la motosierra | Alta | Alto | Indemnización generosa; cronograma claro; comunicación directa |
| Fuga de capital humano calificado | Alta | Alto | Salarios meritocráticos + concursos ágiles + blindaje de sectores protegidos |
| Sanciones internacionales que bloqueen la OPI | Media | Alto | Banco de inversión con experiencia en OFAC; estructura societaria offshore con *compliance* reforzado |
| Litigios de accionistas privados contra expropiaciones | Media | Alto | LORAFEE + cláusula *pay-before-take*; debido proceso reforzado |
| Hiperinflación residual durante la transición | Media | Alto | Anclaje fiscal por FEM; reforma tributaria anti-inflacionaria |
| Crisis social por costo del ajuste | Alta | Alto | **Nueva escala salarial** (mínimo USD 500) + sectores protegidos blindados (salud, educación, pensiones no contributivas) + retiros voluntarios incentivados; comunicación transparente |

### 9.2. Ventana de oportunidad

La presente propuesta se ejecuta en una ventana de **12 meses** bajo shock estilo Milei, aprovechando:
- Respaldo inicial de la opinión pública en reformas estructurales.
- Disposición de la comunidad internacional a apoyar una transición ordenada.
- Recursos extraordinarios de la OPI de PDVSA (~USD 10.000 millones).
- Capacidad técnica instalada en la diáspora venezolana (potencial retorno).

Pasados los 12 meses, la fatiga social, la captura burocrática residual y la dinámica política normal harán inviables reformas de esta magnitud. **La oportunidad es ahora o nunca**.

---

## Próximo documento

**Documento 4: Plan de implementación 0-12 meses** (cronograma detallado, hitos semanales, matriz de responsabilidades, sistema de monitoreo semanal del Presidente de la República + gabinete).

---

*Documento elaborado en el marco del proyecto de Reforma del Estado venezolano, con base en la base de conocimiento `kb_gobierno` (Qdrant) y referencias citadas. Las cifras deben ser actualizadas con datos oficiales antes de la versión final. Los principios rectores están consolidados en `~/qdrant-kb/memory.md`.*

---

## Glosario de siglas

| Sigla | Nombre completo |
|---|---|
| **AN** | Asamblea Nacional |
| **BCV** | Banco Central de Venezuela |
| **BND** | Banco Nacional de Datos |
| **CANTV** | Compañía Anónima Nacional Teléfonos de Venezuela |
| **CNE** | Consejo Nacional Electoral |
| **COT** | Código Orgánico Tributario |
| **CRBV** | Constitución de la República Bolivariana de Venezuela |
| **Cédula-RUT** | Cédula con Rol Único Tributario |
| **FEM** | Fondo de Estabilización Macroeconómica |
| **IVSS** | Instituto Venezolano de los Seguros Sociales |
| **LOAFSP** | Ley Orgánica de la Administración Financiera del Sector Público |
| **LOAP** | Ley Orgánica de la Administración Pública |
| **LOBCV** | Ley Orgánica del Banco Central de Venezuela |
| **LOE** | Ley Orgánica de Educación |
| **LOH** | Ley Orgánica de Hidrocarburos |
| **LOM** | Ley Orgánica de Minas |
| **LOPP** | Ley Orgánica de Planificación Pública |
| **LORAFEE** | Ley Orgánica del Régimen de Adquisición Forzosa de Acciones de Empresas Estratégicas |
| **LOTSJ** | Ley Orgánica del Tribunal Supremo de Justicia |
| **LOTTT** | Ley Orgánica del Trabajo, los Trabajadores y las Trabajadoras |
| **OCDE** | Organización para la Cooperación y el Desarrollo Económicos |
| **OPI** | Oferta Pública Inicial |
| **PDVSA** | Petróleos de Venezuela S.A. |
| **SNI** | Sistema Nacional de Identidad |
| **SPDP** | Superintendencia de Protección de Datos Personales |
| **SUNAA** | Superintendencia Nacional de Aguas y Saneamiento |
| **TSJ** | Tribunal Supremo de Justicia |
| **VePass** | Clave Única de Identidad Digital |

