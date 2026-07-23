---
titulo: Reforma Integral del Estado Venezolano - Pilar III.7
parte: III.7
version: 0.1.2 (limpieza final: 0 caracteres no-Latinos; regla RUN-ADN, hospital local, captura obligatoria adultos; RUI en III.7.3.2; algoritmo DV en III.7.5.6)
fecha: 2026-07-15
instituciones_nuevas: Servicio Nacional de Identificación, Superintendencia de Protección de Datos Personales (SPDP), Centro de Datos Guri-1/2/3, Servicio Nacional del Registro Inmobiliario (SNRI), Superintendencia Nacional de Catastro (SUNAC)
infraestructura_critica: 3 sitios redundantes cerca del Guri (100 ha + 40 MW pico)
referente_principal: Chile (RUN=RUT, ClaveUnica, Cedula QR+NFC, Conservador Bienes Raices) + Estonia (X-Road, e-Land Register) + India (Aadhaar) + Suecia (Lantmateriet, sistema Torrens)
sistemas_clave: VePass (clave única), SNI (Sistema Nacional Identidad), BND (Banco Nacional Datos), INIA (Inteligencia Artificial), Banco Nacional ADN, RUP (Registro Unico Profesionales), RUI (Registro Unico Inmuebles)
clausula_continuidad: 3/4 Asamblea + referendum popular
---

# PARTE III — PILARES DE LA REFORMA

# III.7. Gobierno digital, identidad nacional y soberanía de datos

> *"La tecnología no es un adorno de la administración pública: es la infraestructura básica sobre la cual se sostiene la posibilidad de un Estado de derecho en el siglo XXI."*

---

## III.7.1. El problema: fragmentación de identidad y opacidad de datos

Venezuela tiene hoy, como casi todos los países latinoamericanos, **múltiples sistemas de identificación que no se hablan entre sí**:

| Sistema | Entidad | Uso | Número |
|---------|---------|-----|--------|
| Cédula de identidad | SAIME | Identidad civil | V-XXXXXXX |
| RIF | SENIAT | Identidad tributaria | J-XXXXXXX / V-XXXXXXX (separado) |
| IVSS | Seguro Social | Identidad laboral | Número interno |
| CNE | Consejo Nacional Electoral | Identidad electoral | Cédula |
| Registro Civil | Registro Civil | Acta de nacimiento | Número de acta |
| Pasaporte | SAIME | Identidad internacional | Cédula + letra |
| Tarjeta de la patria | Organo del Estado | Identificación política | Cédula |

**Consecuencias inmediatas**: un ciudadano venezolano promedio necesita presentar 4-7 documentos diferentes para realizar trámites que involucran a dos o más instituciones. Cada institución tiene su propio archivo, su propia lógica de actualización y su propia vulnerabilidad al fraude. La ONGs Provea documenta anualmente miles de casos de personas excluidas de servicios públicos porque su información está duplicada, desactualizada o contradicha entre sistemas.

Esta fragmentación tiene además un **costo político**: permite que cada político de turno construya su propio padrón clientelar a partir del control de una base de datos. La fragmentación es funcional al clientelismo.

La reforma digital es, además de modernizadora, **libertadora**: rompe el monopolio político sobre la identidad del ciudadano.

### Referentes internacionales

| País | Sistema de identidad | Integración | Clave única |
|------|---------------------|-------------|-------------|
| **Chile** | RUN = RUT (un número para todo) | Total (civil + tributaria + electoral + salud) | **ClaveÚnica** |
| **Singapur** | NRIC | Alta (SingPass + MyInfo) | **SingPass** |
| **Estonia** | KI-kaart (tarjeta con chip) | Total (X-Road) | e-ID |
| **India** | Aadhaar | Total (12 dígitos + 10 huellas + 2 iris) | e-Aadhaar |
| **Emiratos Árabes** | Emirates ID | Alta (smart card + biométrica) | UAE Pass |
| **Venezuela (actual)** | Múltiples sistemas | **Nula** | **No existe** |

El modelo que esta reforma adopta es **el chileno** (RUN = RUT, ClaveÚnica, Cédula-RUT con QR y NFC), con adaptaciones al contexto venezolano y con elementos biométricos inspirado en el modelo indio (Aadhaar) que Chile aún no implementó.

---

## III.7.2. Data center soberano cerca del Guri

### Justificación de la ubicación

La Central Hidroeléctrica Simón Bolívar (Guri), en el estado Bolívar, es la segunda central hidroeléctrica más grande del mundo (10.235 MW instalados). Tiene, además:

- **Energía confiable**: la red del Guri alimenta ~80% del consumo eléctrico nacional y es relativamente estable frente a perturbaciones.
- **Refrigeración natural abundante**: el río Caroní y el Embalse de Guri proveen agua fría ilimitada para sistemas de refrigeración líquida de servidores.
- **Ubicación estratégica en el interior**: a más de 600 km de la costa, fuera del alcance de las principales rutas de huracanes y alejado de los principales blancos de una agresión militar convencional.
- **Distancia de Caracas y Maracaibo**: reduce el riesgo de concentración geográfica del poder de procesamiento.
- **Suelo geológicamente estable**: la zona del Macizo Guayanés es de los más antiguos y estables del planeta, con bajísimo riesgo sísmico.

### Diseño del complejo

El complejo se construye en el municipio Caroní (Ciudad Guayana), con un diseño de **tres sitios redundantes** ("3-site active-active failover"inspirado en a los data center de AWS y Google):

| Sitio | Función | Capacidad inicial | Capacidad año 6 |
|-------|---------|-------------------|-------------------|
| **Guri-1** (campus principal, ~100 ha) | Producción, IA, banco de ADN | 20 MW | 80 MW |
| **Guri-2** (a 30 km, municipio Sucre) | Backup activo | 10 MW | 40 MW |
| **Guri-3** (cueva natural del Macizo Guayanés) | Archivo frío + recovery ante desastre | 2,5 MW | 10 MW |

### Nota sobre la escala

El complejo Guri propuesto tiene una escala equivalente a **Colossus** (la primera computadora electrónica de Bletchley Park, 1943): lo suficientemente grande como para hacer lo que ningún sistema anterior podía hacer, pero no tanto como para ser inviable técnica o financieramente. Las cifras de esta propuesta (100 ha + 40 MW pico en Guri-1 al año 6) reflejan esa filosofía.

**Comparación con alternativas reales** (año 2024):

| Complejo | Tamaño | Capacidad |
|----------|--------|-----------|
| Meta (ex-Facebook) Eagle Mountain, Utah (en construcción) | ~485 ha | 1.000 MW planeados |
| AWS US East, Ashburn | ~320 ha | ~400 MW |
| Google The Dalles, Oregón | ~280 ha | ~400 MW |
| Microsoft Quincy, Washington | ~240 ha | ~250 MW |
| **Guri-1 (esta propuesta)** | **100 ha** | **40 MW** |
| Centro de datos CERN, Ginebra | ~40 ha | ~40 MW |

El complejo Guri-1 propuesto es **un orden de magnitud menor** que las grandes granjas hyperscale comerciales, pero comparable a la capacidad de procesamiento del CERN (suficiente para procesar datos de los experimentos LHC, modelado genómico a escala poblacional, IA nacional).

La eficiencia esperada (PUE ~1,2 con refrigeración líquida del río Caroní y climas frescos del Macizo Guayanés) es **superior a la media industrial** (~1,5-1,8). Esto reduce el consumo eléctrico y, en consecuencia, el costo operativo.

### Soberanía de datos

Por disposición constitucional (nuevo artículo 134-B propuesto):

> *"Todos los datos personales de los venezolanos y todos los datos del Estado venezolano se almacenan, procesan y custodian exclusivamente en territorio venezolano, en infraestructura operada por el Estado o por contratistas privados bajo control público. Ninguna autoridad puede autorizar la transferencia de datos personales o del Estado a jurisdicciones extranjeras sin autorización de las tres cuartas partes (3/4) de la Asamblea Nacional y resolución fundada del Tribunal Supremo de Justicia en Sala Constitucional."*

### Computación de alta capacidad para IA

El complejo Guri aloja la **Infraestructura Nacional de Inteligencia Artificial (INIA)**, plataforma compartida que permite:

- **A la DNA-RB**: detección de patrones de contratación anómala, análisis de redes financieras sospechosas, cruce de datos patrimoniales.
- **A la MIED-LAM**: personalización adaptativa de los currículos del Programa Inteligencia 2.0, evaluación continua del aprendizaje.
- **A la defensa**: sistemas de comando y control, simulación, análisis de inteligencia.
- **A la salud pública**: modelado epidemiológico, análisis genómico poblacional, gestión hospitalaria.
- **A la justicia**: análisis de jurisprudencia, detección de patrones de reincidencia, priorización de causas.
- **A la seguridad pública**: reconocimiento facial y de placas con autorización judicial específica, análisis de patrones delictivos.

La INIA opera bajo principios de transparencia algorítmica (auditoría externa anual de los modelos) y protección de derechos fundamentales (decisiones automatizadas con explicación obligatoria, recurso humano garantizado).

---

## III.7.3. Banco Nacional de Datos (BND)

El BND integra, en una arquitectura federada inspirado en el modelo X-Road de Estonia, las siguientes bases de datos sectoriales:

| Base | Entidad responsable | Datos | Acceso |
|------|---------------------|-------|--------|
| **Registro Civil Unificado** | Servicio Autónomo de Registro Civil | Nacimientos, defunciones, matrimonios, uniones, RUN/RUT | Universal con VePass |
| **Expediente Clínico Electrónico Nacional (ECEN)** | Ministerio para la Salud | Historial médico, prescripciones, alergias, imágenes diagnósticas | Paciente + equipo médico autorizado |
| **Expediente Educativo Nacional (EEN)** | MIED-LAM | Calificaciones, avance curricular, becas, sanciones | Estudiante + padres + docentes autorizados |
| **Expediente Judicial Electrónico (EJE)** | Poder Judicial | Causas, sentencias, antecedentes, medidas cautelares | Jueces + fiscales + abogados con VePass |
| **Registro de Identificación Biométrica (RIB)** | Servicio Nacional de Identificación | 10 huellas, foto, firma, ADN | Sólo VePass + PIN |
| **Banco Nacional de ADN** | Servicio Nacional de Identificación + MIED-LAM | Muestra genética de cada nacido vivo, árbol genealógico de agregación familiar | Sólo con orden judicial específica |
| **Registro Nacional de Conductores (RNC)** | Ministerio para Transporte | Licencias, infracciones, vehículos asociados | Conductor + autoridades de tránsito + policias|
| **Registro Tributario (RT)** | SENIAT | RIF = RUN, declaraciones, pagos, deudas, exenciones | Contribuyente + SENIAT |
| **Registro Electoral (RE)** | Consejo Nacional Electoral | Padrón electoral (idéntico al Registro Civil por VePass) | CNE + ciudadanos |
| **Registro Patrimonial de Funcionarios (RPF)** | DNA-RB | Patrimonio de funcionarios públicos, comparación con ingresos | DNA-RB + CGR con orden judicial |
| **Sistema Único de Salud (SUS)** | Ministerio de Salud + alcaldías | Afiliación, prestaciones, copagos | Ciudadano + proveedor autorizado |
| **Registro Único de Profesionales (RUP)** | BND + Ministerio de Educación Universitaria | Títulos universitarios: técnico superior, pregrado, especialización, maestría, doctorado; institución, fecha, reconocimiento, apostilla | Universal con VePass + consentimiento del titular |
| **Registro Único de Inmuebles (RUI)** | Servicio Nacional del Registro Inmobiliario (SNRI) + Superintendencia Nacional de Catastro (SUNAC) | Código RUI único, linderos georeferenciados, cadena de titulación completa, gravámenes, uso de suelo, valoración catastral, multipropiedad | Universal con VePass (datos básicos) + VePass-Fuerte (datos completos) |

### Arquitectura federada (no monolítica)

Cada institución dueña de su base de datos, pero todas interoperan mediante el estándar X-Road inspirado en. **Ningún dato se centraliza físicamente**: el BND es un protocolo de interoperabilidad, no una mega-base. Cada consulta pasa por el VePass del solicitante y queda registrada en bitácora inalterable (blockchain con anclaje al Guri-3).

---



### III.7.3.1. Registro Único de Profesionales (RUP)

El RUP es la base de datos oficial de **todos los títulos académicos universitarios y de educación técnica superior** otorgados por instituciones reconocidas por el Estado venezolano. Inspirado en el modelo italiano de la banca dati del MIUR (Ministero dell'Istruzione, dell'Università e della Ricerca) y en el español del Registro Nacional de Títulos Universitarios (RNTU), pero con una arquitectura digital interoperable con el VePass.

#### Cobertura del RUP

El RUP registra, con valor probatorio universal en Venezuela y en el extranjero, los siguientes títulos:

- **Técnico superior universitario** (TSU): título otorgado por los institutos universitarios de tecnología (IUT) y colegios universitarios, con duración de 2-3 años.
- **Pregrado / licenciatura / ingeniería / arquitectura**: títulos de 4-6 años en universidades acreditadas.
- **Especialización**: estudios de postgrado de 1-2 años con 24-60 créditos.
- **Maestría**: postgrado de 1,5-2 años con 60-90 créditos, con tesis de grado.
- **Doctorado**: postgrado de 3-5 años con tesis doctoral original y defensa pública.

Adicionalmente, se registran:

- **Cédula profesional** para profesiones reguladas por ley (abogado, médico, ingeniero, arquitecto, psicólogo, contador, etc.) emitida por la autoridad competente.
- **Especialidades médicas** reconocidas por la Federación Médica Venezolana.
- **Títulos extranjeros** revalidados por el Ministerio de Educación Universitaria (reconocimiento, equiparación o convalidación).
- **Sanciones profesionales**: suspensiones, inhabilitaciones, revocatorias de cédula profesional, sentencias disciplinarias firmes.

#### Datos registrados por cada título

| Campo | Descripción |
|-------|-------------|
| RUN del titular | Vinculación inequívoca con la identidad |
| Tipo de título | TSU / pregrado / especialización / maestría / doctorado / cédula |
| Denominación | Nombre oficial del título (ej. "Médico Cirujano", "Magíster en Administración Pública") |
| Institución emisora | Universidad + facultad + sede |
| Fecha de expedición | Día/mes/año |
| Número de registro | Asignado por la institución al expedir |
| Reconocimiento | Estado: vigente / suspendido / revocado |
| Apostilla electrónica | Estándar e-Apostille de la Conferencia de La Haya |
| Verificación biométrica | Huella del titular al momento de registro |
| Código QR + URL | Acceso universal para verificación por terceros |

#### Ingreso al RUP

El ingreso al RUP ocurre de oficio por la **institución educativa** al momento de la expedición del título:

1. La universidad o IUT carga electrónicamente los datos en el BND dentro de los **30 días siguientes** a la fecha de graduación.
2. El graduado **verifica sus propios datos** mediante VePass-Plus y los confirma.
3. La universidad firma electrónicamente con sello digital certificado por la autoridad de certificación del BND.
4. El RUP genera la **apostilla electrónica** con firma criptográfica verificable universalmente.

Para **títulos anteriores** a la entrada en vigencia del RUP, las universidades tienen un plazo de **5 años** para cargar masivamente sus archivos de egresados. Los profesionales ya egresados pueden además **autocargar sus propios títulos** mediante VePass, sujetos a verificación por la universidad emisora.

Para **títulos extranjeros revalidados**, el Ministerio de Educación Universitaria inserta el registro al momento de emitir la resolución de revalidación.

#### Verificación universal

Cualquier persona natural o jurídica puede verificar un título del RUP mediante:

- **App VePass** con el RUN del titular + el código QR del documento.
- **Sitio web vepass.gob.ve** con RUN del titular.
- **Línea 1-800-VEPASS** con RUN del titular (consulta verbal).
- **Acceso institucional** para empleadores, mediante convenio y VePass-Plus.

La verificación devuelve: **estado del título (vigente/suspendido/revocado)**, institución, fecha, sanciones si las hubiere. **No devuelve** otros datos personales del titular.

#### Marco constitucional y legal

Reforma al artículo 104 CRBV (educación) adicionando:

> *"Todos los títulos académicos universitarios y técnicos superiores otorgados por instituciones reconocidas por el Estado se inscriben de oficio en el Registro Único de Profesionales, administrado por el Banco Nacional de Datos. El registro confiere valor probatorio universal a los títulos y permite su verificación por cualquier persona natural o jurídica. La falsificación, suplantación o adulteración de títulos académicos será sancionada conforme a la ley penal."*

Reforma al Código Penal:

- **Tipo penal nuevo**: "Ejercicio ilegal de profesión con título falso o adulterado", con pena de 4-8 años de prisión.
- Agravante: cuando el ejercicio ilegal cause daño a la salud, integridad o patrimonio de tercero, pena de 8-15 años.

#### Integración con otros pilares

El RUP es la **columna vertebral** de la meritocracia en el servicio civil:

| Pilar | Uso del RUP |
|-------|-------------|
| **III.1 Servicio Civil** | Verificación de requisitos académicos para concursos públicos |
| **III.3 MIED-LAM** | Verificación de credenciales docentes para ingreso y ascenso |
| **III.6 Justicia y DNA-RB** | Verificación de títulos de jueces, fiscales y funcionarios del Poder Judicial |
| **III.2 Seguridad** | Verificación de credenciales del personal policial y militar |
| **III.7 Salud** | Verificación de matrículas profesionales del personal de salud |

Sin un RUP confiable, la meritocracia es invocable pero no verificable. Con el RUP, cualquier empleador público o privado puede confirmar las credenciales académicas en segundos.

#### Continuidad del RUP

La reforma incluye una cláusula específica:

> *"Ninguna reforma al régimen del Registro Único de Profesionales podrá aprobarse sin el voto de las tres cuartas partes (3/4) de la Asamblea Nacional y la ratificación mediante referéndum popular."*

La protección es equivalente a la del VePass, MIED-LAM y DNA-RB.

### III.7.3.2. Registro Único de Inmuebles (RUI)

El RUI es la base de datos oficial de **todos los bienes inmuebles** del territorio venezolano —viviendas, apartamentos, edificios, locales comerciales, oficinas, naves industriales, terrenos rústicos y urbanos, fincas agropecuarias, fundos, lotes, parcelas, inmuebles del Estado y concesiones— con valor probatorio universal, trazabilidad histórica completa y protección anti-fraude. Inspirado en el **Conservador de Bienes Raíces chileno** (DFL 1.224 de 1939, con sus reformas), el **e-Land Register estonio** (en operación digital desde 1994, con blockchain KSI desde 2008, primer registro de propiedad del mundo con firma criptográfica verificable), el **Lantmäteriet sueco** y el **sistema Torrens** australiano. La arquitectura propuesta supera los modelos fragmentados latinoamericanos (registros y catastros separados por municipio o estado) con un sistema único, federado, digital y verificable criptográficamente.

#### Cobertura del RUI

El RUI inscribe, con valor probatorio universal en Venezuela y reconocimiento internacional (vía apostilla electrónica de la Conferencia de La Haya), los siguientes tipos de inmuebles:

- **Vivienda unifamiliar y multifamiliar**: casas, apartamentos, townhouses.
- **Edificios y desarrollos verticales**: torres residenciales, edificios de oficinas, complejos comerciales.
- **Terrenos**: urbanos (solares baldíos), rurales (fincas, fundos, parcelas agropecuarias), industriales.
- **Locales comerciales y oficinas**: con o sin uso mixto.
- **Naves industriales y galpones**: plantas manufactureras, centros logísticos, depósitos.
- **Inmuebles rurales**: haciendas, fundos, unidades de producción agropecuaria, bosques productivos, fundos piscícolas.
- **Inmuebles del Estado y bienes de dominio público**: parques nacionales, vialidad, infraestructura crítica, inmuebles destinados a servicios públicos.
- **Concesiones y derechos de uso**: otorgados por el Estado (mineras, hidroeléctricas, telecomunicacionales, portuarias), con su plazo, canon y condiciones.
- **Servidumbres, usufructos y derechos reales limitados**: registrados como gravámenes vinculados al inmueble principal.

#### Datos inscritos por cada inmueble

Cada inmueble registrado en el RUI tiene asociado un **Código RUI único** (alfanumérico de 16 caracteres, con checksum) que lo identifica de manera irrepetible y permanente. La ficha incluye:

| Campo | Descripción |
|-------|-------------|
| **Código RUI** | Identificador único irrepetible |
| **RUN del titular registral** | Persona natural propietaria (vinculación con BND) |
| **Razón social del titular** | Si es persona jurídica (RUN de la empresa + RUP del representante legal) |
| **Tipo de inmueble** | Vivienda / comercio / industrial / rural / público / concesión |
| **Uso actual** | Residencial / comercial / industrial / agropecuario / mixto / baldío |
| **Ubicación georeferenciada** | Coordenadas UTM + polígono de linderos (formato GeoJSON en datum SIRGAS-REGVEN) |
| **Dirección postal** | Estado, municipio, parroquia, avenida, calle, número, piso, apartamento |
| **Linderos** | Norte, sur, este, oeste con dimensiones y colindancias (texto + croquis) |
| **Superficie total** | m² (terreno) + m² (construcción si aplica) |
| **Año de construcción** | Para inmuebles edificados |
| **Valoración catastral** | Actualización anual por SUNAC conforme a índices de mercado |
| **Valoración de mercado** | Referencia histórica de transacciones comparables |
| **Estado registral** | Vigente / suspendido / en proceso de transferencia / en litigio |
| **Gravámenes** | Hipotecas, embargos, prendas, servidumbres, usufructos, litigios |
| **Derecho de uso** | Propiedad plena / arrendamiento / concesión / comodato / ocupación autorizada |
| **Certificado de libertad** | Indicador binario: libre de gravámenes (con timestamp de la verificación) |
| **Historial de transferencias** | Cadena completa desde la primera inscripción hasta la fecha, con cada acto, fecha, partes, notario, número de protocolo |
| **Fotografías** | Imágenes actualizadas del exterior e interior (al menos 4 + fachada) |
| **Plano catastral** | Plano arquitectónico registrado con firma del profesional colegiado (vía RUP) |
| **Hash criptográfico** | Del documento de propiedad digital + anclaje a blockchain del Guri-3 |

#### Cadena de titulación (principio de tracto sucesivo)

Inspirado en el sistema Torrens, el RUI mantiene la **cadena ininterrumpida** de todos los actos jurídicos que han afectado al inmueble desde su primera inscripción:

1. **Título originario**: primera inscripción (compraventa del Estado, prescripción adquisitiva, donación, expropiación, sucesión).
2. **Transferencias intermedias**: cada compraventa, donación, permuta, herencia, división de comunidad, fusión de inmuebles.
3. **Gravámenes constituidos y cancelados**: hipotecas, prendas, embargos, servidumbres, con sus fechas de inicio y cancelación.
4. **Actos administrativos**: declaratorias de utilidad pública, afectaciones, desafectaciones, expropiaciones.
5. **Litigios**: demandas de propiedad, reivindicaciones, prescripciones en curso, sentencias firmes.

**Cualquier transferencia o gravamen posterior debe citar expresamente la inscripción anterior**. La falta de tracto sucesivo es causal automática de nulidad registral y de responsabilidad penal del notario autorizante.

#### Multipropiedad y régimen de comunidad

El RUI soporta todos los regímenes de cotitularidad:

- **Proindiviso**: cuota porcentual de cada copropietario (ej. tres hermanos con 33,33% cada uno).
- **Condominio vertical**: unidades funcionales autónomas (apartamentos) más áreas comunes proporcionales (modelo de la Ley de Propiedad Horizontal venezolana de 1983 + reforma 2026).
- **Conjunto inmobiliario**: urbanizaciones con calles, áreas verdes, equipamiento colectivo.
- **Fideicomiso sobre inmuebles**: el fiduciario figura como titular registral, los beneficiarios como titulares del derecho económico (vinculado al RUP del fiduciario y al fideicomiso registrado).
- **Propiedad comunitaria indígena**: figuras asociativas de pueblos y comunidades indígenas conforme al Art. 119 CRBV y la Ley Orgánica de Pueblos y Comunidades Indígenas.

#### Procedimiento de inscripción registral

Toda mutación de propiedad, gravamen, afectación o acto relevante se inscribe en el RUI mediante el siguiente procedimiento obligatorio:

1. **Solicitud**: el notario público (registrado en el RUP, con VePass-Firma profesional) carga la minuta del acto en el sistema RUI vía BND.
2. **Verificación de identidad y capacidad**: el sistema verifica el VePass-Fuerte del vendedor, del comprador y del notario. Bloquea la operación si alguno tiene inhabilidad (muerte, interdicción, embargo previo sobre el bien, inhibición notarial, inhabilitación política, investigación penal).
3. **Verificación registral**: el sistema consulta la **libertad del inmueble** (gravámenes, litigios, afectaciones, sucesiones pendientes). Si hay alerta, bloquea hasta subsanación.
4. **Verificación fiscal**: cruce automático con el SENIAT — exige solvencia de impuestos municipales y nacionales del vendedor sobre el inmueble.
5. **Verificación catastral**: la SUNAC confirma que la ubicación, superficie y linderos declarados coinciden con el catastro. Si hay discrepancia, bloquea hasta regularización.
6. **Firma múltiple**: el acto se firma con VePass-Firma por todas las partes y por el notario. Las firmas quedan registradas con timestamp, hash criptográfico y anclaje blockchain.
7. **Pago**: el sistema calcula y cobra los aranceles registrales y notariales. El comprobante queda asociado al acto.
8. **Inscripción**: el sistema emite el nuevo Certificado de Libertad + Título de Propiedad digital, actualiza el RUI, y notifica al Catastro (SUNAC) y al SENIAT para los fines fiscales correspondientes.
9. **Notificación a las partes**: cada interviniente recibe confirmación por VePass + correo electrónico + SMS.

**Plazo máximo total**: 24 horas hábiles desde la solicitud hasta la inscripción efectiva, en condiciones normales.

#### Anti-fraude: las 4 garantías del RUI

1. **Anti-doble venta**: cuando un vendedor firma la transferencia, el sistema marca el inmueble como **"en proceso de transferencia"** y bloquea cualquier nueva operación sobre el mismo. La marca se levanta con la inscripción efectiva o caduca a los 30 días si no se completa.
2. **Anti-falsificación de títulos**: cualquier modificación de la ficha registral requiere VePass-Firma del titular registral vigente + del notario actuante. La dirección IP, la geolocalización del dispositivo y el timestamp quedan registrados. La firma digital sin el código OTP es inválida por construcción.
3. **Anti-prescripción fraudulenta**: las demandas de prescripción adquisitiva (usucapión) deben publicarse en el RUI en un plazo máximo de 30 días desde su interposición. Cualquier transferencia del inmueble mientras la prescripción está en curso requiere resolución judicial previa.
4. **Anclaje blockchain al Guri-3**: cada inscripción genera un hash criptográfico anclado a la cadena inalterable del BND (blockchain con anclaje al Guri-3, sección III.7.3). Esto hace materialmente imposible alterar una inscripción sin invalidar toda la cadena posterior.

#### Procedimiento de regularización de inmuebles informales

Venezuela tiene un porcentaje significativo de inmuebles en situación de informalidad (posesión sin título inscrito, títulos no saneados, ocupaciones irregulares). El RUI incorpora un **procedimiento simplificado de regularización** para estos casos:

- **Declaración posesoria notarial**: el poseedor de buena fe, con 10 años continuos de ocupación sin oposición, acude al notario y declara la posesión.
- **Publicación en el RUI durante 90 días**: el sistema publica la declaración posesoria para que cualquier titular registral previo o interesado formule oposición.
- **Sin oposición**: el notario inscribe al poseedor como titular registral con un sello especial de **"título saneado por regularización"**.
- **Con oposición**: el caso pasa al TSJ para resolución judicial conforme a la Ley Orgánica Procesal Civil.

Este procedimiento permite reducir la informalidad inmobiliaria del ~40% actual al ~5% en un plazo de 10 años, sin necesidad de masivos operativos de regularización.

#### Migración de registros preexistentes

Venezuela tiene actualmente múltiples registros: catastro municipal, Registro Público de la Propiedad (dependiente de cada estado), Registro Civil (para actos civiles), Catastro Nacional (dependiente del Ministerio del Ambiente y Recursos Naturales), y registros especiales (inmuebles rurales del INTi, inmuebles forestales, etc.). Todos estos sistemas tienen información fragmentada, duplicada y a menudo contradictoria.

La reforma ordena:

1. **Conciliación nacional inicial** (12 meses): un equipo técnico cruza las bases existentes para asignar un Código RUI a cada inmueble identificable. Inmuebles en conflicto entre dos registros se marcan con alerta de revisión.
2. **Migración progresiva** (5 años): cada registro preexistente migra al RUI con plena equivalencia funcional. Los registros tradicionales se mantienen como medio de consulta histórica durante la transición.
3. **Catastro único** (SUNAC): se crea la Superintendencia Nacional de Catastro, dependiente del Ministerio del Ambiente, con la función de mantener el catastro físico (geometría de parcelas, linderos, edificaciones) integrado con el RUI registral.
4. **Caducidad registral** (10 años): las inscripciones en registros tradicionales que no hayan sido migradas al RUI pierden valor probatorio para nuevas operaciones.

#### Uso del RUI en transacciones cotidianas

| Operación | Consulta RUI |
|-----------|--------------|
| **Compraventa** | Certificado de libertad + verificación de identidad + firma múltiple + inscripción |
| **Hipoteca** | Verificación de libertad + inscripción del gravamen + actualización ante pagos |
| **Herencia** | Determinación de inmuebles del causante + inscripción a nombre de herederos + partición |
| **Donación** | Verificación de identidad + acto notarial + inscripción |
| **División de comunidad** | Partición georeferenciada + inscripción de lotes resultantes |
| **Permuta** | Doble transferencia simultánea con verificación cruzada |
| **Arrendamiento** | Inscripción opcional del contrato (recomendada, no obligatoria) |
| **Embargo judicial** | Orden del TSJ + inscripción inmediata + levantamiento al pago |
| **Expropiación** | Decreto del Ejecutivo + orden judicial + indemnización + inscripción al Estado |
| **Sucesión intestada** | Declaración judicial de herederos + partición + inscripción |

#### Integración con otros pilares

El RUI es transversal a toda la reforma:

| Pilar | Uso del RUI |
|-------|-------------|
| **III.1 Servicio Civil** | Verificación de domicilio declarado por funcionarios públicos |
| **III.4 Fiscal** | Base del Impuesto sobre Bienes Inmuebles (IBI) — la SUNAC provee valoración catastral al SENIAT |
| **III.5 Empresas del Estado** | Inventario y privatización de activos inmobiliarios del Estado (PDVSA, Corpoelec, CANTV, etc.) |
| **III.6 Justicia y DNA-RB** | Identificación de bienes vinculados a lavado de activos; extinción de dominio |
| **III.7 Salud** | Dirección registrada del paciente para asignación de centro de atención primaria |
| **III.7 Educación** | Dirección registrada del estudiante para asignación de escuela por zona |
| **III.7 Padrón electoral** | Georreferenciación del votante para asignación de centro y mesa |

#### Marco constitucional

Reforma al artículo 115 CRBV adicionando:

> *"Todos los bienes inmuebles ubicados en el territorio de la República se inscriben en el Registro Único de Inmuebles, administrado por el Servicio Nacional del Registro Inmobiliario bajo la rectoría del Banco Nacional de Datos. La inscripción confiere valor probatorio universal y es requisito indispensable para todo acto jurídico de disposición, gravamen o afectación. La Superintendencia Nacional de Catastro mantiene el catastro físico integrado. La falsificación, alteración o supresión de inscripciones registrales será sancionada conforme a la ley penal con pena de ocho (8) a quince (15) años de prisión, sin perjuicio de la nulidad absoluta del acto y de las responsabilidades civiles y administrativas."*

#### Marco penal complementario

- **Tipo penal nuevo**: "Fraude inmobiliario registral", con pena de 8-15 años.
- **Agravante**: cuando se realice mediante violencia, intimidación o contra personas vulnerables (adultos mayores, personas con discapacidad), pena de 12-20 años.
- **Tipo penal nuevo**: "Ejercicio ilegal de notario o fedatario", con pena de 6-12 años.
- **Cooperación necesaria del Colegio de Notarios**: el Colegio Nacional de Notarios Públicos de Venezuela participa en la fiscalización disciplinaria y en la formación continua obligatoria.

#### Cláusula de continuidad

> *"Ninguna reforma al régimen del Registro Único de Inmuebles ni al Servicio Nacional del Registro Inmobiliario podrá aprobarse sin el voto de las tres cuartas partes (3/4) de la Asamblea Nacional y la ratificación mediante referéndum popular."*

La protección se alinea con la del BND, VePass, MIED-LAM, DNA-RB, RUP y CDF. **Séptimo componente** del documento con esta jerarquía constitucional máxima.

#### Métricas de éxito específicas

| Indicador | Línea base (2024) | Meta año 3 | Meta año 6 |
|-----------|-------------------|------------|-------------|
| Inmuebles inscritos en el RUI | <30% | 75% | 100% |
| Inmuebles con catastro georeferenciado | <20% | 70% | 100% |
| Transacciones registrales en línea | <5% | 80% | 100% |
| Tiempo promedio de inscripción | 30-90 días | 24 horas | 2 horas |
| Casos de doble venta detectados y bloqueados | n/d | 200/año | 50/año |
| Inmuebles regularizados por procedimiento simplificado | 0 | 500.000 | 2.000.000 |
| Informalidad inmobiliaria | ~40% | 20% | <5% |
| Recaudación anual por IBI (Impuesto sobre Bienes Inmuebles) | <USD 100 M | USD 800 M | USD 1.500 M |

---

## III.7.4. VePass — Clave Única inspirado en modelo chileno y en el SingPass singapurense

### Concepto

**VePass** es la identidad digital única de cada venezolano (RUN/RUT = número de cédula) que permite acceder a todos los servicios digitales del Estado con autenticación robusta.

inspirado en a ClaveÚnica chilena (operada por la División de Gobierno Digital del Ministerio Secretaría General de la República desde 2019) y al SingPass singapurense.

### Niveles de autenticación

| Nivel | Mecanismo | Uso típico | Tiempo de validez |
|-------|-----------|------------|-------------------|
| **VePass-Lite** | Cédula-RUT con chip NFC + PIN de 4 dígitos | Trámites cotidianos (consultar expediente, sacar certificados, votar) | Continuo |
| **VePass-Plus** | VePass-Lite + OTP por SMS / email / app | Trámites sensibles (declarar impuestos, consultar antecedentes) | 5 minutos |
| **VePass-Fuerte** | VePass-Plus + biometría (huella + rostro) | Trámites críticos (declaración jurada, poderes notariales, testamentos, ventas de vienes) | 10 minutos |
| **VePass-Firma** | VePass-Fuerte + firma electrónica avanzada con certificado emitido por el BND | Firmar documentos con validez legal, emitir documentos tributarios | 1-2-3 año (renovable) |

### Centro de ayuda y recuperación

La emisión de VePass ocurre **en el mismo trámite y la misma ventanilla** que la Cédula-RUT (proceso detallado en III.7.5). Esto evita crear una institución paralela al Registro Civil. Para los casos posteriores a la emisión inicial, el ciudadano dispone de cuatro canales de autogestión:

1. **Kioskos autoservicio VePass** instalados en las propias oficinas del Registro Civil, en alcaldías, en centros comerciales de alto tráfico, en universidades y en terminales de transporte. Cada kiosco cuenta con:
 - Lector NFC para Cédula-RUT.
 - Escáner de código QR.
 - Lector de huella dactilar.
 - Cámara para selfie (verificación facial).
 - Pantalla táctil con instrucciones en español y lenguas indígenas.
 - Impresora de recibos/comprobantes.
 - Conexión cifrada al BND.

 El kiosco permite: activar VePass, bloquear Cédula-RUT por pérdida, solicitar reposición, actualizar datos de contacto, consultar expediente, descargar certificados.

 Inspirado en el modelo de Estonia (kioscos ID-card en bibliotecas y oficinas públicas) y al modelo indio (kioscos Aadhaar en pueblos pequeños).

2. **App móvil VePass** (iOS/Android) con autenticación biométrica del dispositivo (Touch ID, Face ID, huella Android), para todas las gestiones no presenciales.

3. **Sitio web vepass.gob.ve** con VePass-Plus (OTP por SMS / email / app) para autogestión.

4. **Call center 24/7** (número corto 1-800-VEPASS) con verificación por voz + OTP, para personas que no pueden usar canales digitales.

### Canales de entrega del OTP

El OTP que utiliza VePass puede entregarse por tres canales alternativos, todos disponibles desde el momento de la emisión de la Cédula-RUT:

1. **SMS al número de celular registrado** — canal primario. Si el usuario no tiene celular o no lo ha registrado, este canal queda desactivado y se usan los demás.

2. **Email a la dirección registrada y verificada** — canal alternativo, especialmente útil para usuarios con celular prepago de saldo limitado, en zonas con cobertura intermitente, o que simplemente prefieren no usar SMS por motivos de privacidad o seguridad.

3. **TOTP generado por la App VePass** — canal más seguro y el preferido cuando es posible. Inspirado en al estándar RFC 6238 (TOTP) implementado por aplicaciones comerciales como Google Authenticator, Authy, Microsoft Authenticator y 1Password. La App VePass:

 - Comparte una clave secreta con el servidor BND al momento de la activación, almacenada en el enclave seguro del dispositivo (iOS Secure Enclave / Android StrongBox).
 - Genera un código de 6 dígitos que rota cada 30 segundos, sin necesidad de conexión a internet ni señal celular.
 - Funciona incluso en zonas sin cobertura (rural, subterráneo, exterior del país con roaming desactivado).
 - Es **resistente al SIM swap** (no depende de la SIM ni del número telefónico).
 - Es **resistente a intercepción** (los códigos nunca viajan por la red).
 - Es accesible: el usuario ve el código en la pantalla del celular incluso sin servicio.

El usuario elige el canal en la configuración de su VePass y puede activar dos o tres simultáneamente. Si un canal falla (SMS no llega, email cae en spam, app desinstalada), puede usar cualquiera de los otros. Si los tres fallan, debe acudir al canal presencial del Registro Civil.

**Por orden de preferencia**: TOTP via app > email > SMS. El SMS es el menos seguro (vulnerable a SIM swap y a interceptación SS7) pero es el más universal; por eso se mantiene como opción pero no como canal único obligatorio.

Para usuarios sin celular y sin email (caso de adultos mayores en pobreza extrema), el sistema genera automáticamente **OTP impresos en papel** al momento de la Cédula-RUT, con una cantidad limitada (típicamente 10 códigos) que se pueden usar como respaldo físico. El agotamiento del talonario requiere actualización presencial.

Para **casos complejos** que requieren presencia (fallecimiento del titular, pérdida total de la Cédula-RUT con imposibilidad de acreditar identidad por otros medios, modificaciones sustanciales), el ciudadano acude a la **oficina del Registro Civil más cercana**, que es la ventanilla natural para estos trámites. No se requiere una red separada.

### Casos especiales

- **Venezolanos en el extranjero**: VePass accesible desde el exterior con autenticación por documento diplomático + selfie + OTP al celular o email registrado.
- **Personas sin acceso digital**: mantienen la posibilidad de hacer todos los trámites presencialmente con la Cédula-RUT física.
- **Personas con discapacidad visual**: autenticación por voz + OTP.

---

## III.7.5. Sistema Nacional de Identidad (SNI)inspirado en modelo RUN/RUT chileno

El SNI unifica en un solo proceso **identidad civil, tributaria, electoral, sanitaria, educativa y biométrica**, tomando como modelo el RUN/RUT chileno y los siguientes principios:

### Nacimiento: del hospital al Registro Civil — plazos según contexto geográfico

Reforma del Registro Civil venezolano inspirado en el Registro Civil chileno (Ley 4.808 de 1930, reformada):

#### Etapa 1: Hospital — Registro de niño vivo

Todo hospital, clínica o centro de salud pública o privado donde ocurra un nacimiento debe ejecutar el siguiente **procedimiento integrado e inseparable** —no se emite Certificado de Niño Vivo sin captura previa de las muestras biológicas—:

#### Paso 1: Captura de muestras biológicas (durante el procedimiento médico estándar)

El hospital toma, en el orden establecido por el protocolo BND-Hospitalario, las siguientes muestras del recién nacido y sus padres. Estas capturas se realizan en las primeras dos horas de vida, integradas con los procedimientos médicos neonatales de rutina (APGAR, peso, talla, profilaxis):

- **Muestra de ADN del recién nacido**: hisopo de mejilla tomado por personal de enfermería capacitado, codificado y almacenado temporalmente en el kit de cadena de custodia provisto por el BND. La muestra se envía al laboratorio del Banco Nacional de ADN dentro de las 24 horas.
- **Huellas plantares del recién nacido**: ambas plantas de los pies escaneadas digitalmente con escáner de alta resolución (mínimo 500 dpi), conforme al estándar ICAO 9303 para identificación biométrica neonatal.
- **Registro fotográfico neonatal**: foto del recién nacido (primer plano + cuerpo completo), más foto de la madre y del padre si están presentes.
- **Datos biométricos de los padres**: las 10 huellas dactilares de cada progenitor (escaneadas con el mismo equipo), foto y firma electrónica capturada en tableta.

#### Paso 2: Generación y firma del Certificado de Niño Vivo

El sistema BND consolida los datos del paso 1 con los datos clínicos estándar (fecha/hora/lugar del nacimiento, sexo, peso, talla, condiciones de salud, APGAR) y genera automáticamente el Certificado de Niño Vivo.

**El sistema BND NO permite emitir el certificado si falta alguna de las muestras biológicas del paso 1.** Esta es una regla de integridad del sistema, no una opción del médico: sin ADN, sin huellas plantares, sin foto, sin biometría de los padres, no hay certificado. El bloqueo es técnico y verificable.

El médico responsable firma electrónicamente el certificado con sus credenciales VePass-Firma (certificado profesional médico), completando así el documento.

#### Paso 3: Transmisión al Registro Civil central

Una vez firmado, el certificado se transmite en tiempo real al Registro Civil central, donde queda disponible para la inscripción del recién nacido dentro de los plazos establecidos (24 horas hábiles en hospitales con oficina de registro integrada, 5 días hábiles en hospitales sin oficina).

**Plazo máximo entre el nacimiento y la emisión del certificado**: **2 horas**. Este plazo aplica al ciclo completo (captura + firma + transmisión).

#### Nacimientos fuera de un centro de salud

Cuando el parto ocurre **fuera de un hospital, clínica o centro de salud** —en el domicilio, en el trayecto, en la vía pública, en zonas rurales sin acceso inmediato, o en comunidades indígenas con parteras tradicionales—, la madre y el recién nacido deben acudir al **centro de salud más cercano** (hospital, ambulatorio, CDI, consultorio popular, hospital tipo I rural) para completar tres pasos obligatorios antes de la inscripción registral:

1. **Constatar el estado de salud de ambos**. Examen médico de la madre (control posparto, signos vitales, prevención de hemorragia, evaluación emocional) y del recién nacido (APGAR completo, peso, talla, reflejos, evaluación inicial). Este paso garantiza que la atención médica —universal y gratuita— llegue a los nacimientos extrahospitalarios, que en zonas rurales suelen ser los de mayor riesgo.

2. **Certificar que la madre ha dado a luz al niño**. El médico certifica mediante declaración jurada firmada con VePass-Firma que la paciente consultante es la madre biológica del recién nacido que presenta, y que el nacimiento ocurrió en la fecha, hora y lugar declarados por ella. Esta certificación se emite en el sistema BND con la firma electrónica profesional del médico y queda asociada al RUN futuro del niño.

3. **Emitir el Certificado de Niño Vivo** — siempre que se hayan capturado previamente las muestras biológicas del recién nacido y los datos biométricos de los padres. El sistema BND aplica el mismo bloqueo técnico que en los nacimientos hospitalarios: sin ADN + huellas plantares + foto del recién nacido + biometría de los padres, no se emite certificado. En este caso, el "lugar de nacimiento" registrado es la dirección donde ocurrió el parto (domicilio, vía pública, etc.), **no** el centro de salud donde se hizo la certificación.

**Plazo para acudir al centro de salud**: dentro de las **24 horas siguientes** al parto, por la importancia del control médico neonatal y materno.

**Excepciones documentadas** (casos donde el parto fue atendido por personal médico fuera de un establecimiento, por ejemplo en ambulancias): si la atención ocurrió en una **ambulancia o vehículo medicalizado** del Estado con médico o paramédico a bordo, ese profesional puede emitir el Certificado de Niño Vivo directamente en el sistema BND con sus credenciales VePass-Firma. La madre debe luego completar el examen en centro de salud dentro de 48 horas.

**Partos atendidos por parteras tradicionales** en comunidades indígenas: la partera, previamente registrada y certificada por el Ministerio de Salud (MS) mediante un programa específico de formación, puede emitir un **Certificado de Atención de Parto Comunitario** que sirve como antecedente para la posterior certificación médica. La madre debe acudir al centro de salud dentro de 48 horas para completar el proceso estándar. Este protocolo reconoce el valor cultural de las parteras tradicionales (wayúu, warao, pemón, etc.) y evita que su práctica sea criminalizada.



### Equipamiento y kits estandarizados para hospitales y centros de salud

Para que el protocolo anterior funcione, el BND distribuye a cada hospital, clínica, ambulatorio, CDI y centro de salud del país un **kit BND estandarizado** que incluye:

- Escáner biométrico dactilar certificado FBI IAFIS Appendix F (huellas de los padres).
- Escáner de huellas plantares neonatal (alta resolución, ≥500 dpi).
- Cámara fotográfica calibrada para registro neonatal.
- Kit de toma de muestra de ADN (hisopos estériles, tubos de almacenamiento codificados, sistema de cadena de custodia).
- Tableta con el sistema BND-Hospitalario precargado y firmado criptográficamente.
- Impresora térmica para comprobantes físicos.
- Conectividad cifrada al BND (vía VPN o enlace dedicado).

El reemplazo de consumibles (hisopos, reactivos, papel térmico) es responsabilidad del BND mediante contrato con proveedor logístico nacional. La capacitación del personal médico y de enfermería se realiza en pregrado y se renueva anualmente. La auditoría técnica del equipamiento se efectúa cada 6 meses.

### III.7.5.3. Capacidad de procesamiento de ADN en cada hospital

La captura de la muestra de ADN del recién nacido (Paso 1 del procedimiento hospitalario) es apenas la primera mitad del proceso. **La segunda mitad —el procesamiento de la muestra para generar el perfil numérico STR que se almacena en el Banco Nacional de ADN— debe ocurrir en el mismo hospital**, no en un laboratorio central distante. Esto garantiza que:

- El perfil del recién nacido esté disponible en el BND en **minutos**, no en días.
- La información esté disponible para verificación inmediata en el momento del alta hospitalaria.
- La dependencia de un laboratorio central externo no cree cuellos de botella ni vulnerabilidad política.

#### Equipamiento de procesamiento local

Para cumplir este estándar, cada hospital, clínica y centro de salud del país debe contar con una **estación de ADN rápido** compuesta por:

- **Procesador de STR rápido** (Rapid DNA Instrument). Modelo de referencia: **ANDE (Accelerated Nuclear DNA Equipment)** de ANDE Corporation, validado por el FBI para uso forense, o alternativas equivalentes (IntegenX RapidHIT, etc.). Procesa una muestra de hisopo de mejilla y genera el perfil STR en **menos de 2 horas**, con intervención mínima del operador.
- **Kit de reactivos** específico para STR multiplex de 15-20 loci (compatible con CODIS/ENFSI).
- **Conexión cifrada** al BND para transmitir el perfil en tiempo real.
- **Personal capacitado**: un técnico de laboratorio con formación de 80 horas, o un enfermero/perfusionista con capacitación adicional. La operación del equipo es automatizada: el operador coloca el hisopo, presiona "iniciar" y el equipo realiza el resto.

#### Modelo de costos e implementación

| Concepto | Detalle |
|----------|---------|
| Costo unitario del equipo | USD 250.000 - 500.000 |
| Número de hospitales a equipar | ~300 (hospitales tipo II+) + 1.000 centros de salud con versión básica |
| Inversión total estimada | USD 200-400 millones (gradual en 5 años) |
| Costo por perfil generado | USD 15-30 (reactivos + mantenimiento) |
| Throughput | 1-4 muestras por turno (8h) |
| Mantenimiento | Anual, incluido en contrato con proveedor |

inspirado en al modelo de Estonia (que equipó todos sus hospitales con capacidad de ADN rápido en 2018) y al de Singapur (que utiliza la red de hospitales públicos como nodos forenses del SPF).

#### Niveles de capacidad

- **Nivel A — Hospitales tipo III y IV** (~50 establecimientos): equipo ANDE completo + redundancia + personal dedicado.
- **Nivel B — Hospitales tipo II** (~250 establecimientos): equipo ANDE estándar + personal capacitado.
- **Nivel C — Centros de salud tipo I y ambulatorios** (~1.000 establecimientos): kits detoma + envío a hospital cercano para procesamiento (hub-and-spoke), con resultado en <24 horas vía app.

### III.7.5.4. Captura obligatoria de ADN al ingreso hospitalario para adultos sin perfil

Toda persona que ingresa a un hospital, clínica o centro de salud público o privado —por emergencia, consulta, cirugía, hospitalización, o cualquier otro motivo— y que **no tiene perfil de ADN registrado en el Banco Nacional de ADN**, debe completar el proceso detoma y procesamiento de muestra de ADN durante su permanencia en el establecimiento.

**Base legal**: esta obligación se fundamenta en el principio de interés público nacional del Banco Nacional de ADN (art. 56 CRBV reformado, parágrafo tercero del Pilar III.7) y en la necesidad de garantizar cobertura universal del registro.

#### Procedimiento

1. Al momento del ingreso, el sistema BND consulta (vía VePass-Plus del paciente o del personal de admisión) si el paciente tiene perfil de ADN registrado.
2. Si NO lo tiene, se incorpora al **protocolo detoma obligatorio**:
   - El personal de admisión o enfermería entrega el kit y explica brevemente el procedimiento.
   - El paciente firma el consentimiento con VePass-Lite o firma manuscrita (en caso de emergencia sin conciencia del paciente, se difiere al familiar o representante legal).
   - Se toma el hisopo de mejilla y se procesa en el equipo de estación de ADN rápido del hospital.
   - El perfil STR generado se carga al BND y se vincula al RUN del paciente.
   - El paciente recibe comprobante con código QR para verificación.

#### Excepciones

- **Emergencias con riesgo de vida** donde eltoma pueda retrasar la atención crítica: se difiere eltoma hasta la estabilización (24-48 horas).
- **Personas con orden judicial de notoma** (rara, en casos específicos definidos por ley).
- **Negativa expresa del paciente** sin emergencia: se documenta la negativa en el BND pero se permite el ingreso hospitalario. **Esta excepción NO aplica** para procedimientos que requieren conocer la identidad biológica del paciente (transfusiones, trasplantes, identificación forense post-mortem, etc.).
- **Pacientes ya registrados**: simplemente se consulta el BND y se actualiza la información si hay cambios.

#### Finalidad de la captura universal

La captura masiva durante atenciones hospitalarias aprovecha la oportunidad natural para completar el registro nacional sin campañas costosas niforzada. **Una persona venezolana promedio visita un hospital al menos una vez cada pocos años**, lo que garantiza que en un periodo de 10 años la cobertura del Banco Nacional de ADN supere el 95% de la población adulta.

Las finalidades legítimas del BND son:

1. **Identificación forense post-mortem y post-accidente**: restituir la identidad a cadáveres no identificados, víctimas de tragedias (incendios, naufragios, explosiones, terremotos, etc.) y desaparecidos.
2. **Compatibilidad de órganos y sangre**: facilitar la búsqueda de donantes compatibles para pacientes en lista de espera de trasplante.
3. **Investigación de filiación**: pruebas de paternidad/maternidad, reunificación familiar en contextos de migración o sustracción de menores.
4. **Apoyo a la justicia**: comparación con perfiles obtenidos en escenas del crimen (Banco de perfiles delictivos, gestionado por el CICPC conforme a la ley).

#### Usos terminantemente prohibidos del BND

Sin perjuicio de lo ya dispuesto en el artículo 56 CRBV (parágrafo primero reformado, Pilar III.7):

- **No se usará** para discriminación por etnia, raza, sexo, orientación sexual, religión u opinión política.
- **No se usará** para construir perfiles genéticos poblacionales con fines de control social.
- **No se compartirá** con aseguradoras privadas, empleadores, gobiernos extranjeros sin autorización 3/4 de la Asamblea, ni con terceros comerciales.
- **No se comercializará**: el BND es un bien público, no un activo comercial. La venta o comercialización de datos genéticos es delito penal (incorporado en el Código Penal en la reforma del Pilar III.6).

La violación de estas prohibiciones se sanciona con destitución inmediata + inhabilidad 15 años + pena de prisión 8-15 años, conforme al mismo régimen del artículo 56.

#### Continuidad del BND

> *"Ninguna reforma al régimen del Banco Nacional de Datos ni del Banco Nacional de ADN podrá aprobarse sin el voto de las tres cuartas partes (3/4) de la Asamblea Nacional y la ratificación mediante referéndum popular."*

La protección es equivalente a la del VePass, MIED-LAM, DNA-RB y RUP. **Quinto componente** del documento con esta jerarquía constitucional máxima.

#### Regla de integridad: sin perfil de ADN en el BND no se asigna RUN

La asignación del **RUN (Registro Único Nacional)** —y por extensión del RUT y de la Cédula-RUT— está **condicionada técnicamente** a la existencia del perfil de ADN del titular en el Banco Nacional de Datos. Esta regla aplica a:

- **Recién nacidos**: el sistema BND no permite asignar RUN al recién nacido si no se ha capturado y procesado previamente su muestra de ADN con resultado de perfil STR cargado.
- **Adultos sin perfil**: en el marco de la captura obligatoria al ingreso hospitalario (sección III.7.5.4), si un adulto no tiene perfil de ADN registrado y necesita asignación de RUN/RUT (caso raro de ciudadanos no inscritos en el Registro Civil), el BND captura la muestra, procesa el perfil y luego asigna el RUN.
- **Migración de adultos**: durante el proceso de migración a Cédula-RUT (sección III.7.5 sobre migración), si el adulto no tiene perfil de ADN, se le ofrece eltoma en la misma visita al Registro Civil como parte integral del proceso. La asignación del nuevo RUN/RUT y la emisión de la Cédula-RUT se completan en la misma visita.

Esta regla convierte al BND en un **sistema universal de identidad biológica** desde el primer instante de vida del venezolano. A diferencia de sistemas que sólo registran identidad administrativa, Venezuela registra identidad administrativa + biológica de manera inseparable.

Una vez completados los tres pasos, la inscripción en el Registro Civil sigue el **plazo de 5 días hábiles** descrito en el apartado siguiente, dado que estos nacimientos ocurren típicamente en zonas donde el hospital no tiene oficina de registro integrada.

### III.7.5.5. Nacidos sin vida (óbito fetal): protocolo anti-robo y trazabilidad genética

#### Definición clínica y legal

Se considera **nacido sin vida** u **óbito fetal** al producto de la concepción que, después de la expulsión o extracción completa del cuerpo de la madre, no presenta signos vitales (latido cardíaco, respiración, movimientos voluntarios), conforme a los criterios de la OMS (≥22 semanas de gestación o ≥500 gramos de peso, según CIE-10/11). Por debajo de ese umbral, la interrupción espontánea del embarazo se clasifica como **aborto espontáneo** (ver sección III.7.5.7, pendiente de redacción).

El nacido sin vida **no es persona natural** (no aplica el Art. 22 CRBV), pero el evento tiene efectos jurídicos, registrales, estadísticos y forenses que la reforma regula expresamente para cerrar una laguna histórica aprovechada por redes de robo de niños, trata y fraude.

#### El problema: el óbito fetal como vector de robo de niños

La omisión de un protocolo específico de óbito fetal ha generado una vulnerabilidad explotada por redes organizadas:

- **Sustracción hospitalaria simulada**: se declara el óbito de un recién nacido y, en realidad, el bebé vivo es sustraído y comercializado o entregado a terceros. Sin registro genético del feto, no existe manera de probar la defraudación.
- **Sustitución familiar**: se inscribe un recién nacido ajeno como hijo biológico de la madre. Sin perfil de ADN del óbito fetal previo, no hay contra-prueba forense.
- **Falsificación estadística y de beneficios**: se declaran óbitos falsos para acceder a licencias de duelo o pensiones; o se ocultan óbitos para mantener otros beneficios.

La reforma cierra esta vulnerabilidad con un **protocolo obligatorio de cuatro pasos** análogo al del nacido vivo, pero con un documento final específico: el **Certificado de Defunción Fetal (CDF)**, y —lo más importante— con la **captura obligatoria de ADN del producto** que actúa como trampa genética permanente.

#### Procedimiento obligatorio en centro de salud

Cuando el producto de la concepción es expulsado sin signos vitales, el centro de salud ejecuta el siguiente protocolo **dentro de las 2 horas siguientes** al evento:

#### Paso 1: Constatación clínica del óbito

Médico o personal de salud capacitado verifica y registra:

- Ausencia de latido cardíaco, respiración espontánea y movimientos voluntarios.
- Edad gestacional estimada (fecha última menstruación, ecografía previa).
- Peso y talla del producto.
- Circunstancias del evento: espontáneo / inducido médicamente por indicación terapéutica / interrupción voluntaria del embarazo conforme a la ley.

#### Paso 2: Captura de muestras biológicas del producto (OBLIGATORIA)

- **Muestra de ADN del producto**: hisopo de tejido fetal (preferentemente de músculo esquelético si el producto tiene >22 semanas; hisopo de membranas o cordón si es más pequeño), codificado y enviado al Banco Nacional de ADN dentro de las 24 horas.
- **Huellas plantares** si el desarrollo lo permite (escáner ≥500 dpi).
- **Registro fotográfico** del producto (escala métrica, identificación numérica visible, plano general).
- **Muestra de tejido para estudio anatomopatológico** cuando esté indicado (necropsia o estudio histopatológico), conservada conforme a la cadena de custodia.

Si la captura no es posible por el estado del producto (ej. aborto temprano <12 semanas), se documenta la imposibilidad técnica y se archiva el motivo en el BND.

#### Paso 3: Verificación de la identidad de la madre y trazabilidad

- **Confirmación del RUN de la madre** mediante VePass-Plus o, en emergencia, verificación dactilar contra el BND.
- **Cruce automático anti-fraude**: el sistema BND verifica en tiempo real tres condiciones críticas:
  1. Que **no exista una inscripción previa de óbito fetal con el mismo RUN de la madre** en los últimos 12 meses (detección de patrones anómalos de óbito recurrente).
  2. Que **no exista una inscripción previa de óbito fetal con perfil de ADN coincidente** al del producto actual (detección de clonación de identidad fetal).
  3. Que **no exista una inscripción de nacido vivo previa** de la misma madre cuyo ADN coincida con el del producto actual (detección de reinscripción fraudulenta de un bebé ya registrado).
- **Verificación de paternidad declarada**: si se declara un progenitor varón, se capturan sus 10 huellas dactilares y se vinculan al registro del óbito fetal.

Cualquiera de las tres condiciones que arroje coincidencia **dispara una alerta automática** a la DNA-RB y al Ministerio Público, con bloqueo de la inscripción hasta investigación.

#### Paso 4: Emisión del Certificado de Defunción Fetal (CDF)

El sistema BND genera el **Certificado de Defunción Fetal (CDF)** con la siguiente información:

- RUN de la madre.
- Fecha, hora y lugar del óbito.
- Edad gestacional, peso y sexo (si es determinable).
- Causa inmediata de muerte fetal (siguiendo CIE-10/11).
- Tipo de evento: espontáneo / inducido médicamente / IVE conforme a ley.
- Número de protocolo BND.
- **Perfil de ADN del producto** (vinculado al Código de Identificación Fetal) — o indicación "no viable para tipificación" si no fue posible la captura.
- Identificación del médico certificador (VePass-Firma).
- Código QR + URL de verificación.

**El CDF es firmado con VePass-Firma por el médico responsable y transmitido en tiempo real al Registro Civil central**, donde se inscribe como **acta de defunción fetal** dentro de las 24 horas hábiles.

#### Inscripción registral y efectos jurídicos

El Registro Civil inscribe el óbito fetal con las siguientes características:

- **No asigna RUN** al producto (no hay persona natural). En su lugar, asigna un **Código de Identificación Fetal (CIF)** interno del BND.
- El CIF se vincula al RUN de la madre y queda marcado como **"cerrado"** en el BND.
- **No genera Cédula-RUT** ni inscripción en el Registro Electoral.
- **Sí genera**: registro estadístico vital, habilitación de licencia de duelo materno/paterno conforme a la LOTTT (8 días para la madre, 3 días para el padre), acceso a servicios de salud mental perinatal, exención de cuotas de recuperación hospitalaria.

#### La trampa genética: por qué la captura de ADN es irrevocable

El BND retiene el perfil de ADN del producto y de la madre **por 75 años después del evento** (plazo general de retención del BND). Este registro opera como una **trampa genética permanente** contra el fraude y la trata:

1. **Imposibilidad de reinscribir un bebé robado como "hijo biológico"**: si en el futuro cualquier persona intenta registrar un recién nacido con un perfil de ADN que ya está archivado como óbito fetal, el cruce en el BND detecta la coincidencia y **bloquea la inscripción automáticamente**. El sistema exige entonces resolución judicial previa.
2. **Verificación forense de filiación futura**: si un adulto reclama ser descendiente biológico de la madre y existe discrepancia con la inscripción de óbito fetal previa, el cruce de ADN resuelve el caso sin ambigüedad, identificando al producto sustraído o al impostor.
3. **Detección de patrones de trata**: el BND y la DNA-RB pueden identificar redes de trata mediante análisis de clusters: óbitos fetales reiterados en una misma zona geográfica o centro de salud, o con madres diferentes vinculadas al mismo personal médico o la misma oficina de registro.
4. **Cadena de custodia probatoria**: si un funcionario del Registro Civil, médico o personal administrativo inscribe un nacido vivo cuyo ADN coincide con un óbito fetal archivado, queda registrado el intento con fecha, hora, RUN del funcionario y dirección IP. La responsabilidad penal queda determinada de oficio.

#### Excepciones y casos especiales

- **Parto múltiple donde algunos bebés sobreviven y otros nacen sin vida**: se aplica el protocolo de óbito fetal **solo a los productos sin vida**, mientras que los nacidos vivos siguen el protocolo estándar de la sección III.7.5. El evento se documenta como un parto múltiple con un identificador único en el BND que vincula a todos los productos.
- **Óbito fetal en domicilio o vía pública**: la madre debe acudir al centro de salud más cercano dentro de las **6 horas** con el producto, para completar el protocolo. El centro de salud certifica el óbito fetal y emite el CDF. Si el estado del producto impide la captura de ADN, se documenta y se cruza con la base de desaparecidos para descartar sustracción previa.
- **Objeción de conciencia del médico**: la certificación del óbito fetal es un acto administrativo de salud pública que **no admite objeción de conciencia** (la objeción aplica al procedimiento que causa el óbito, no a la certificación del hecho consumado). El médico que se niegue comete falta administrativa sancionable con suspensión de 30 a 90 días e inhabilitación.
- **Negativa de la madre a la captura de ADN**: se documenta la negativa y se emite el CDF sin perfil genético del producto. Esta circunstancia queda registrada en el BND como **"registro sin perfil de ADN por negativa del titular"** y se reporta en el informe trimestral anonimizado de la SPDP sobre integridad del sistema. **Excepción**: si existen indicios racionales de comisión de delito (sustracción de menores, trata, fraude), la negativa activa procedimiento judicial de captación forzada conforme a orden del TSJ.
- **Madre fallecida en el evento**: si la madre muere durante o inmediatamente después del parto, la captura de muestras del producto se realiza con autorización del médico forense, y el CDF se emite junto con el acta de defunción materna, vinculados en el BND bajo un identificador de evento único.

#### Marco constitucional

Reforma al artículo 56 CRBV adicionando:

> *"El Estado garantiza la trazabilidad genética de todo producto de la concepción nacido sin vida, mediante la captura obligatoria de muestras biológicas del producto y de la madre en el momento del evento. El Certificado de Defunción Fetal es un documento público con valor registral, estadístico y forense. La omisión, alteración o falsificación del Certificado de Defunción Fetal o de los perfiles de ADN asociados será sancionada conforme a la ley penal con pena de ocho (8) a quince (15) años de prisión, sin perjuicio de las responsabilidades administrativas y civiles."*

#### Cláusula de continuidad

> *"Ninguna reforma al régimen del Certificado de Defunción Fetal ni al protocolo de óbito fetal podrá aprobarse sin el voto de las tres cuartas partes (3/4) de la Asamblea Nacional y la ratificación mediante referéndum popular."*

La protección se alinea con la del BND, VePass, MIED-LAM y DNA-RB. **Sexto componente** del documento con esta jerarquía constitucional máxima.

#### Métricas de éxito específicas

| Indicador | Línea base (2024) | Meta año 3 | Meta año 6 |
|-----------|-------------------|------------|-------------|
| Óbitos fetales con CDF emitido | <40% | 95% | 100% |
| Óbitos fetales con perfil de ADN capturado | <10% | 85% | 98% |
| Casos detectados de reinscripción fraudulenta | n/d | 50/año | 10/año |
| Redes de trata desarticuladas gracias al cruce BND | n/d | 5/año | 15/año |
| Tiempo promedio entre óbito y emisión del CDF | Variable | <4 horas | <2 horas |

---

#### Etapa 2: Inscripción inmediata en el Registro Civil

El padre y la madre (o uno de ellos) deben inscribir al recién nacido en el Registro Civil respetando los plazos establecidos según el contexto geográfico del hospital donde ocurrió el nacimiento:

**Plazo de 24 horas hábiles** — aplicable cuando el hospital, clínica o centro de salud cuenta con **oficina del Registro Civil integrada** (modelo inspirado en al Registro Civil chileno, presente en las principales maternidades del país). En este caso la inscripción ocurre antes del egreso médico o, como máximo, al día siguiente.

**Plazo de 5 días hábiles** — aplicable cuando el hospital **no cuenta con oficina del Registro Civil integrada**, lo cual ocurre principalmente en:
 - Hospitales rurales Tipo I y Tipo II sin oficina de registro.
 - Clínicas privadas que aún no han integrado el sistema.
 - Partos domiciliarios o en centros de salud comunitarios sin infraestructura registral.

En estos casos, los padres deben acudir a la oficina del Registro Civil más cercana (la del municipio cabecera o la que figure como referencia para su parroquia) **dentro de los 5 días hábiles siguientes al nacimiento**. Este plazo reconoce las realidades de la geografía venezolana —especialmente en zonas rurales, amazónicas e insulares— y evita imponer cargas imposibles a familias que ya están en situación vulnerable.

**Inscripción en línea** — disponible para ambos casos cuando ambos padres cuentan con VePass-Fuerte (autenticación robusta con biometría), sin necesidad de presencia física.

La inscripción:

1. **Asigna el RUN (Registro Único Nacional)** al recién nacido, número que será también su **RUT (Registro Único Tributario)** desde el nacimiento.
2. **Genera la Cédula-RUT electrónica** (ver III.7.6), emitida físicamente al cumplir los 5 años (modelo inspirado en Chile) o antes si los padres lo requieren.
3. **Crea automáticamente** las afiliaciones iniciales:
 - Sistema Único de Salud (afiliación como beneficiario de los padres hasta mayoría de edad)
 - Ministerio de Educación (preinscripción en el sistema educativo)
 - IVSS (seguro social contributivo desde que tenga primer ingreso)
 - Registro Electoral (preinscripción; voto habilitado a los 18 años)
4. **Asocia la muestra de ADN** del recién nacido al RUN y al árbol genealógico familiar.

La obligación de inscribir es **responsabilidad administrativa de los padres**, con plazos distintos según el contexto. El incumplimiento injustificado genera:

- **Multa simbólica** (1 UT, ~USD 5) por inscripción tardía una vez vencido el plazo aplicable.
- **Activación automática de protección integral del recién nacido** por el Consejo de Protección del Niño en caso de reincidencia o sospecha de desprotección.
- **Bloqueo de beneficios administrativos posteriores** (becas, ayudas familiares) hasta regularizar la inscripción.

El plazo de **5 días hábiles** NO se aplica en zonas urbanas con hospitales grandes que tengan Registro Civil integrado — ahí rige el de 24 horas. La diferenciación geográfica se publica anualmente en un **listado oficial de hospitales con/sin oficina de registro integrada**, actualizado por el Servicio Nacional de Identificación y disponible en tiempo real en vepass.gob.ve y en la app móvil.

#### Etapa 3: Cédula-RUT

Una vez inscrito, el recién nacido tiene:

- **RUN** (registro civil)
- **RUT** (registro tributario, mismo número)
- **Pre-Cédula-RUT** digital (asociada al VePass de los padres)
- **Cédula-RUT física** emitida al cumplir 5 años (modelo inspirado en Chile)

### III.7.5.6. Algoritmo de cálculo del dígito verificador (DV) del RUN/RUT

El dígito verificador (DV) es un dígito adicional calculado mediante el algoritmo **Módulo 11** que se agrega al número de cédula existente para formar el RUN/RUT completo. Este DV permite:

- Detectar errores de digitación en cualquier consulta o transcripción.
- Validar la integridad del número sin necesidad de consultar la base de datos.
- Mantener la continuidad del número de cédula que los ciudadanos ya conocen y usan (V-NNNNNNNN → NNNNNNNN-DV).

El algoritmo se aplica de manera uniforme a todos los números de cédula venezolana y es el **único método válido** para calcular el DV. Cualquier sistema público o privado que manipule RUN/RUT debe utilizar exactamente esta especificación; las variantes están prohibidas por la ley penal (ver III.7.13 riesgos asociados a errores de validación).

#### Algoritmo Módulo 11 (especificación vinculante)

Para calcular el DV de un número `N` (sin prefijo `V`/`E`/`J` ni separadores):

1. **Revertir el número**: invertir el orden de los dígitos de `N`, de manera que el dígito más a la derecha quede primero.
2. **Aplicar multiplicadores cíclicos**: comenzando desde el dígito más a la derecha (ahora en posición 0 del número invertido), multiplicar cada dígito por un multiplicador que cicla entre **2, 3, 4, 5, 6, 7** en ese orden, y se reinicia al llegar a 7.
3. **Sumar los productos**: `S = Σ (dígito_i × multiplicador_i)`.
4. **Calcular el módulo**: `r = S mod 11`.
5. **Obtener el DV**: `DV = 11 - r`.
6. **Casos especiales**:
   - Si `DV = 11`, entonces `DV = "0"` (cero).
   - Si `DV = 10`, entonces `DV = "K"`.
   - En otro caso, `DV` es el dígito numérico correspondiente (0-9).

#### Implementación de referencia en Python

```python
def calcular_dv(numero):
    """
    Calcula el dígito verificador (DV) del RUN/RUT venezolano
    mediante el algoritmo Módulo 11 (Pilar III.7.5.6 de la Reforma).

    Args:
        numero: str o int con el número base (sin prefijo V/E/J
                ni separadores).

    Returns:
        str con el DV: dígito 0-9, "0" si el cálculo da 11,
        o "K" si da 10.

    Ejemplos:
        >>> calcular_dv("19907563")
        '2'
        >>> calcular_dv(12345678)
        '5'
        >>> calcular_dv("1")
        '9'
    """
    n = str(numero).replace(".", "").replace("-", "").replace(" ", "").strip()
    if not n.isdigit():
        raise ValueError(f"Número inválido: {numero!r}")
    suma = 0
    multiplicador = 2
    for digito in reversed(n):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    residuo = suma % 11
    dv_num = 11 - residuo
    if dv_num == 11:
        return "0"
    if dv_num == 10:
        return "K"
    return str(dv_num)


def validar_run(run_completo):
    """
    Valida aritméticamente un RUN/RUT completo (NNN-DV).

    Returns:
        True si el DV es correcto, False en caso contrario.

    Ejemplos:
        >>> validar_run("19907563-2")
        True
        >>> validar_run("19907563-3")
        False
    """
    partes = str(run_completo).strip().split("-")
    if len(partes) != 2:
        return False
    numero, dv_provisto = partes[0], partes[1].upper()
    try:
        return calcular_dv(numero) == dv_provisto
    except ValueError:
        return False


if __name__ == "__main__":
    # Casos de prueba
    casos = ["19907563", "12345678", "10000000", "99999999", "1", "5"]
    print(f"{'Número base':<15} {'RUN/RUT completo':<20} {'¿Válido?'}")
    print("-" * 50)
    for n in casos:
        dv = calcular_dv(n)
        run = f"{n}-{dv}"
        print(f"{n:<15} {run:<20} {validar_run(run)}")

    # Demostración detallada para 19907563
    print("\nDemostración detallada para 19907563:")
    n = "19907563"
    print(f"  Dígitos (derecha a izquierda): {list(reversed(n))}")
    mult_cycle = []
    m = 2
    for _ in n:
        mult_cycle.append(m)
        m = m + 1 if m < 7 else 2
    print(f"  Multiplicadores cíclicos:        {mult_cycle}")
    productos = [int(d) * mult_cycle[i] for i, d in enumerate(reversed(n))]
    print(f"  Productos:                       {productos}")
    print(f"  Suma:                            {sum(productos)}")
    print(f"  Suma mod 11:                     {sum(productos) % 11}")
    print(f"  DV = 11 - residuo:               {11 - (sum(productos) % 11)}")
    print(f"  RUN/RUT final:                   {n}-{calcular_dv(n)}")
```

#### Salida esperada al ejecutar el bloque anterior

```
Número base     RUN/RUT completo     ¿Válido?
--------------------------------------------------
19907563        19907563-2           True
12345678        12345678-5           True
10000000        10000000-8           True
99999999        99999999-9           True
1               1-9                  True
5               5-1                  True

Demostración detallada para 19907563:
  Dígitos (derecha a izquierda): ['3', '6', '5', '7', '0', '9', '9', '1']
  Multiplicadores cíclicos:        [2, 3, 4, 5, 6, 7, 2, 3]
  Productos:                       [6, 18, 20, 35, 0, 63, 18, 3]
  Suma:                            163
  Suma mod 11:                     9
  DV = 11 - residuo:               2
  RUN/RUT final:                   19907563-2
```

#### Ejemplo de cálculo paso a paso

Para el número de cédula **19907563** (8 dígitos):

| Posición desde la derecha | Dígito | × Multiplicador | = Producto |
|---|---|---|---|
| 0 | 3 | × 2 | 6 |
| 1 | 6 | × 3 | 18 |
| 2 | 5 | × 4 | 20 |
| 3 | 7 | × 5 | 35 |
| 4 | 0 | × 6 | 0 |
| 5 | 9 | × 7 | 63 |
| 6 | 9 | × 2 (ciclo reinicia) | 18 |
| 7 | 1 | × 3 | 3 |
| **Suma total S** | | | **163** |

- Residuo: `r = 163 mod 11 = 9` (pues 11 × 14 = 154, y 163 − 154 = 9)
- DV = `11 − 9 = 2`

**RUN/RUT resultante: 19907563-2**

#### Validación en cualquier sistema

Cualquier sistema (público o privado) puede validar un RUN/RUT aplicando el mismo algoritmo al número sin DV y comparando el DV calculado con el DV provisto:

```
DV_calculado == DV_provisto   →  RUN válido (existe o tiene formato correcto)
DV_calculado != DV_provisto   →  RUN inválido (error de digitación o RUN inexistente)
```

La validación es **aritmética pura**: no requiere consultar la base de datos. Por esta razón, el algoritmo se utiliza en formularios web, sistemas de facturación, trámites bancarios, declaraciones tributarias y cualquier punto donde se ingrese un RUN/RUT.

#### Casos especiales de migración

- **Cédulas con menos de 8 dígitos** (formato histórico, ej. V-NNNNNNN de 7 dígitos o V-NNNNNN de 6): se completan con ceros a la izquierda hasta completar 8 dígitos antes de aplicar el algoritmo. Ejemplo: cédula histórica "V-12345" → número base "00012345" → DV calculado.
- **Cédulas con guiones o puntos** (separadores históricos, ej. "1.234.567"): se eliminan todos los caracteres no numéricos antes de aplicar el algoritmo.
- **Cédulas con más de 8 dígitos** (formato moderno, hasta 9 dígitos): se aplican los multiplicadores cíclicos tal cual; el algoritmo opera sobre el número entero sin truncar.
- **Cédulas de extranjería** (E-NNNNNNNN): se calcula DV sobre la parte numérica; el prefijo "E" se conserva como clasificación pero no forma parte del RUN/RUT para el BND (el RUN numérico es el mismo que el de un nacional).
- **RIF preexistente** (V-NNNNNNNN-DV_ANTERIOR para personas naturales, J-NNNNNNNN para personas jurídicas): durante la migración se concilian tres identificadores:
  1. Si el RIF tiene el mismo número base que la cédula, el RUN adopta ese número y se calcula el DV con este algoritmo.
  2. Si el RIF tiene un número distinto al de la cédula, se concilia con prioridad al número de cédula; las discrepancias se resuelven con auditoría de la DNA-RB.
  3. Para personas jurídicas (RIF J-XXXXX), el RUN de la empresa se calcula aplicando el mismo algoritmo sobre el número base, manteniendo el prefijo "J" para todas las interacciones del RUI y del SENIAT.
- **Cédulas nuevas asignadas por el sistema** (recién nacidos o extranjeros naturalizados): el Servicio Nacional de Identificación asigna un número correlativo de 8 dígitos y calcula el DV mediante este algoritmo antes de emitir la Cédula-RUT.
- **Personas con dos cédulas históricas** (caso excepcional): la DNA-RB determina cuál es la cédula canónica, regulariza la situación y calcula el DV sobre el número canónico.

#### Implementación de referencia pública

La Superintendencia de Protección de Datos Personales (SPDP) publica la **implementación de referencia** del algoritmo en código abierto (Python, JavaScript, Java, PHP) bajo licencia MIT, en el repositorio público `github.com/ve-pass/dv-algorithm`. Esta implementación:

- Es la **única canónica** y debe ser utilizada por todos los sistemas públicos y privados que manipulen RUN/RUT.
- Incluye **pruebas unitarias exhaustivas** con casos de borde documentados.
- Es auditada anualmente por la SPDP y por veeduría internacional independiente.

Cualquier desviación de la implementación de referencia (algoritmo paralelo, orden de multiplicadores alterado, tratamiento distinto de DV=10 o DV=11) constituye **incumplimiento técnico sancionable** conforme al régimen de protección de datos y, si produce daño a tercero, delito de fraude informático conforme al Código Penal reformado por el Pilar III.6.

#### Tabla de búsqueda rápida (respaldo analógico)

Para facilitar la verificación por terceros sin acceso a dispositivo digital, la SPDP publica una **tabla impresa de búsqueda de DV** para los números base del 1 al 10.000.000, distribuida gratuitamente en alcaldías, oficinas del Registro Civil, notarías y bancos. La tabla es **opcional** (la validación algorítmica es preferible) pero sirve de respaldo para:

- Ciudadanos sin acceso digital en zonas rurales.
- Verificación visual en transacciones notariales.
- Auditorías físicas de campo.

#### Relación con otros componentes del BND

| Componente | Uso del DV |
|---|---|
| **SNI** | Validación aritmética de cada RUN ingresado en cualquier trámite |
| **VePass** | El RUN+DV es el identificador del usuario en todas las plataformas |
| **RUP** | Cada título profesional se vincula al RUN+DV del titular |
| **RUI** | Cada operación registral cita el RUN+DV de compradores, vendedores y titulares |
| **Banco Nacional de ADN** | Muestras y perfiles vinculados al RUN+DV |
| **CDF (III.7.5.5)** | El CDF cita el RUN+DV de la madre; el CIF del producto se vincula al RUN+DV materno |
| **Cédula-RUT** | Lleva impreso el RUN+DV en la tarjeta |
| **LOPD (III.7.8)** | El DV es dato no sensible y puede circular libremente para validación |

#### Cláusula de continuidad

> *"La fórmula del algoritmo Módulo 11 aquí establecida, incluyendo el orden de los multiplicadores (2, 3, 4, 5, 6, 7 con reinicio), el cálculo del residuo, las reglas especiales para DV=10 ('K') y DV=11 ('0'), y el formato RUN-DV, forman parte del núcleo constitucional del régimen de identificación nacional y gozan de la misma jerarquía de protección que el RUN/RUT mismo. Ninguna reforma podrá alterar el algoritmo sin reforma constitucional aprobada por tres quintos (3/5) de la Asamblea Nacional y ratificada mediante referéndum popular."*

La protección se alinea con la del BND, VePass, MIED-LAM, DNA-RB, RUP, CDF y RUI. **Octavo componente** del documento con esta jerarquía constitucional máxima.

---

### Migración de adultos

Los venezolanos adultos ya inscritos en el viejo sistema (cédula SAIME + RIF SENIAT) son **migrados automáticamente al SNI** mediante un proceso gradual:

1. **Conciliación de bases**: SENIAT y SAIME cruzan información para asignar a cada ciudadano un RUN/RUT único, preservando el número de cédula existente y calculando el dígito verificador (DV) mediante el algoritmo de la sección III.7.5.6. Los casos de duplicidad se resuelven con auditoría de la DNA-RB.
2. **Emisión progresiva de Cédula-RUT**: durante los primeros 18 meses de la reforma, todos los venezolanos deben obtener su nueva Cédula-RUT con QR + NFC + chip biométrico. El costo es asumido por el Estado.
3. **Activación biométrica obligatoria**: la nueva Cédula-RUT requiere registro presencial de las 10 huellas dactilares, foto y firma electrónica en cualquier oficina del Registro Civil.
4. **Caducidad de documentos anteriores**: 36 meses después del inicio del proceso, la antigua cédula SAIME deja de ser válida para todos los efectos.

### Marco constitucional del SNI

Reforma al artículo 56 CRBV (identidad), que incorpora un nuevo parágrafo único y un numeral adicional sobre **usos prohibidos**:

> *"Toda persona tiene derecho a un nombre propio, al apellido del padre y de la madre, y a una identidad única, irrepetible y permanente asignada por el Estado venezolano desde el nacimiento. La identidad es unitaria: el Registro Único Nacional, el Registro Único Tributario, el registro electoral y los registros sectoriales convergen en una sola plataforma interoperable administrada por el Servicio Nacional de Identificación con VePass.*
>
> *El Estado garantiza el derecho a la intimidad, a la privacidad y a la protección de los datos personales conforme a la ley. Toda persona tiene derecho a acceder a sus propios datos y a conocer el uso que se hace de ellos.*
>
> *Parágrafo primero. Se prohíbe terminantemente el uso de los datos del Sistema Nacional de Identidad, del VePass, del Registro Único Nacional y de cualquier registro público interoperable, para fines políticos, proselitistas, discriminatorios o de persecución. En particular, se prohíbe:*
>
> *(a) condicionar la prestación de servicios públicos, beneficios sociales, acceso a cargos públicos, inscripción en programas sociales, asignación de viviendas, becas, créditos, pensiones, jubilaciones, permisos, licencias o cualquier otra actuación administrativa, a la afiliación, militancia, simpatía, voto u opinión política del solicitante;*
>
> *(b) construir, mantener, actualizar, compartir, transferir o utilizar bases de datos, perfiles, listas, padrones o cualquier registro con el propósito de perseguir, hostigar, intimidar, excluir, estigmatizar o restringir derechos de personas por motivos de su opinión política, afiliación partidista, religión, origen étnico, sexo, orientación sexual, identidad de género, discapacidad, condición socioeconómica o cualquier otra categoría protegida por la Constitución;*
>
> *(c) transmitir, ceder, vender, regalar o permitir el acceso a datos de identidad —incluyendo RUN/RUT, datos biométricos, fotografía, domicilio, huella dactilar, ADN o cualquier otro dato almacenado— a partidos políticos, organizaciones con fines políticos, agrupaciones civiles con orientación política, gobiernos extranjeros sin autorización conforme al artículo 134-B, o cualquier tercero no autorizado;*
>
> *(d) crear padrones paralelos al Registro Civil o al Registro Electoral con fines políticos, clientelares o de control social.*
>
> *Parágrafo segundo. La persona natural o la autoridad investida de poder público que utilice los datos del Sistema Nacional de Identidad, del VePass, del Registro Único Nacional, del Registro Único Tributario o de cualquier registro público interoperable para los fines prohibidos en el parágrafo primero será, sin perjuicio de otras responsabilidades civiles y administrativas:*
>
> *(i) Destituida de manera inmediata de su cargo, función o comisión, con inhabilitaciónpolítica por quince (15) años para el ejercicio de cualquier cargo público. La destitución será ejecutada por la autoridad competente dentro de las cuarenta y ocho (48) horas siguientes a la verificación del hecho, sin posibilidad de suspensión de los efectos del acto administrativo.*
>
> *(ii) Juzgada penalmente conforme a la Ley Orgánica contra la Delincuencia Organizada y Financiamiento al Terrorismo, por el delito de **uso indebido de datos de identidad con fines políticos o discriminatorios**, con pena de prisión de ocho (8) a quince (15) años, multa equivalente al triple del daño patrimonial causado o de la ventaja obtenida, e inhabilitaciónpolítica definitiva. La acción penal es pública, de oficio y no requiere instancia de parte.*
>
> *Parágrafo tercero. Corresponde a la Dirección Nacional Anticorrupción "Rómulo Betancourt" (DNA-RB), en coordinación con la Superintendencia de Protección de Datos Personales (SPDP) y el Ministerio Público, la investigación y persecución de los hechos previstos en este artículo. Las denuncias podrán ser presentadas por cualquier persona mediante el VePass, sin necesidad de asistencia letrada. La identidad del denunciante será protegida mediante protocolo especial de la SPDP."*

### III.7.5.7. Marco institucional del Servicio Nacional de Identificación: transformación del SAIME e integración del Registro Civil

El Servicio Nacional de Identificación (SNI) que opera el BND y emite la Cédula-RUT no surge de la nada: se construye sobre el andamiaje institucional del **Servicio Administrativo de Identificación, Migración y Extranjería (SAIME)** y sobre las funciones registrales hoy dispersas entre el Registro Civil dependiente del Ministerio del Poder Popular para Relaciones Interiores, Justicia y Paz, los Tribunales de Municipio y el Consejo Nacional Electoral. Esta subsección documenta el origen histórico, las críticas documentadas, la decisión de reforma y el cronograma de transición.

#### Origen histórico del SAIME

El sistema venezolano de identificación civil tiene sus raíces en la década de 1940, cuando el control de identidad se vinculó a funciones de seguridad y policía de migración en el contexto de la Segunda Guerra Mundial.

| Año | Norma | Gaceta Oficial | Efecto institucional |
|---|---|---|---|
| 1924 | Propuesta del Dr. Guillermo Pablo Soublette al Ministerio de Relaciones Interiores | — | Idea del carnet de identidad inspirada en el sistema inglés |
| 1938 | Ley del Servicio Nacional de Seguridad | — | Gabinete Central de Identificación |
| 1941 | Primera cédula para extranjeros (Friedrich Wachter Fischer, N-0001) | — | Inicio de la cedulación |
| 1942 | Primera cédula para venezolanos (Gral. Isaías Medina Angarita, N-001) | — | Inicio de la cedulación de nacionales |
| 1946 | Decreto Ley N° 367 | — | Dirección de Identificación dependiente del Ministerio de Relaciones Interiores |
| 1946 | Decreto N° 409 | — | Reglamento del Servicio Nacional de Identificación (derogado en 1971) |
| **1971** | **Ley Orgánica de Identificación** | **29.594** | Deroga Decreto 409; crea la Fiscalía General de Cedulación bajo fiscalización del Consejo Supremo Electoral |
| 1972 | Inicio de la cedulación a color | — | Mayor seguridad documental |
| 1992 | Decreto N° 2.487 | 35.027 | División en Oficina Nacional de Identificación (ONI) + Dirección General Sectorial de Extranjería (DEX) |
| 2000-2003 | Fusión temporal como Dirección de Identificación y Extranjería | — | Reversión de la división |
| 2004 | Nace ONIDEX (Oficina Nacional de Identificación y Extranjería) | — | Fusión definitiva |
| **9 junio 2009** | **Decreto N° 6.733** (Reglamento Orgánico del Ministerio del Poder Popular para Relaciones Interiores y Justicia) | **39.196** | ONIDEX pasa a denominarse **SAIME**, como servicio desconcentrado sin personalidad jurídica, con plena capacidad de gestión presupuestaria, administrativa y financiera |
| 2013 | Inicio del proceso de reformulación de la estructura organizativa funcional del SAIME | — | Iniciada por el MPPREIJ |
| **Diciembre 2015** | Aprobación formal de la nueva estructura organizativa y funcional del SAIME | — | Consolida la estructura legal del organismo bajo el marco del Decreto N° 6.733 |

El SAIME queda formalmente establecido entonces como un **servicio desconcentrado**, sin personalidad jurídica propia pero con autonomía operativa (gestión presupuestaria, administrativa y financiera), adscrito al **Ministerio del Poder Popular para Relaciones Interiores, Justicia y Paz (MPPREIJ)** —denominación vigente del Ministerio del Interior al 2026—. La consolidación orgánica de 2015 es la base administrativa sobre la cual opera al momento de la presente reforma.

#### Críticas documentadas y causa-raíz de la reforma

El SAIME atraviesa una crisis institucional documentada por la prensa, las ONG y los propios usuarios. Las cuatro patologías que justifican su transformación:

1. **Ineficiencia operativa estructural**: en 2017 el SAIME emitió aproximadamente 300.000 pasaportes de 1,8 a 3 millones de solicitudes (cumplimiento del 10-17%). La plataforma en línea lanzada en 2017 para "garantizar entrega en 72 horas con tarifas dobles" se cayó reiteradamente.
2. **Corrupción y extorsión sistémicas**: Transparencia Venezuela consignó más de 100 denuncias de venezolanos que no logran obtener su pasaporte en los plazos reglamentarios, muchas asociadas a cobros irregulares de funcionarios. El diario *El Estímulo* documentó el modus operandi de "las mafias del SAIME".
3. **Discontinuidad de trámites**: sin justificación oficial, expedientes se paralizan durante meses o se pierden definitivamente, lo que obliga a los usuarios a recurrir a "gestores" informales o al mercado clandestino de Facebook (grupos con miles de seguidores que ofrecen cédulas, pasaportes y actas a precios dolarizados, muchos fraudulentos).
4. **Apatridia inducida**: con un éxodo de 7,13 millones de venezolanos (plataforma R4V de Naciones Unidas, 2023), la ausencia de sedes consulares eficientes, los costos dolarizados (pasaporte nuevo ~USD 200-216; prórroga ~USD 100-108) y la exigencia de presencia física en Venezuela han producido un creciente número de niños y adolescentes sin documentación, con efectos sobre el acceso a salud, educación y empleo.

La causa-raíz es la combinación de **baja autonomía funcional + dependencia política del Ministerio del Interior + ausencia de meritocracia en el ingreso + opacidad presupuestaria + plataforma tecnológica subcontratada a vendors extranjeros sin auditoría pública** (la plataforma SAIME fue administrada entre 2011 y 2022 por una empresa estatal extranjera, y desde julio de 2022 por la firma argentina Exclé C.A., esta última sancionada por la OFAC de EE.UU. en diciembre 2020).

#### Decisión de reforma: transformación, no abolición

La reforma **transforma** el SAIME en lugar de abolirlo, para preservar el capital institucional acumulado (83 oficinas territoriales, 42 oficinas de migración, experiencia del personal, expediente documental histórico) mientras se sustituye su arquitectura jurídica, su dependencia política, su régimen de personal y su plataforma tecnológica. La transformación se ejecuta mediante tres actos legislativos:

| Norma vigente | Reforma propuesta |
|---|---|
| Ley Orgánica de Identificación (1971, Gaceta Oficial 29.594) | **Derogada expresamente**. Se dicta la **Ley Orgánica del Servicio Nacional de Identificación y del Servicio Nacional de Migración y Extranjería** como cuerpo legal único. |
| Decreto N° 6.733 (2009, Gaceta Oficial 39.196) — creación del SAIME | **Derogados expresamente los artículos 68 a 74 de la Sección IX** ("Servicio Administrativo de Identificación, Migración y Extranjería"). La nueva ley crea el SNI y el SNMEx como personas jurídicas públicas con autonomía funcional, presupuestaria y administrativa. Ver texto íntegro del Decreto 6.733 en `borrador_reforma/2026/anexos/gaceta_39196_decreto_6733.pdf` (descargado de Gaceta Oficial 39.196 del 9 de junio de 2009). | |
| Estructura orgánica aprobada en diciembre 2015 | **Sustituida** por la nueva estructura orgánica del SNI. La transición del personal se rige por el régimen específico descrito más adelante. |
| Atribuciones dispersas del Registro Civil (Ministerio del Interior + Tribunales + CNE) | **Centralizadas técnicamente** en el SNI. Las funciones jurisdiccionales (inscripción, rectificación, declaración de ausencia, adopción) permanecen en el Poder Judicial conforme al régimen procesal civil. |
| Plataforma tecnológica contratada a vendors extranjeros (Albet, Exclé C.A.) | **Reemplazada** por la plataforma del BND operada en Guri-1/2/3, con código abierto auditado por la SPDP y la comunidad académica nacional. |

#### Estructura orgánica del Servicio Nacional de Identificación (SNI)

El SNI es una **persona jurídica pública autónoma**, adscrita al Ministerio del Poder Popular para Relaciones Interiores, Justicia y Paz (denominación sujeta a la reforma ministerial del Pilar III.2), con patrimonio propio y autonomía funcional, presupuestaria, administrativa, técnica y de gestión. Su estructura:

- **Director General**:
  - Designado por **concurso público de antecedentes y oposición** ante un jurado mixto (5 miembros: 2 del Ministerio del Interior, 2 del Poder Judicial, 1 de la Academia de Ciencias), con ratificación de la Asamblea Nacional por **3/5**.
  - Período: **7 años**, no reelegible, no coincidente con el ciclo presidencial (primera integración escalonada).
  - Remoción sólo por **causa grave** (sentencia firme, incumplimiento reiterado, conflicto de interés no resuelto) con **3/5 de la Asamblea**.
  - **Incompatibilidades absolutas**: no ser miembro activo de partidos políticos ni haberlo sido en los últimos 8 años; no parentesco hasta 4° grado con el Presidente, Vicepresidente, Ministros del Interior/Justicia/Defensa o directores de órganos del Poder Ciudadano; no haber sido contratista del Estado en los últimos 5 años.
  - **Veeduría internacional**: el Director General es evaluado cada 2 años por un panel de 3 expertos internacionales en identificación civil y protección de datos (modelo del Comité de Supervisión de la Agencia Española de Protección de Datos).
- **Subdirecciones (4)**:
  1. **Subdirección de Identificación Civil**: emisión y renovación de Cédula-RUT, captura biométrica, operación de kioskos autoservicio VePass.
  2. **Subdirección del Registro Civil**: integración técnica de nacimientos, defunciones, matrimonios, divorcios, adopciones y sus rectificaciones; mantenimiento del BND como nodo central.
  3. **Subdirección de Tecnología y BND**: operación técnica del BND, VePass, INIA y plataformas conexas; ciberseguridad; cumplimiento LOPD.
  4. **Subdirección de Atención al Ciudadano**: red de oficinas territoriales,call center 1-800-VEPASS, gestión de quejas y denuncias.
- **Red territorial**: las 83 oficinas SAIME se transforman en oficinas del SNI, sumadas a las 335 oficinas del Registro Civil existentes y a una red de 500 kioskos autoservicio VePass en alcaldías, centros comerciales, universidades y terminales.
- **Régimen de personal**: idéntico al Pilar III.1 CNSC — concursos públicos, carrera meritocrática, evaluación anual, capacitación obligatoria, VePass como credencial.

#### Separación funcional: Servicio Nacional de Migración y Extranjería (SNMEx)

La reforma **separa** las funciones de migración y extranjería de las de identificación civil, creando el **Servicio Nacional de Migración y Extranjería (SNMEx)** como entidad autónoma hermana del SNI. Esta separación evita que las funciones de identificación (que requieren neutralidad política total) sean capturadas por las funciones migratorias (que son inherentemente sensibles a la política exterior y de seguridad).

| Función | Entidad |
|---|---|
| Cédula de identidad, Cédula-RUT, pasaporte diplomático | SNI |
| Pasaporte ordinario, prórroga, visados, registro de extranjeros, control migratorio, prohibición de salida del país, carnet de movilidad fronteriza, adquisición/renuncia/recuperación de nacionalidad | SNMEx |
| Registro Civil (nacimientos, defunciones, matrimonios, divorcios, adopciones) — funciones técnicas y registrales | SNI |
| Registro Civil — funciones jurisdiccionales (inscripción tardía, rectificación, declaración de ausencia, adopciones) | Tribunales de Municipio (Poder Judicial) |
| Padrón electoral (basado en el Registro Civil) | Consejo Nacional Electoral |

El SNMEx tiene estructura análoga al SNI pero con régimen de personal específico que incorpora controles migratorios (vederías de Interpol, cooperación internacional, escuadrones anti-fraude) y responde al Ministerio del Interior en coordinación con el Ministerio de Relaciones Exteriores.

#### Integración del Registro Civil al SNI

El Registro Civil venezolano es hoy una **institución fragmentada**:

- Las **oficinas de Registro Civil** (aproximadamente 335 a nivel nacional) dependen del Ministerio del Interior.
- La **supervisión técnica** (formatos, libros, procedimientos) está a cargo de la Dirección General del Registro Civil del mismo Ministerio.
- La **fiscalización electoral** (asegurarse de que el padrón refleje correctamente el Registro Civil) corresponde al Consejo Nacional Electoral desde la Ley Orgánica del Poder Electoral.
- Las **funciones jurisdiccionales** (inscripción tardía, rectificación de partidas, declaraciones de ausencia, adopciones, divorcios) corresponden a los Tribunales de Municipio del Poder Judicial.

La reforma **no invierte** esta atribución jurisdiccional (que permanece en el Poder Judicial), pero **centraliza técnicamente** las funciones registrales en el SNI bajo el BND. La consecuencia operativa:

- Toda oficina del Registro Civil existente se integra a la red del SNI.
- El personal del Registro Civil pasa a ser funcionario del SNI (con concursos de transición conforme al régimen del Pilar III.1).
- La plataforma del BND reemplaza los libros en papel y los sistemas heterogéneos actuales.
- Los Tribunales de Municipio acceden al BND con VePass-Fuerte para sus funciones jurisdiccionales, pero no tienen acceso a la operación técnica del registro.
- El Consejo Nacional Electoral consulta el Registro Civil en tiempo real vía BND (en lugar de las conciliaciones periódicas actuales).

#### Transición operativa (3-5 años)

La transformación se ejecuta en cuatro fases:

**Fase 0 — Marco legal y planificación (meses 0-12)**
- Sanción de la Ley Orgánica del SNI y del SNMEx.
- Reglamentos internos del SNI.
- Concurso público para el primer Director General del SNI.
- Auditoría integral del SAIME actual: personal, infraestructura, expedientes, pasivos.
- Diseño técnico de la migración de la plataforma SAIME al BND.
- Inicio de los concursos de transición para personal del SNI (modelo Pilar III.1).

**Fase 1 — Coexistencia operativa (meses 12-24)**
- Las 83 oficinas SAIME operan como "oficinas SNI en transición", con doble etiquetado.
- Emisión de Cédula-RUT nueva en paralelo con la cédula SAIME vigente.
- Migración gradual de la plataforma tecnológica (primero la captura biométrica, luego la emisión de documentos).
- Apertura de los 500 kioskos autoservicio VePass.
- Apertura de la primera red de atención consular digital del SNMEx en 20 embajadas piloto (para reducir la apatridia inducida por ausencia de sedes consulares).

**Fase 2 — Apertura plena del SNI (meses 24-36)**
- Cierre del SAIME como servicio.
- El SNI opera plenamente con Cédula-RUT, BND, VePass.
- El SNMEx opera plenamente con sus atribuciones propias.
- El Registro Civil queda integrado al SNI en todo el territorio.
- Caducidad oficial de la cédula SAIME para todos los efectos administrativos (36 meses desde el inicio del proceso; ventana ya contemplada en III.7.5 "Migración de adultos").

**Fase 3 — Liquidación y consolidación (meses 36-60)**
- Liquidación de pasivos laborales del antiguo SAIME (indemnizaciones conforme a la LOTTT reformada y a los retiros voluntarios incentivados del Pilar III.1).
- Reubicación del personal no incorporado al SNI/SNMEx.
- Cierre del archivo físico histórico del SAIME (transferido al Archivo General de la Nación, con acceso vía BND para verificación).
- Auditoría externa internacional del proceso de transición.

#### Régimen de personal de transición

La reforma protege los derechos del personal del SAIME conforme a la LOTTT reformada (principio 9: mochila austríaca 8,33% + seguro de cesantía 1,2%) y al Pilar III.1 (motoresierra con retiros voluntarios incentivados):

- **Personal que aprueba el concurso de transición**: se incorpora al SNI o al SNMEx con la nueva escala salarial del Pilar III.4 (mínimo USD 500/mes + primas técnicas).
- **Personal que opta por retiro voluntario**: indemnización conforme a la mochila austríaca acumulada + bono adicional equivalente a 6 meses de salario por antigüedad mayor a 5 años en el SAIME.
- **Personal en período de prueba o con menos de 1 año**: baja conforme al procedimiento ordinario de la administración pública.
- **Sindicalización**: el nuevo personal del SNI puede organizarse en sindicatos conforme al Pilar III.6 (libertad sindical plena), pero la dirección es meritocrática y no electoral.
- **Prohibición de reincorporación de personal despedido por corrupción**: la DNA-RB mantiene el registro de personal separado del SAIME por causas disciplinarias o penales; su reingreso al SNI/SNMEx está prohibido por 15 años.

#### Cronograma detallado de transición

| Mes | Acción |
|---|---|
| 0 | Sanción de la Ley Orgánica del SNI y del SNMEx |
| 1 | Publicación de los reglamentos del SNI |
| 2 | Concurso público para Director General del SNI |
| 3 | Concurso público para Director General del SNMEx |
| 4 | Inicio de los concursos de transición para personal del SNI |
| 6 | Auditoría integral del SAIME actual |
| 9 | Diseño técnico de migración de plataforma al BND |
| 12 | Apertura de Fase 1: coexistencia operativa; primeras Cédula-RUT emitidas |
| 15 | Apertura de los primeros 100 kioskos autoservicio VePass |
| 18 | Apertura del BND en Guri-1 a producción |
| 21 | Migración del 50% de las oficinas SAIME a la plataforma BND |
| 24 | Cierre del SAIME como servicio; apertura plena del SNI |
| 27 | Apertura de la red consular digital del SNMEx en 20 embajadas |
| 30 | Caducidad oficial de la cédula SAIME para efectos administrativos |
| 36 | Liquidación del archivo físico histórico del SAIME |
| 48 | Liquidación de pasivos laborales completada |
| 60 | Cierre definitivo del proceso de transición |

#### Marco constitucional y legal de transición

Reforma al artículo 332 CRBV adicionando:

> *"Créase el Servicio Nacional de Identificación (SNI) como persona jurídica pública autónoma, adscrita al Ministerio del Poder Popular para Relaciones Interiores, Justicia y Paz, sucesor del Servicio Administrativo de Identificación, Migración y Extranjería (SAIME) en lo concerniente a identificación civil y registro civil. Créase el Servicio Nacional de Migración y Extranjería (SNMEx) como persona jurídica pública autónoma, sucesor del SAIME en lo concerniente a migración, extranjería y documentación de viaje. La ley orgánica establece la composición, atribuciones, régimen de autonomía y régimen de personal de ambos servicios."*

**Derogatoria expresa**: en la disposición final de la Ley Orgánica del SNI y del SNMEx, se incluye:

> *"Quedan derogados: (a) la Ley Orgánica de Identificación publicada en la Gaceta Oficial N° 29.594 del 26 de agosto de 1971; (b) el Decreto N° 6.733 del 9 de junio de 2009 publicado en la Gaceta Oficial N° 39.196, en lo concerniente a la creación del Servicio Administrativo de Identificación, Migración y Extranjería; (c) la estructura organizativa aprobada en diciembre de 2015 conforme al referido Decreto; (d) todas las disposiciones legales y reglamentarias vigentes que se opongan a la presente ley."*

#### Cláusula de continuidad del SNI

> *"Ninguna reforma al régimen del Servicio Nacional de Identificación podrá aprobarse sin el voto de las tres cuartas partes (3/4) de la Asamblea Nacional y la ratificación mediante referéndum popular."*

La protección se alinea con la del BND, VePass, MIED-LAM, DNA-RB, RUP, CDF, RUI y el algoritmo DV. **Noveno componente** del documento con esta jerarquía constitucional máxima.

#### III.7.5.7.1. Marco legal primario: artículos 68-74 del Decreto N° 6.733 (Gaceta Oficial 39.196, 9 de junio de 2009)

A continuación se transcriben los artículos específicos del Decreto N° 6.733 que crean y regulan el SAIME como servicio desconcentrado del Ministerio del Poder Popular para Relaciones Interiores y Justicia. Esta transcripción se incluye como **fuente primaria** del diagnóstico institucional y como **objeto expreso de la derogatoria** que ejecuta la reforma.

**Artículo 68** (Sección IX del Decreto 6.733 — creación):

> *"La Oficina Nacional de Identificación y la Dirección General de Extranjería pasa a denominarse **Servicio Administrativo de Identificación, Migración y Extranjería** con carácter de servicio desconcentrado sin personalidad jurídica, con capacidad de gestión presupuestaria, administrativa o financiera, dependiente jerárquicamente del Ministro o Ministra del Poder Popular para Relaciones Interiores y Justicia, y su coordinación será ejercida por el Viceministro o Viceministra de Política Interior y Seguridad Jurídica.*
>
> *El Servicio Administrativo de Identificación, Migración y Extranjería podrá utilizar, conjunta o separadamente, las siglas **SAIME** para todos los efectos administrativos y jurisdiccionales."*

**Artículo 69** (atribuciones):

> *"El Servicio Administrativo de Identificación, Migración y Extranjería, se encarga de ejercer las competencias que el ordenamiento jurídico le atribuye al Ejecutivo Nacional en materia de identificación de personas naturales, nacionalidad, extranjería, migración y control de extranjeros."*

**Artículo 70** (misión):

> *"El Servicio Administrativo de Identificación, Migración y Extranjería tiene como misión brindar celeridad y funcionalidad a la identificación ciudadana, mediante la implantación de alta tecnología en sus procesos, con el propósito de garantizar oportunidad el derecho a la identidad y a la seguridad jurídica, así como el ejercicio de sus atribuciones de migración, además de lograr el efectivo control de los extranjeros que se hallaren en el país, en aplicación de las políticas de identificación, migración y extranjería emanadas del Ministerio con competencia en la materia."*

**Artículo 71** (fuentes de ingreso — 7 incisos):

> *"Los ingresos del Servicio Administrativo de Identificación, Migración y Extranjería, serán los siguientes:*
>
> *1. Hasta un setenta y cinco por ciento (75%) de lo recaudado por concepto de tasas por los servicios que preste de conformidad con la ley en materia de timbre fiscal.*
>
> *2. Los ingresos provenientes de convenios celebrados con instituciones públicas y privadas.*
>
> *3. Los recursos que se generen por leyes especiales.*
>
> *4. Los intereses y demás productos que resulten de la administración de sus fondos.*
>
> *5. Los provenientes de donaciones, aportes, subvenciones y demás liberalidades que reciba de personas naturales o jurídicas nacionales de carácter público o privado.*
>
> *6. Los aportes ordinarios o extraordinarios que anualmente se le asigne en la Ley de Presupuesto, a través del Ministerio.*
>
> *7. Cualquier otro recurso que se genere por la autogestión."*

**Artículo 72** (excedentes):

> *"Los ingresos que perciba el Servicio Administrativo de Identificación, Migración y Extranjería, así como los excedentes, deberán orientarse hacia el autofinanciamiento del servicio y serán destinados tanto a los gastos operativos como a los gastos de inversión, de conformidad con las leyes que regulen la materia."*

**Artículo 73** (titular):

> *"El o la titular del Servicio Administrativo de Identificación, Migración y Extranjería tendrá rango de Director o Directora General, quien será designado por el Ministro o Ministra."*

**Artículo 74** (funcionamiento):

> *"El funcionamiento y desarrollo de los procesos del Servicio Administrativo de Identificación, Migración y Extranjería, se regirá conforme a lo señalado en las leyes que lo regulan, en su Reglamento Orgánico y demás normas de funcionamiento que se dicten al efecto."*

**Patrón análogo: Servicio Autónomo de Registros y Notarías (SAREN)** — artículos 75-79 de la Sección X del mismo Decreto 6.733, con naturaleza jurídica idéntica. El SAREN está adscrito al mismo Ministerio y coordina con el Viceministro de Política Interior y Seguridad Jurídica. La reforma del Pilar III.7 (RUI) aprovecha esta arquitectura institucional para reubicar las funciones de registros públicos en el Servicio Nacional del Registro Inmobiliario (SNRI), separándolas del Registro Civil propiamente dicho.

#### III.7.5.7.2. Diagnóstico jurídico comparado entre el Decreto 6.733 y la reforma propuesta

| Aspecto | Decreto 6.733 (2009) | Reforma propuesta (Pilar III.7) |
|---|---|---|
| **Naturaleza jurídica del SAIME** | Servicio desconcentrado sin personalidad jurídica (art. 68) | Persona jurídica pública autónoma (SNI) con patrimonio propio |
| **Designación del titular** | Designado por el Ministro (art. 73); libre nombramiento conforme al art. 4 del propio Decreto | Concurso público + ratificación 3/5 AN + período fijo 7 años no reelegible |
| **Adscripción política** | Dependiente jerárquicamente del Ministro del Interior + coordinado por el Viceministro de Política Interior y Seguridad Jurídica (art. 68) | Adscrito al Ministerio del Interior pero sin dependencia jerárquica directa; coordinación con el Viceministro sustituida por autonomía funcional |
| **Régimen de personal** | Cargos directivos de "libre nombramiento y remoción" (art. 4 del Decreto); personal sin concurso meritocrático obligatorio | Concurso meritocrático vía CNSC (Pilar III.1); mochila austríaca; VePass como credencial |
| **Coordinación con migración** | Integrada en el mismo servicio (art. 68; 69) | **Separada**: SNMEx como servicio hermano con directorio propio |
| **Plataforma tecnológica** | Subcontratada a vendors extranjeros sin auditoría (proveedor estatal extranjero 2011-2022, Exclé Argentina 2022+) | BND propio en Guri-1/2/3 con código abierto auditado por SPDP |
| **Control de captura política** | Ninguno explícito | Cláusula 3/4 + referéndum; veeduría internacional; incompatibilidades |
| **Ingresos** | Hasta 75% tasas de timbre fiscal + autogestión (art. 71) | Asignación presupuestaria del Presupuesto Nacional + tasas reducidas (Cédula-RUT gratuita para el ciudadano); ingresos por VePass-Firma, RUI, RUP, certificados digitales |
| **Modificación del marco normativo** | Por Decreto presidencial del MPPREIJ (sin Asamblea Nacional) | Por ley orgánica con 3/5 AN; estructura blindada contra reorganización discrecional |

Esta tabla demuestra que la reforma del Pilar III.7 **invierte cada uno de los rasgos del SAIME actual** que producen la crisis institucional documentada: convierte el servicio desconcentrado en persona jurídica autónoma, el libre nombramiento en concurso meritocrático, la dependencia política en autonomía funcional, la plataforma subcontratada en infraestructura soberana, y la modificación discrecional en reforma constitucional agravada.

#### Métricas de éxito de la transición

| Indicador | Línea base (2024) | Meta año 3 | Meta año 6 |
|-----------|-------------------|------------|-------------|
| SAIME en operación | Sí | No (cerrado) | No |
| SNI operativo con VePass | No | Sí | Sí |
| Cédulas SAIME vigentes | 100% | 30% | 0% |
| Cédulas-RUT emitidas | 0 | 80% | 100% |
| Oficinas SNI operativas | 0 | 125 (de 125) | 125 |
| Kioskos VePass operativos | 0 | 300 | 500 |
| Pasaportes emitidos/año | 300.000 | 2.500.000 | 3.500.000 |
| Plazo promedio emisión pasaporte | 6-24 meses | 5 días | 24 horas |
| Casos de extorsión documentados | n/d | <50/año | 0 |
| Venezolanos en el exterior con acceso consular digital (SNMEx) | <5% | 70% | 95% |

---

## III.7.6. Cédula-RUT: documento físico con QR + NFC + chip biométrico

### Especificaciones técnicas inspirado en el modelo chileno (Cédula de Identidad 2019-)

La Cédula-RUT es una tarjeta de policarbonato con:

- **Chip NFC** con datos cifrados: RUN/RUT, foto, 10 huellas (template, no crudo), firma electrónica, certificados de autenticación.
- **Código QR** de alta densidad con la misma información, legible sin contacto para verificación rápida por autoridades.
- **Datos impresos** legibles a simple vista: nombre completo, RUN/RUT, fecha de nacimiento, sexo, nacionalidad, fecha de emisión y vencimiento, autoridad emisora.
- **Elementos de seguridad física**: holograma, micro-impresiones, tinta óptica variable (OVI), grabado láser.
- **Tarjeta bilingüe**: español + warao, wayúu, pemón y otras lenguas indígenas según región de emisión.

inspirado en a la cédula chilena (Servicio de Registro Civil e Identificación, 2019) y al NRIC de Singapur.

### Activación con biometría del titular

La Cédula-RUT se activa por primera vez en el Registro Civil al momento de su emisión, mediante:

1. **Registro de las 10 huellas dactilares** (templates, no imágenes crudas, cifrados).
2. **Captura de foto biométrica** (estándar ICAO 9303).
3. **Captura de firma manuscrita digitalizada**.
4. **Vinculación con el VePass** del titular (si es menor de edad, vinculado al VePass de sus padres hasta cumplir 14 años).

Cada activación posterior de la tarjeta como **factor de autenticación** requiere la coincidencia de al menos una huella (en condiciones normales) o la combinación con PIN para usos sensibles.

### Bloqueo por el portador

El titular puede bloquear su Cédula-RUT **en cualquier momento** mediante:

- **App móvil** VePass (bloqueo con huella + PIN).
- **Oficina del Registro Civil presencial** (con huella + documento de identidad o, si es la cédula misma la perdida, con testigo o medio alternativo).
- **Call center** (verificación por voz + OTP al celular o email registrado + preguntas de seguridad).
- **Sitio web** VePass (bloqueo con VePass-Plus + OTP por SMS / email / app).

**El bloqueo es inmediato e irreversible desde la perspectiva del portador.** Una vez bloqueada, la tarjeta no sirve para autenticación ni para firmar documentos. La rehabilitación requiere:

1. Solicitar nueva Cédula-RUT en cualquier oficina del Registro Civil.
2. Acreditar identidad mediante el proceso estándar (huella + foto + firma).
3. Pagar el costo de reposición (1 UT, salvo caso de robo acreditado).

inspirado en el bloqueo de tarjeta bancaria: el bloqueo es la regla, no la excepción, ante cualquier sospecha.

---

## III.7.7. Registro de huellas dactilares: casos especiales

El estándar es el registro de **las 10 huellas dactilares** (todos los dedos de ambas manos) conforme a las normas ICAO 9303 y NIST. Sin embargo, se contemplan los siguientes casos especiales:

### Caso 1: Persona que ha perdido dedos de una mano

Se registran las huellas disponibles (los 5 dedos de la otra mano, más los dedos que conserve de la mano afectada). Se completa el registro con:

- **Registro fotográfico** de ambas manos, con fecha, ángulo y médico certificador.
- **Certificado médico** que acredite la causa de la pérdida (accidente, cirugía, condición congénita).
- **Huella plantar** (del dedo gordo del pie) como respaldo secundario.

### Caso 2: Persona que ha perdido una mano entera

Se registran las 5 huellas de la mano conservada, más:

- Registro fotográfico de la mano conservada y del muñón.
- Certificado médico.
- Huella plantar del dedo gordo del pie del mismo lado del cuerpo (huella espejo como respaldo).

### Caso 3: Persona que ha perdido ambas manos

Se activa el **registro de huella de familiar directo**:

- **Prioridad 1**: huella de la madre.
- **Prioridad 2**: huella del padre.
- **Prioridad 3**: huella de un hijo adulto.
- **Prioridad 4**: huella de un hermano adulto.

Cada familiar debe acreditar vínculo por documento (acta de nacimiento, acta de matrimonio) y registrar su propia huella en el Registro Civil como huella de respaldo autorizada. La activación de la Cédula-RUT del familiar afectado requiere que el familiar autorizado esté presente en el momento del uso (autenticación dual: familiar + beneficiario).

### Caso 4: Persona sin manos y sin familiares directos disponibles

Se activa el registro de **huella plantar**:

- Huella de los 10 dedos de los pies (plantares).
- Huella del dedo gordo del pie como patrón principal.
- Registro fotográfico completo del pie.

inspirado en a la práctica forense internacional (INTERPOL) en la que las huellas plantares son patrón secundario válido.

### Caso 5: Persona con amputación o malformación que afecta manos y pies

Registro combinado de:

- Huellas disponibles (las que conserve).
- Registro fotográfico del cuerpo completo para identificación visual.
- Marcadores genéticos del Banco Nacional de ADN como factor definitivo de identificación.
- Activación del protocolo de **autenticación por ADN** con muestra tomada al momento del uso (hisopo de mejilla) y comparación contra el registro del Banco Nacional de ADN.

El Banco Nacional de ADN se convierte, en estos casos extremos, en el factor definitivo de identificación y autenticación.

### Normativa técnica

La norma de implementación se detalla en el **Reglamento General del SNI**, que establece:

- Equipos biométricos certificados (FBI IAFIS Appendix F para huellas, ICAO 9303 para foto).
- Procedimientos de captura para personas con discapacidad.
- Período de retención de datos (mínimo: 75 años después de la muerte del titular).
- Protocolos de cadena de custodia para muestras de ADN.

---

## III.7.8. Ley Orgánica de Protección de Datos Personales

La reforma sanciona una **Ley Orgánica de Protección de Datos Personales (LOPD)** inspirada en el RGPD europeo (Reglamento 2016/679), la LGPD brasileña (Lei 13.709/2018) y la Ley 19.628 chilena, con los siguientes principios:

### Principios rectores

1. **Consentimiento informado**: todo tratamiento de datos personales requiere consentimiento libre, específico e informado del titular.
2. **Finalidad**: los datos sólo pueden usarse para los fines declarados al momento de la recolección.
3. **Minimización**: sólo se recolectan los datos estrictamente necesarios.
4. **Exactitud**: los datos deben ser exactos y actualizados.
5. **Limitación del plazo de conservación**: los datos se conservan sólo durante el plazo necesario para la finalidad.
6. **Integridad y confidencialidad**: medidas técnicas y organizativas adecuadas para proteger los datos.
7. **Responsabilidad proactiva**: el responsable del tratamiento debe demostrar cumplimiento.
8. **Privacidad desde el diseño**: los sistemas se diseñan con privacidad incorporada.
9. **Evaluación de impacto**: los tratamientos de alto riesgo requieren evaluación previa.

### Derechos del titular

- **Acceso**: conocer qué datos se tienen y para qué se usan.
- **Rectificación**: corregir datos inexactos.
- **Supresión (derecho al olvido)**: solicitar eliminación cuando no haya base legal para conservarlos.
- **Oposición**: oponerse a tratamientos basados en interés legítimo.
- **Portabilidad**: recibir los propios datos en formato estructurado y de uso común.
- **No ser objeto de decisiones automatizadas con efectos significativos**: garantía de intervención humana.

### Autoridad de control

La **Superintendencia de Protección de Datos Personales (SPDP)**, organismo constitucional con autonomía funcional, integrada por 3 Superintendentes designados por 3/5 de la Asamblea por períodos de 8 años.

La SPDP tiene facultades de investigación, sanción (multas hasta 4% del PIB del infractor), y resolución de conflictos entre titulares y responsables.

### Categorías especiales de datos

Los datos biométricos (huellas, ADN, iris), los datos de salud, los datos de origen étnico, las opiniones políticas, las convicciones religiosas y los datos de menores de edad se consideran **categorías especiales de datos** y gozan de protección reforzada.

Su tratamiento requiere:
- Consentimiento explícito del titular (o de sus padres en caso de menores).
- Base legal específica (generalmente, prestación de un servicio público esencial como salud o educación).
- Medidas técnicas reforzadas.
- Auditoría periódica por la SPDP.

---

## III.7.9. VePass en defensa y seguridad nacional

El usuario que origina este documento planteó la necesidad de uso de los datos también por las instituciones de defensa. La propuesta incorpora:

### Acceso de defensa con control civil reforzado

- Los sistemas de defensa pueden acceder a datos del BND mediante **autorización específica del Ministerio de Defensa**, con notificación simultánea a la SPDP y al Comité de Supervisión Parlamentaria (creado en la reforma constitucional).
- Las solicitudes de acceso deben **dejar registro indeleble** (bitácora inalterable).
- Los accesos con fines de defensa quedan sujetos a **revisión anual por el Comité Parlamentario de Inteligencia** (analogía al Comité de Inteligencia del Congreso de EE.UU.).

### Datos excluidos del acceso de defensa

- Datos de salud mental.
- Datos de orientación sexual o identidad de género.
- Datos de afiliación religiosa.
- Datos de opiniones políticas.
- Datos de menores (salvo riesgo inminente para la integridad del menor, con autorización judicial).

---

## III.7.10. Cláusula de continuidad

Reforma al artículo 56 CRBV adicionando:

> *"Ninguna reforma al régimen del Servicio Nacional de Identificación, del VePass, del Banco Nacional de Datos o del Sistema Nacional de Identidad podrá aprobarse sin el voto de las tres cuartas partes (3/4) de la Asamblea Nacional y la ratificación mediante referéndum popular."*

La identidad de los venezolanos es la infraestructura más crítica del Estado. Su capturapolítica es un riesgo comparable a la captura del Banco Central o de la Fuerza Armada: por eso la misma jerarquía de protección (3/4 + referéndum).

---

## III.7.11. Cronograma de implementación

| Fase | Período | Hitos principales |
|------|---------|-------------------|
| **0. Marco legal** | Meses 0-12 | Reforma constitucional aprobada + LOPD sancionada + Reglamento General del SNI + creación del Servicio Nacional de Identificación |
| **1. Infraestructura física** | Meses 0-24 | Construcción de los 3 data centers Guri + red de fibra óptica nacional + sistema de VePass operativo |
| **2. Registro de niños vivos** | Meses 12-18 | Integración hospitalaria universal + inicio del nuevo proceso de inscripción inmediata |
| **3. Migración de adultos** | Meses 18-36 | Emisión masiva de Cédula-RUT con QR + NFC + chip biométrico; instalación de kioskos autoservicio en las 335 oficinas del Registro Civil existentes |
| **4. Expansión de servicios** | Años 3-5 | Integración de todos los organismos al VePass + interoperabilidad X-Road completa + IA disponible para instituciones |
| **5. Consolidación** | Años 5-7 | Migración completa + auditorías + ajustes + cobertura universal |

## III.7.12. Indicadores de éxito

| Indicador | Línea base (2024) | Meta año 3 | Meta año 6 |
|-----------|-------------------|------------|------------|
| Venezolanos con Cédula-RUT nueva | 0% | 70% | 100% |
| Venezolanos con VePass activo | 0% | 60% | 95% |
| Niños inscritos en plazo (24h urbano / 5 días rurales) | <30% | 75% | 95% |
| Hospitales con Registro Civil integrado | <20% | 70% | 100% |
| Trámites accesibles por VePass | <5 | 200 | 500 |
| Tiempo promedio de un trámite presencial | Variable (3-30 días) | 1 día | <1 hora |
| Capacidad computacional INIA | 0 PFLOPS | 2,5 PFLOPS | 25 PFLOPS |
| Muestras de ADN en Banco Nacional | 0 | 2 M | 30 M |
| Instituciones integradas al BND (X-Road) | 0 | 30 | 100 |
| Costo de operación per cápita | n/a | <USD 5/año | <USD 3/año |
| Satisfacción ciudadana con servicios digitales | <10% | 50% | 75% |

## III.7.13. Riesgos y mitigación

| Riesgo | Prob. | Impacto | Mitigación |
|--------|------|---------|------------|
| Ataque cibernético al BND | Alta | Crítico | Arquitectura 3-site + cifrado AES-256 + redundancia + CERT nacional + simulacros mensuales + seguro cibercrimen |
| Filtración masiva de datos | Media | Crítico | Privacy-by-design + cifrado en reposo y en tránsito + tokenización + monitoreo en tiempo real + notificación obligatoria a SPDP en 24h |
| Capturapolítica del Servicio Nacional de Identificación | Media | Crítico | Incompatibilidades + renovación escalonada + cláusula 3/4 + referéndum + veeduría internacional |
| Resistencia cultural al registro biométrico | Alta | Medio | Campaña pedagógica + opción de inscripción progresiva + garantía de no uso político + monitoreo internacional |
| Exclusión de personas sin acceso digital | Alta | Alto | Kioskos autoservicio + Cédula-RUT física + oficinas del Registro Civil existentes + línea de atención 1-800-VEPASS para adultos mayores |
| Brecha de talento técnico (ciberseguridad, IA, criptografía) | Alta | Alto | Plan nacional de formación técnica + salarios competitivos + repatriación de talento + convenios internacionales |
| Colapso del Guri (guerra, sabotaje, desastre natural) | Baja | Crítico | 3 sitios geográficamente distribuidos + generadores de respaldo + plan de evacuación + mirror en sitio extranjero neutral (cifrado homomórfico) |
| Usopolítico de la IA para vigilancia masiva | Media | Alto | Supervisión parlamentaria + auditoría algorítmica externa + lista negra de usos prohibidos + VePass como factor de auditoría |

---

*Continuará: III.8 Planificación estratégica de Estado inspirado en modelo coreano-singapurense.*
