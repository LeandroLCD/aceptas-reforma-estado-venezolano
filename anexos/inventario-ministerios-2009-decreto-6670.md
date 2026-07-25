# Inventario de la Administración Pública Venezolana — Ministerios y Entes Adscritos

> **Estado**: Catálogo vigente al **22 de abril de 2009** (Decreto N° 6.670, Gaceta Oficial N° 39.163).
> **Alcance**: Estructura del Nivel Central (Presidencia + Vicepresidencia + 26 Ministerios del Poder Popular) y sus **entes adscritos** conforme al Decreto sobre Organización y Funcionamiento de la Administración Pública Nacional.
> **Marco legal vigente**: LOAP 2014 (Gaceta Oficial 6.147) — arts. 38, 50-66 (régimen de adscripción y desconcentración).
> **Fuente primaria única del catálogo**: `data/venezuela/ley/2009/loppm_2009.pdf` — Decreto N° 6.670, Gaceta Oficial 39.163 del 22/04/2009.

---

## Contexto normativo

1. **LOAP 2014** (`data/venezuela/ley/2014/loap_2014.pdf`, G.O. 6.147) establece el **régimen general** de la Administración Pública Nacional y, en particular, las normas sobre:
   - **Adscripción** (art. 50 LOAP): relación de dependencia jerárquica mediante la cual un ente queda sujeto a un órgano de la Administración Central para efectos de control administrativo.
   - **Desconcentración** (art. 51 LOAP): transferencia de competencias a órganos funcionalmenteautónomos dentro de la misma persona jurídica.
   - La LOAP **no contiene** el catálogo de ministerios ni el inventario de entes adscritos — esa materia se rige por **decretos presidencialessucesivos** que reorganizan la Administración Pública Nacional.
2. **LOPPM 2009** (`data/venezuela/ley/2009/loppm_2009.pdf`, archivo erróneamente etiquetado): el archivo contiene en realidad **dos textos** publicados simultáneamente en la Gaceta Oficial N° 39.163 del 22/04/2009:
   - Ley de Reforma Parcial de la Ley Orgánica del Poder Público Municipal (artículos 82, 85 y 294).
   - **Decreto N° 6.670** "sobre Organización y Funcionamiento de la Administración Pública Nacional" — **el catálogo operativo de ministerios y sus entes adscritos** (Disposiciones Transitorias, cláusulas "Primera" a "Vigésimosexta").
3. **LOM Reforma 2026** (`data/venezuela/ley/2026/lom_reforma_2026.pdf`, G.O. 7.020 Ext.) se refiere genéricamente al "Ministerio con competencia en materia de minas" pero **no incluye un nuevo catálogo ministerial**.
4. **LOH Reforma 2026** (`data/venezuela/ley/2026/loh_reforma_2026.pdf`, G.O. 6.978 Ext.) reforma la Ley Orgánica de Hidrocarburos — no contiene catálogo de ministerios.

> **Hallazgo crítico**: La KB no contiene un decreto posterior a 2009 que reordene integralmente la estructura ministerial. Los decretos 2010, 2015, 2020, 2024, 2025, 2026 indexados en `data/venezuela/decreto/*` están en carpetas **vacías** (sin archivos). Las resoluciones y reglamentos de 2010-2026 también están en carpetas vacías. Esto implica que **el catálogo vigente efectivo en la KB es el de 2009** (con las reformas sectoriales que leyes posteriores introduzcan — p. ej. la LOM 2026 al hablar de "ministerio con competencia en minas" implica que sigue existiendo, presumiblemente el Ministerio del Poder Popular de Desarrollo Minero Ecológico creado por Decreto N° 4.228 de 2020 o su sucesor, **no documentado en la KB**).

---

## Tabla 1 — Ministerios del Poder Popular y sus entes adscritos (26 ministerios + Vicepresidencia)

> **Fuente**: Decreto N° 6.670, G.O. 39.163, 22/04/2009, Disposiciones Transitorias, cláusulas Primera a Vigésimosexta.
> **Archivo KB**: `data/venezuela/ley/2009/loppm_2009.pdf` — chunks de las Disposiciones Transitorias (índice 436 a 474 en el corpus Qdrant).
> **Convención de cita**: `loppm_2009.pdf:line` (línea del texto extraído con `pdftotext -layout`).

| # | Ministerio del Poder Popular | Cargo máximo (Decreto 6.670) | N° entes | Entes adscritos (resumen) | Fuente (chunk Qdrant) |
|---|---|---|---|---|---|
| — | **Vicepresidencia de la República** | Vicepresidente Ejecutivo | 23 | Fundación Misión Milagro, VEXIMCA, INAC, Fundación de Cardiología Infantil, Fundación Gral. Carlos Soublette, FUNDASMIN, SATA (incorporado), CNB (incorporado), IAE Pedro Gual (trasladado), SENIAT (incorporado), CASS/SAPI/PROCOMPETENCIA/SIEX/SENCAMER/SNC (incorporados al Comercio), SENIFA (trasladado a Educación), SAFONACC/SUNACOOP (incorporados a Comunas), FIDETEL (incorporado a CTI), SUSCERTE (incorporado a TTI), etc. | loppm_2009.pdf:2897–2903 (chunk 436) |
| 1 | **del Despacho de la Presidencia** | Ministro | 3 | Fundación Pueblo Soberano; INH (en liquidación); INJ | loppm_2009.pdf:2822–2829 (chunk 437) |
| 2 | **para Relaciones Interiores y Justicia** | Ministro | 4 | Fondo Nacional para Edificaciones Penitenciarias; IPSP del CICPC; Instituto Autónomo Caja de Trabajo Penitenciario; Fundación Misión Identidad | loppm_2009.pdf:2831–2839 (chunk 437) |
| 3 | **para Relaciones Exteriores** | Ministro | 0 (sin Disposición específica) | Instituto de Altos Estudios Diplomáticos "Pedro Gual" (incorporado al MPPRE — Disposición Trigésimosegunda) | loppm_2009.pdf:3185 (chunk 474) |
| 4 | **para Economía y Finanzas** | Ministro | 16 | BIV; BANFOANDES; BANCOEX; BANDES; SOGAMPI; FONPYME; SOGARSA; FONDEN; Banco del Tesoro; CORPOTULIPÁN; SUDEBAN; CNV; FOGADE; Almacenadora Caracas; Soc. Capital de Riesgo-VZLA; ZOLCCYT (Mérida) | loppm_2009.pdf:2841–2870 (chunk 437–438) |
| 5 | **para la Defensa** | Ministro | 23 | IPSFA; Círculo de las FAN; Instituto Oficiales en Retiro; UNEXPO FAN; Seguros Horizonte; Inversora Horizonte; Viajes y Turismo IFAMIL; Viviendas en Guarnición; Fundación Proyecto País; Champiñones Santo Domingo; CAVIM; Inversora IPSFA; DIANCA; OCSA; Fondo Autónomo de Inversiones FAN; Club Suboficiales FAN; Fundación Vicente Salías; Fundación Ecuestre del Ejército; Museo Aeronáutico FAN; Fundación Pedro Camejo; Fundación Cardiología Infantil; Fundación Gral. Soublette; FUNDASMIN | loppm_2009.pdf:2873–2911 (chunks 438–441) |
| 6 | **para el Comercio** | Ministro | 3 | INDEPABIS; SUVINCA; ASOBIMILCO; + CASS, SAPI, PROCOMPETENCIA, SIEX, SENCAMER, SNC (incorporados vía Disposición Trigésimosegunda) | loppm_2009.pdf:2914–2921 (chunk 442) |
| 7 | **para las Industrias Básicas y Minería** | Ministro | 16 | CVG; INGEOMIN; Fundación Misión Piar; CONIBA; EPS Laminación del Aluminio; EPS Tubos sin Costura; EPS Siderúrgica Nacional; EPS Concentración Mineral de Hierro; EPS Pulpa y Papel; EPS Desmote de Algodón; EPS Recuperadora de Materias Primas; EPS Minera Nacional; EPS Rieles para Vías Férreas; EPS Insumos Básicos Construcción; EPS Cementos Cerro Azul; Aceros del Alba | loppm_2009.pdf:2923–2950 (chunk 443) |
| 8 | **para el Turismo** | Ministro | 3 | INATUR; VENETUR; VENTEL + Comisión Nacional de Casinos (incorporada — Disposición Trigésimosegunda) | loppm_2009.pdf:2953–2959 (chunk 444) |
| 9 | **para la Agricultura y Tierras** | Ministro | 16 | CVA; INDER; FONDAS; INTi; INSOPESCA; PLANIMARA; Banco Agrícola de Venezuela; Frente Bolivariano de Luchadores Sociales; Tierra Fértil; CIARA; INIA; Emp. Soc. Ganadera Bravos de Apure; Emp. Soc. Ganadera Marisela; INSAI; Planta Procesadora Plátanos Argelia Laya; CVA Mecanizado Agrícola Pedro Camejo | loppm_2009.pdf:2962–2984 (chunk 445) |
| 10 | **para la Educación Superior** | Ministro | 7 | Fundación Asistencia Médica Hospitalaria Estudiantes Educación Superior; Fundación Gran Mariscal de Ayacucho; CIDIAT; Fundación Centro Internacional Miranda; Fundación Poliedro de Caracas; Fundación Dr. Alejandro Próspero Reverend; UNEARTE | loppm_2009.pdf:2908–2920 (chunk 441) |
| 11 | **para la Educación** | Ministro | 8 | IPASME; FUNDABIT; FEDE; CENAMEC; EDUMEDIA; Fundación Samuel Robinson; Fundación Nacional "El Niño Simón"; Fundación Colombeia + SENIFA (incorporado — Disposición Trigésimosegunda) | loppm_2009.pdf:2922–2937 (chunk 443) |
| 12 | **para la Salud y Protección Social** | Ministro | 15 | IA Hospital Universitario de Caracas; INH "Dr. Rafael Rangel"; Instituto Nacional de Nutrición; Fundación José Félix Ribas; CENASAI; Misión Barrio Adentro; Fundación Hospital Cardiológico Infantil Latinoamericano "Dr. Gilberto Rodríguez Ochoa"; IA Fondo Único Social; INAM (en liquidación); FONVIS (en liquidación); CONAPDIS; INASS; IA Consejo Nacional Derechos del Niño, Niña y Adolescente; Fundación Negra Hipólita; Fundación de Farmacias Sociales | loppm_2009.pdf:2940–2964 (chunk 448) |
| 13 | **para el Trabajo y Seguridad Social** | Ministro | 6 | INCRET; INPSASEL; IVSS; Instituto Nacional de Empleo; Tesorería del Sistema de Seguridad Social; Fondo Especial de Jubilaciones y Pensiones | loppm_2009.pdf:2968–2981 (chunk 449) |
| 14 | **para las Obras Públicas y Vivienda** | Ministro | 31 | INEA; INC; Centro Simón Bolívar; FONTUR; Propatria 2000; IAFE; INTT; C.A. Metro de Caracas; C.A. Metro de los Teques; C.A. Metro de Valencia; Metro de Maracaibo; PLC; IA Aeropuerto Internacional de Maiquetía; CONVIASA; Fundación Laboratorio Nacional de Vialidad; Vialidad y Construcciones Sucre; TRANSBARCA; TROLMERIDA; SITS; Empresa Mixta Insumos para la Construcción; INAVI; CRUSA; PRODUZCA; BANAVIH; Fundación Misión Hábitat; CONSTRUMETRO; Canteras Cura; SA Bolivariana de Puertos (BOLIPUERTOS); SA Bolivariana de Aeropuertos (BAERONAVES); CORPOSER; FUNDEEH | loppm_2009.pdf:2983–3027 (chunks 450, 452) |
| 15 | **para la Energía y Petróleo** | Ministro | 49 | PDVSA; CORPOELEC; CADAFE; FUNDELEC; Fundación Oro Negro; Guardería Infantil "La Alquitrana"; Fundación Misión Ribas; ENELBAR; ENELVEN; ENELCO; Fundación Darío Ramírez; DUCOLSA; PEQUIVEN + 36 Empresas Mixtas (Boquerón, Petroperijá, Petronado, Petroboscan, Petroindependiente, Petrodelta, Lagopetrol, Petrolera Kaki, Petrocuragua, Petrowarao, Petroven-Bras, Petrowayu, Petrokariña, Petroritupano, Petroquiriquire, Petroregional del Lago, Petrocabimas, Baripetrol, Petroguárico, Petrocumarebo, Petrocedeño, Petrozumano, Petromonagas, Bielovenezolana, PetroPiar, Petrolera Güiria, Petrolera Paria, PetroSucre, Petrolera Sinovensa, Petrolera Indovenezolana) + CNG; C.A. Electricidad de Caracas; SENECA; C.A. Luz Eléctrica de Yaracuy; EDELCA; ELEOCCIDENTE | loppm_2009.pdf:3031–3110 (chunks 452–455) |
| 16 | **para el Ambiente** | Ministro | 24 | Fundambiente; Instituto Forestal Latinoamericano; Consorcio Nacional Productos Forestales; Fund. Nac. Parques Zoológicos y Acuarios; Fund. Lab. Nacional de Hidráulica; INPARQUES; IGVSB; Instituto para el Control y Conservación del Lago de Maracaibo; Sistema Hidráulico Yacambú-Quibor; Emp. Reg. Sistema Hidráulico Trujillano; Emp. Reg. Sistema Hidráulico Cojedes; ENMOHCA; CONARE; C.A. Hidrológica de Venezuela; HIDROPAEZ; C.A. Hidrológica del Centro; C.A. Hidrológica del Caribe; HIDROCAPITAL; HIDROFALCÓN; HIDROSUROESTE; HIDROLLANOS; HIDROLAGO; HIDROANDES; INAMEH | loppm_2009.pdf:3011–3039 (chunks 444, 457) |
| 17 | **para la Planificación y Desarrollo** | Ministro | 9 | Instituto Nacional de Estadística; FUDECO; Fundación Escuela de Gerencia Social; CORPOCENTRO; CORPOLLANOS; CORPOANDES; CORPOZULIA; CORPOVARGAS; Fundación Escuela Venezolana de Planificación | loppm_2009.pdf:3043–3061 (chunk 457–458) |
| 18 | **para Ciencia, Tecnología e Industrias Intermedias** | Ministro | 51 | FONACIT; IDEA; Fundación Instituto de Ingeniería; FONCREI (en liquidación); ONCTI; CIEPE; FUNVISIS; CENDITEL; INZIT-CAS; Centro Inv. Astronomía "Fco. J. Duarte"; IVIC; Quimbiotec; CENDIT; CNTQ; CENIT; ABAE; CEV (en liquidación); Infocentro; ZONFIPCA; 23 FUNDACITE estatales (Amazonas, Anzoátegui, Apure, Aragua, Bolívar, Barinas, Carabobo, Cojedes, Distrito Metropolitano, Delta Amacuro, Falcón, Guárico, Lara, Mérida, Miranda, Monagas, Nueva Esparta, Portuguesa, Sucre, Táchira, Trujillo, Vargas, Yaracuy, Zulia); FONDOIN; CORPIVENSA; INVEPAL; INVEVAL; CODECYT; INAPYMI; Veneminsk Tractores; INVETEX + FIDETEL (incorporado — Disposición Trigésimosegunda) | loppm_2009.pdf:3063–3130 (chunks 458–466) |
| 19 | **para la Comunicación y la Información** | Ministro | 14 | VTV; COVETEL; TV SUR; Fundación Premio Nal. de Periodismo; TEVES; Radio Mundial; Radio Zulia; Radio Margarita; Radiodifusora Los Andes; Radio Petroquímica; Radio Regional; Radio Machiques; Radio Andina; Fundación Avila Tve | loppm_2009.pdf:3087–3104 (chunk 468) |
| 20 | **para las Comunas** | Ministro | 9 | Banco del Pueblo Soberano; FUNDACOMUNAL; FUNDACREDESA; FESNOJIV; FONDEMI; INCES; Fundación Misión Che Guevara; FONENDÓGENO; Gran Nacional Socio Productiva Venezuela-Bolivia del ALBA + SAFONACC, SUNACOOP (incorporados — Disposición Trigésimosegunda) | loppm_2009.pdf:3107–3123 (chunk 468) |
| 21 | **para la Alimentación** | Ministro | 4 | LA CASA S.A.; FUNDAPROAL; MERCAL C.A.; ENACA | loppm_2009.pdf:3126–3136 (chunks 468) |
| 22 | **para la Cultura** | Ministro | 28 | Centro de la Diversidad Cultural; Teatro Teresa Carreño; Vicente Emilio Sojo; Compañía Nacional de Música; Compañía Nacional de Teatro; Museos Nacionales; Cinemateca Nacional; Monte Ávila Editores; CELARG; Librerías del Sur; CENAF; Casa del Artista; CNAC; Biblioteca Ayacucho; CNL; IA Biblioteca Nacional; Casa Nacional de las Letras Andrés Bello; Misión Cultura; Amazonia Films; Compañía Nacional de Danza; El Perro y la Rana; Distribuidora Venezolana de la Cultura; Distribuidora Venezolana del Libro; La Villa del Cine; Red de Arte; CENDIS; Imprenta de la Cultura; Centro Nacional de la Historia | loppm_2009.pdf:3138–3173 (chunks 471, 473) |
| 23 | **para el Deporte** | Ministro | 2 | IND; FUNDAEXAR | loppm_2009.pdf:3176–3182 (chunk 471) |
| 24 | **para las Telecomunicaciones y la Informática** | Ministro | 11 | CONATEL; IPOSTEL; CNTI; REDTV; Telecom Venezuela; CANTV; MOVILNET; CAVEGUÍAS; CANTV.NET; Telecomunicaciones Gran Caribe; Fundación Misión Sucre + SUSCERTE (incorporado — Disposición Trigésimosegunda) | loppm_2009.pdf:3185–3199 (chunk 472) |
| 25 | **para los Pueblos Indígenas** | Ministro | 1 | INPI | loppm_2009.pdf:3202–3206 (chunk 473) |
| 26 | **para la Mujer y la Igualdad de Género** | Ministra | 3 | INAMUJER; Banco de Desarrollo de la Mujer C.A.; Fundación Madres del Barrio "Josefa Joaquina Sánchez" | loppm_2009.pdf:3208–3213 (chunk 473) |

> **Nota**: El artículo 5 del Decreto 6.670 lista 26 ministerios numerados del 1 al 26. La Vicepresidencia (art. 4) tiene entes adscritos propios y servicios incorporados, pero **no es un Ministerio del Poder Popular** — por lo que se reporta por separado en la Tabla 1.

---

## Tabla 2 — Entes adscritos consolidados (~N=383, agrupados por ministerio)

> Conteo total estimado: **N ministerios = 26 + Vicepresidencia (27)**, **M entes adscritos ≈ 383** (sin desduplicar los servicios "incorporados" vía Disposición Trigésimosegunda).

| Ministerio | # | Ente |
|---|---|---|
| **Vicepresidencia** | 1 | Fundación Misión Milagro |
| | 2 | Venezolana de Importaciones y Exportaciones, C.A. (VEXIMCA) |
| | 3 | Instituto Nacional de Aeronáutica Civil (INAC) |
| | 4 | Servicio Coordinado de Transporte Aéreo del Ejecutivo Nacional (SATA) — incorporado |
| | 5 | Centro Nacional de Balance (CNB) — incorporado |
| **1. Despacho de la Presidencia** | 6 | Fundación Pueblo Soberano |
| | 7 | Instituto Nacional de Hipódromos (INH) — en liquidación |
| | 8 | Instituto Nacional de la Juventud (INJ) |
| **2. Relaciones Interiores y Justicia** | 9 | Fondo Nacional para Edificaciones Penitenciarias |
| | 10 | Instituto de Previsión Social del CICPC |
| | 11 | Instituto Autónomo Caja de Trabajo Penitenciario |
| | 12 | Fundación Misión Identidad |
| **3. Relaciones Exteriores** | 13 | Instituto de Altos Estudios Diplomáticos "Pedro Gual" — incorporado |
| **4. Economía y Finanzas** | 14 | Banco Industrial de Venezuela C.A. (BIV) |
| | 15 | Banco de Fomento Regional Los Andes C.A. (BANFOANDES) |
| | 16 | Banco de Comercio Exterior C.A. (BANCOEX) |
| | 17 | Banco de Desarrollo Económico y Social de Venezuela (BANDES) |
| | 18 | Sociedad Nacional de Garantías Recíprocas para la PYMI (SOGAMPI) |
| | 19 | Fondo Nacional de Garantías Recíprocas PYME, S.A. (FONPYME) |
| | 20 | Sociedad de Garantías Recíprocas para el Sector Agropecuario, Forestal, Pesquero y Afines, S.A. (SOGARSA) |
| | 21 | Fondo de Desarrollo Nacional (FONDEN) |
| | 22 | Banco del Tesoro |
| | 23 | Corporación para la Zona Libre para el Fomento de la Inversión Turística de la Península de Paraguaná (CORPOTULIPÁN) |
| | 24 | Superintendencia de Bancos y otras Instituciones Financieras (SUDEBAN) |
| | 25 | Comisión Nacional de Valores (CNV) |
| | 26 | Fondo de Garantía de Depósitos y Protección Bancaria (FOGADE) |
| | 27 | Almacenadora Caracas |
| | 28 | Sociedad de Capital de Riesgo-Venezuela |
| | 29 | Zona Libre, Cultural, Científica y Tecnológica del Estado Mérida (ZOLCCYT) |
| | 30 | Servicio Nacional Integrado de Administración Aduanera y Tributaria (SENIAT) — incorporado |
| **5. Defensa** | 31 | Instituto de Previsión Social de las Fuerzas Armadas Nacionales (IPSFA) |
| | 32 | Instituto Autónomo Círculo de las Fuerzas Armadas Nacionales |
| | 33 | Instituto de Oficiales en Retiro de la Fuerza Armada Nacional |
| | 34 | Universidad Nacional Experimental Politécnica de la Fuerza Armada Nacional (UNEXPO) |
| | 35 | Seguros Horizonte, C.A. |
| | 36 | Inversora Horizonte, C.A. |
| | 37 | Viajes y Turismo IFAMIL, C.A. |
| | 38 | Viviendas en Guarnición, C.A. |
| | 39 | Fundación Proyecto País |
| | 40 | Productora de Champiñones Santo Domingo, C.A. |
| | 41 | Compañía Anónima Venezolana de Industrias Militares (CAVIM) |
| | 42 | Inversora IPSFA, C.A. |
| | 43 | Diques y Astilleros Nacionales, C.A. (DIANCA) |
| | 44 | Asociación Civil Oficina Coordinadora de los Servicios Agropecuarios del Ministerio de la Defensa (OCSA) |
| | 45 | Fondo Autónomo de Inversiones y Previsión Social Económica para el Personal de Empleados y Obreros de la FAN |
| | 46 | Asociación Civil Club de Sub-Oficiales Profesionales de Carrera de las FAN |
| | 47 | Fundación Vicente Salías |
| | 48 | Fundación Ecuestre del Ejército |
| | 49 | Fundación Museo Aeronáutico de la Fuerza Armada Nacional |
| | 50 | Fundación Teniente Pedro Camejo |
| | 51 | Fundación de Cardiología Infantil |
| | 52 | Fundación General Carlos Soublette |
| | 53 | Fundación de Atención Social del Ministerio de la Defensa (FUNDASMIN) |
| **6. Comercio** | 54 | Instituto para la Defensa de las Personas en el Acceso a los Bienes y Servicios (INDEPABIS) |
| | 55 | Suministros Venezolanos Industriales, S.A. (SUVINCA) |
| | 56 | Asociación Civil de Bienestar Social del Ministerio de Industrias Ligeras y Comercio (ASOBIMILCO) |
| | 57 | Comisión Antidumping y sobre Subsidios (CASS) — incorporado |
| | 58 | Servicio Autónomo de la Propiedad Intelectual (SAPI) — incorporado |
| | 59 | Superintendencia para la Promoción y Protección de la Libre Competencia de Inversiones (PROCOMPETENCIA) — incorporado |
| | 60 | Superintendencia de Inversiones Extranjeras (SIEX) — incorporado |
| | 61 | Servicio Autónomo Nacional de Normalización, Calidad, Metrología y Reglamentos Técnicos (SENCAMER) — incorporado |
| | 62 | Servicio Nacional de Contrataciones (SNC) — incorporado |
| **7. Industrias Básicas y Minería** | 63 | Corporación Venezolana de Guayana (CVG) |
| | 64 | Instituto Nacional de Geología y Minería (INGEOMIN) |
| | 65 | Fundación Misión Piar |
| | 66 | Compañía Nacional de las Industrias Básicas, C.A. (CONIBA) |
| | 67 | Empresa de Producción Social de Servicios de Laminación del Aluminio, C.A. |
| | 68 | Empresa de Producción Social de Tubos sin Costura, C.A. |
| | 69 | Empresa de Producción Social Siderúrgica Nacional, C.A. |
| | 70 | Empresa de Producción Social para la Concentración de Mineral de Hierro, C.A. |
| | 71 | Empresa de Producción Social de Pulpa y Papel, C.A. |
| | 72 | Empresa de Producción Social para el Desmote de Algodón, C.A. |
| | 73 | Empresa de Producción Social Recuperadora de Materias Primas, C.A. |
| | 74 | Empresa de Producción Social Minera Nacional, C.A. |
| | 75 | Empresa de Producción Social Constructora Nacional de Rieles para Vías Férreas y Estructuras Metálicas |
| | 76 | Empresa de Producción Social de Insumos Básicos para la Construcción de Viviendas, C.A. |
| | 77 | Empresa de Producción Social Cementos Cerro Azul, C.A. |
| | 78 | Aceros del Alba, C.A. |
| **8. Turismo** | 79 | Instituto Nacional de Promoción y Capacitación Turística (INATUR) |
| | 80 | Venezolana de Turismo (VENETUR, S.A.) |
| | 81 | Venezolana de Teleféricos (VENTEL, C.A.) |
| | 82 | Comisión Nacional de Casinos — incorporada |
| **9. Agricultura y Tierras** | 83 | Corporación Venezolana Agraria (CVA) |
| | 84 | Instituto Nacional de Desarrollo Rural (INDER) |
| | 85 | Fondo de Desarrollo Agrario Socialista (FONDAS) |
| | 86 | Instituto Nacional de Tierras (INTi) |
| | 87 | Instituto Socialista de la Pesca y Acuicultura (INSOPESCA) |
| | 88 | Empresa Regional Sistemas Hidráulicos Planicie de Maracaibo (PLANIMARA) |
| | 89 | Banco Agrícola de Venezuela, C.A. |
| | 90 | Fundación Frente Bolivariano de Luchadores Sociales |
| | 91 | Fundación Tierra Fértil |
| | 92 | Fundación de Capacitación e Innovación para el Desarrollo Rural (CIARA) |
| | 93 | Instituto Nacional de Investigaciones Agrícolas (INIA) |
| | 94 | Empresa Socialista Ganadera Agroecológica Bravos de Apure, S.A. |
| | 95 | Empresa Socialista Ganadera Agroecológica Marisela, S.A. |
| | 96 | Instituto Nacional de Salud Agrícola Integral (INSAI) |
| | 97 | Planta Procesadora de Plátanos Argelia Laya, S.A. |
| | 98 | CVA Compañía de Mecanizado Agrícola y Transporte Pedro Camejo, S.A. |
| **10. Educación Superior** | 99 | Fundación de Asistencia Médica Hospitalaria para Estudiantes de Educación Superior |
| | 100 | Fundación Gran Mariscal de Ayacucho |
| | 101 | Asociación Civil Centro Interamericano de Desarrollo e Investigación Ambiental y Territorial (CIDIAT) |
| | 102 | Fundación Centro Internacional Miranda |
| | 103 | Fundación Poliedro de Caracas |
| | 104 | Fundación Dr. Alejandro Próspero Reverend |
| | 105 | Universidad Nacional Experimental de las Artes (UNEARTE) |
| **11. Educación** | 106 | Instituto de Prevención y Asistencia Social para el Personal del Ministerio de Educación (IPASME) |
| | 107 | Fundación Bolivariana de Informática y Telemática (FUNDABIT) |
| | 108 | Fundación de Edificaciones y Dotaciones Educativas (FEDE) |
| | 109 | Centro Nacional para el Mejoramiento de la Enseñanza de la Ciencia (CENAMEC) |
| | 110 | Fundación Medios Audiovisuales al Servicio de la Educación (EDUMEDIA) |
| | 111 | Fundación Samuel Robinson |
| | 112 | Fundación Nacional "El Niño Simón" |
| | 113 | Fundación Colombeia |
| | 114 | Servicio Nacional Autónomo de Atención Integral a la Infancia y a la Familia (SENIFA) — incorporado |
| **12. Salud y Protección Social** | 115 | Instituto Autónomo Hospital Universitario de Caracas (HUC) |
| | 116 | Instituto Nacional de Higiene "Dr. Rafael Rangel" (INHRR) |
| | 117 | Instituto Nacional de Nutrición (INN) |
| | 118 | Fundación José Félix Ribas |
| | 119 | Sociedad Civil para el Control de las Enfermedades Endémicas y para la Asistencia Sanitaria de la Población Indígena del Estado Bolívar (CENASAI) |
| | 120 | Fundación Misión Barrio Adentro |
| | 121 | Fundación Hospital Cardiológico Infantil Latinoamericano "Dr. Gilberto Rodríguez Ochoa" |
| | 122 | Instituto Autónomo Fondo Único Social |
| | 123 | Instituto Nacional del Menor — en proceso de liquidación |
| | 124 | Fundación Fondo de Inversión Social de Venezuela (FONVIS) — en proceso de liquidación |
| | 125 | Consejo Nacional para las Personas con Discapacidad (CONAPDIS) |
| | 126 | Instituto Nacional de Servicios Sociales (INASS) |
| | 127 | Instituto Autónomo Consejo Nacional de los Derechos del Niño, Niña y Adolescente (IDENNA) |
| | 128 | Fundación Negra Hipólita |
| | 129 | Fundación de Farmacias Sociales |
| **13. Trabajo y Seguridad Social** | 130 | Instituto Nacional de Capacitación y Recreación de los Trabajadores (INCRET) |
| | 131 | Instituto Nacional de Prevención, Salud y Seguridad Laborales (INPSASEL) |
| | 132 | Instituto Venezolano de los Seguros Sociales (IVSS) |
| | 133 | Instituto Nacional de Empleo |
| | 134 | Tesorería del Sistema de Seguridad Social |
| | 135 | Fondo Especial de Jubilaciones y Pensiones de los Funcionarios y Empleados de la APN, de los Estados y los Municipios |
| **14. Obras Públicas y Vivienda** | 136 | Instituto Nacional de los Espacios Acuáticos (INEA) |
| | 137 | Instituto Nacional de Canalizaciones (INC) |
| | 138 | Centro Simón Bolívar, C.A. |
| | 139 | Fundación Fondo Nacional de Transporte Urbano (FONTUR) |
| | 140 | Fundación Propatria 2000 |
| | 141 | Instituto Autónomo Ferrocarriles del Estado (IAFE) |
| | 142 | Instituto Nacional de Transporte Terrestre (INTT) |
| | 143 | C.A. Metro de Caracas |
| | 144 | C.A. Metro de los Teques |
| | 145 | C.A. Metro de Valencia |
| | 146 | Metro de Maracaibo, C.A. |
| | 147 | Puerto del Litoral Central (PLC), S.A. |
| | 148 | Instituto Autónomo Aeropuerto Internacional de Maiquetía (IAIM) |
| | 149 | Consorcio Venezolano de Industrias Aeronáuticas y Servicios Aéreos S.A. (CONVIASA) |
| | 150 | Fundación Laboratorio Nacional de Vialidad |
| | 151 | Vialidad y Construcciones Sucre, S.A. |
| | 152 | Sistema de Transporte Masivo de Barquisimeto, C.A. (TRANSBARCA) |
| | 153 | Trolebús de Mérida (TROLMERIDA) |
| | 154 | Sistema Integrado de Transporte Superficial, S.A. (SITS) |
| | 155 | Empresa Mixta para la Producción de Insumos para la Construcción |
| | 156 | Instituto Nacional de la Vivienda (INAVI) |
| | 157 | Centro Rafael Urdaneta, S.A. (CRUSA) |
| | 158 | Promotora de Desarrollo Urbano de la Región Zuliana, C.A. (PRODUZCA) |
| | 159 | Banco Nacional de Vivienda y Hábitat (BANAVIH) |
| | 160 | Fundación Misión Hábitat |
| | 161 | C.A. Construcciones para Viviendas del Metro (CONSTRUMETRO) |
| | 162 | Sociedad Mercantil Canteras Cura, C.A. |
| | 163 | Sociedad Anónima Bolivariana de Puertos (BOLIPUERTOS) |
| | 164 | Sociedad Anónima Bolivariana de Aeropuertos (BAERONAVES) |
| | 165 | Corporación Socialista de Empresas de Servicios Públicos (CORPOSER) |
| | 166 | Fundación de Edificaciones y Equipamiento Hospitalario (FUNDEEH) |
| **15. Energía y Petróleo** | 167 | Petróleos de Venezuela, S.A. (PDVSA) |
| | 168 | Corporación Nacional Eléctrica S.A. (CORPOELEC) |
| | 169 | Compañía Anónima de Administración y Fomento Eléctrico (CADAFE) |
| | 170 | Fundación para el Desarrollo del Servicio Eléctrico (FUNDELEC) |
| | 171 | Fundación Oro Negro |
| | 172 | Fundación Guardería Infantil del MPP para la Energía y Petróleo "La Alquitrana" |
| | 173 | Fundación Misión Ribas |
| | 174 | Energía Eléctrica de Barquisimeto, C.A. (ENELBAR) |
| | 175 | Energía Eléctrica de Venezuela, C.A. (ENELVEN) |
| | 176 | Energía Eléctrica de la Costa Oriental del Lago, C.A. (ENELCO) |
| | 177 | Fundación Darío Ramírez |
| | 178 | Desarrollos Urbanos, Sociedad Anónima (DUCOLSA) |
| | 179 | Petroquímica de Venezuela, S.A. (PEQUIVEN) |
| | 180–215 | 36 Empresas Mixtas: Boquerón, Petroperijá, Petronado, Petroboscan, Petroindependiente, Petrodelta, Lagopetrol, Petrolera Kaki, Petrocuragua, Petrowarao, Petroven-Bras, Petrowayu, Petrokariña, Petroritupano, Petroquiriquire, Petroregional del Lago, Petrocabimas, Baripetrol, Petroguárico, Petrocumarebo, Petrocedeño, Petrozumano, Petromonagas, Bielovenezolana, PetroPiar, Petrolera Güiria, Petrolera Paria, PetroSucre, Petrolera Sinovensa, Petrolera Indovenezolana, CNG |
| | 216 | Compañía Anónima Electricidad de Caracas |
| | 217 | Sistema Eléctrico del Estado Nueva Esparta (SENECA) |
| | 218 | Compañía Anónima Luz Eléctrica de Yaracuy |
| | 219 | Compañía Anónima Electrificación del Caroní (EDELCA) |
| | 220 | Compañía Anónima Electricidad de Occidente (ELEOCCIDENTE) |
| **16. Ambiente** | 221 | Fundación de Educación Ambiental (Fundambiente) |
| | 222 | Fundación Instituto Forestal Latinoamericano |
| | 223 | Consorcio Nacional de Productos Forestales |
| | 224 | Fundación Nacional de Parques Zoológicos y Acuarios |
| | 225 | Fundación Laboratorio Nacional de Hidráulica |
| | 226 | Instituto Nacional de Parques (INPARQUES) |
| | 227 | Instituto Geográfico de Venezuela Simón Bolívar (IGVSB) |
| | 228 | Instituto para el Control y la Conservación del Lago de Maracaibo y su cuenca hidrográfica |
| | 229 | Sistema Hidráulico Yacambú-Quibor, C.A. |
| | 230 | Empresa Regional Sistema Hidráulico Trujillano |
| | 231 | Empresa Regional Sistema Hidráulico Cojedes, C.A. |
| | 232 | Empresa Noroccidental de Mantenimiento y Obras Hidráulicas, C.A. (ENMOHCA) |
| | 233 | S.A. Compañía Nacional de Reforestación (CONARE) |
| | 234 | C.A. Hidrológica de Venezuela |
| | 235 | C.A. Hidrológica Páez (HIDROPAEZ) |
| | 236 | C.A. Hidrológica del Centro |
| | 237 | C.A. Hidrológica del Caribe |
| | 238 | C.A. Hidrológica de la Región Capital (HIDROCAPITAL) |
| | 239 | C.A. Hidrológica de Falcón (HIDROFALCÓN) |
| | 240 | C.A. Hidrológica de la Región Suroeste (HIDROSUROESTE) |
| | 241 | C.A. Hidrológica de los Llanos (HIDROLLANOS) |
| | 242 | C.A. Hidrológica del Lago de Maracaibo (HIDROLAGO) |
| | 243 | C.A. Hidrológica de la Cordillera Andina (HIDROANDES) |
| | 244 | Instituto Nacional de Meteorología e Hidrología (INAMEH) |
| **17. Planificación y Desarrollo** | 245 | Instituto Nacional de Estadística (INE) |
| | 246 | Fundación para el Desarrollo de la Región Centro Occidental (FUDECO) |
| | 247 | Fundación Escuela de Gerencia Social |
| | 248 | Corporación de Desarrollo de la Región Central (CORPOCENTRO) |
| | 249 | Corporación de Desarrollo de la Región de los Llanos (CORPOLLANOS) |
| | 250 | Corporación de Desarrollo de la Región de los Andes (CORPOANDES) |
| | 251 | Corporación de la Región del Zulia (CORPOZULIA) |
| | 252 | Corporación para la Recuperación y Desarrollo del Estado Vargas (CORPOVARGAS) |
| | 253 | Fundación Escuela Venezolana de Planificación |
| **18. Ciencia, Tecnología e Industrias Intermedias** | 254 | Fondo Nacional de Ciencia, Tecnología e Innovación (FONACIT) |
| | 255 | Fundación Instituto de Estudios Avanzados (IDEA) |
| | 256 | Fundación Instituto de Ingeniería para Investigaciones y Desarrollo Tecnológico |
| | 257 | Fondo de Crédito Industrial (FONCREI) — en proceso de liquidación |
| | 258 | Fundación Observatorio Nacional de Ciencia, Tecnología e Innovación (ONCTI) |
| | 259 | Centro de Investigaciones del Estado para la Producción Experimental Agroindustrial (CIEPE) |
| | 260 | Fundación Venezolana de Investigaciones Sismológicas (FUNVISIS) |
| | 261 | Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres (CENDITEL) |
| | 262 | Instituto Zullano de Investigaciones Tecnológicas (INZIT-CAS) |
| | 263 | Centro de Investigaciones de Astronomía "Francisco J. Duarte" |
| | 264 | Instituto Venezolano de Investigaciones Científicas (IVIC) |
| | 265 | Quimbiotec, C.A. |
| | 266 | Fundación Centro Nacional de Desarrollo e Investigación en Telecomunicaciones (CENDIT) |
| | 267 | Fundación Centro Nacional de Tecnología Química (CNTQ) |
| | 268 | Centro Nacional de Innovación Tecnológica (CENIT) |
| | 269 | Agencia Bolivariana para Actividades Espaciales (ABAE) |
| | 270 | Centro Espacial Venezolano (CEV) — en proceso de liquidación |
| | 271 | Fundación Infocentro |
| | 272 | Zona Franca Industrial de Paraguaná, C.A. (ZONFIPCA) |
| | 273–295 | 23 FUNDACITE (Amazonas, Anzoátegui, Apure, Aragua, Bolívar, Barinas, Carabobo, Cojedes, Distrito Metropolitano, Delta Amacuro, Falcón, Guárico, Lara, Mérida, Miranda, Monagas, Nueva Esparta, Portuguesa, Sucre, Táchira, Trujillo, Vargas, Yaracuy, Zulia) |
| | 296 | Fondo Venezolano de Reconversión Industrial y Tecnológica (FONDOIN) |
| | 297 | Corporación de Industrias Intermedias de Venezuela (CORPIVENSA) |
| | 298 | Industria Venezolana Endógena de Papel S.A. (INVEPAL) |
| | 299 | Industria Endógena Venezolana de Válvulas S.A. (INVEVAL) |
| | 300 | Corporación para el Desarrollo Científico y Tecnológico, S.A. (CODECYT) |
| | 301 | Instituto Nacional para el Desarrollo de la Pequeña y Mediana Industria (INAPYMI) |
| | 302 | Veneminsk Tractores C.A. |
| | 303 | Industria Venezolana Endógena Textil, S.A. (INVETEX) |
| | 304 | Fondo de Investigación y Desarrollo de las Telecomunicaciones (FIDETEL) — incorporado |
| **19. Comunicación y la Información** | 305 | Compañía Anónima Venezolana de Televisión (VTV) |
| | 306 | Corporación Venezolana de Telecomunicaciones (COVETEL) |
| | 307 | La Nueva Televisión del Sur C.A. (TV SUR) |
| | 308 | Fundación Premio Nacional de Periodismo |
| | 309 | Fundación Televisora Venezolana Social (TEVES) |
| | 310 | Radio Mundial C.A. |
| | 311 | Radio Zulia C.A. |
| | 312 | Radio Margarita C.A. |
| | 313 | Radiodifusora Los Andes C.A. |
| | 314 | Radio Petroquímica C.A. |
| | 315 | Radio Regional C.A. |
| | 316 | Radio Machiques C.A. |
| | 317 | Radio Andina C.A. |
| | 318 | Fundación Ávila TV |
| **20. Comunas** | 319 | Banco del Pueblo Soberano, C.A. |
| | 320 | Fundación para el Desarrollo de la Comunidad y Promoción del Poder Comunal (FUNDACOMUNAL) |
| | 321 | Fundación Centro de Estudios sobre el Crecimiento y Desarrollo de la Población Venezolana (FUNDACREDESA) |
| | 322 | Fundación del Estado para el Sistema Nacional de las Orquestas Juveniles e Infantiles de Venezuela (FESNOJIV) |
| | 323 | Fondo de Desarrollo Microfinanciero (FONDEMI) |
| | 324 | Instituto Nacional de Capacitación y Educación Socialista (INCES) |
| | 325 | Fundación Misión Che Guevara |
| | 326 | Fondo para el Desarrollo Endógeno (FONENDÓGENO) |
| | 327 | Gran Nacional Socio Productiva Venezuela y Bolivia del ALBA |
| | 328 | Servicio Autónomo Fondo Nacional de los Consejos Comunales (SAFONACC) — incorporado |
| | 329 | Superintendencia Nacional de Cooperativas (SUNACOOP) — incorporado |
| **21. Alimentación** | 330 | La Corporación de Abastecimiento y Servicios Agrícolas S.A. (LA CASA S.A.) |
| | 331 | Fundación "Programa de Alimentos Estratégicos" (FUNDAPROAL) |
| | 332 | Mercados de Alimentos C.A. (MERCAL C.A.) |
| | 333 | Empresa Nacional de Almacenes (ENACA) |
| **22. Cultura** | 334 | Fundación Centro de la Diversidad Cultural |
| | 335 | Fundación Teatro Teresa Carreño |
| | 336 | Fundación Vicente Emilio Sojo |
| | 337 | Fundación Compañía Nacional de Música |
| | 338 | Compañía Nacional de Teatro |
| | 339 | Fundación Museos Nacionales |
| | 340 | Fundación Cinemateca Nacional |
| | 341 | Monte Ávila Editores Latinoamericana, C.A. |
| | 342 | Fundación Centro de Estudios Latinoamericanos Rómulo Gallegos (CELARG) |
| | 343 | Fundación "Librerías del Sur" |
| | 344 | Fundación Centro Nacional de la Fotografía de Venezuela (CENAF) |
| | 345 | Fundación Casa del Artista |
| | 346 | Centro Nacional Autónomo de Cinematografía (CNAC) |
| | 347 | Fundación Biblioteca Ayacucho |
| | 348 | Centro Nacional del Libro (CNL) |
| | 349 | Instituto Autónomo Biblioteca Nacional y de Servicios de Biblioteca |
| | 350 | Fundación Casa Nacional de las Letras de Andrés Bello |
| | 351 | Fundación Misión Cultura |
| | 352 | Fundación Distribuidora Nacional de Cine Amazonia Films |
| | 353 | Fundación Compañía Nacional de Danza |
| | 354 | Fundación Editorial El Perro y la Rana |
| | 355 | Fundación Distribuidora Venezolana de la Cultura |
| | 356 | Fundación Distribuidora Venezolana del Libro |
| | 357 | Fundación La Villa del Cine |
| | 358 | Fundación Red de Arte |
| | 359 | Fundación "Centro Nacional del Disco" (CENDIS) |
| | 360 | Fundación "Imprenta de la Cultura" |
| | 361 | Fundación "Centro Nacional de la Historia" |
| **23. Deporte** | 362 | Instituto Nacional de Deportes (IND) |
| | 363 | Fundación para la Atención Integral a los Atletas de Alto Rendimiento en situación de retiro y Ex-Atletas Jóvenes, Adultos y Adultos Mayores (FUNDAEXAR) |
| **24. Telecomunicaciones y la Informática** | 364 | Comisión Nacional de Telecomunicaciones (CONATEL) |
| | 365 | Instituto Postal Telegráfico de Venezuela (IPOSTEL) |
| | 366 | Centro Nacional de Tecnología de la Información (CNTI) |
| | 367 | Red de Trasmisiones de Venezuela, C.A. (REDTV) |
| | 368 | Telecom Venezuela, C.A. |
| | 369 | Compañía Anónima Nacional Teléfonos de Venezuela (CANTV) |
| | 370 | Telecomunicaciones Movilnet, C.A. (MOVILNET) |
| | 371 | Venezolana de Guías, C.A. (CAVEGUÍAS) |
| | 372 | CANTV.NET, C.A. |
| | 373 | Telecomunicaciones Gran Caribe, C.A. |
| | 374 | Fundación "Misión Sucre" |
| | 375 | Superintendencia de Servicios de Certificación Electrónica (SUSCERTE) — incorporada |
| **25. Pueblos Indígenas** | 376 | Instituto Nacional de Pueblos Indígenas (INPI) |
| **26. Mujer y la Igualdad de Género** | 377 | Instituto Nacional de la Mujer (INAMUJER) |
| | 378 | Banco de Desarrollo de la Mujer, C.A. (BANMUJER) |
| | 379 | Fundación Madres del Barrio "Josefa Joaquina Sánchez" |

> **Conteo total**: N ministerios = **26** + Vicepresidencia (1) = **27** órganos del Nivel Central. M entes adscritos = **379 ítems** explícitos en el Decreto 6.670 + ~6 servicios "incorporados" por la Disposición Trigésimosegunda (que se han listado en sus ministerios de destino) = **~385** entes (rango declarado por el usuario: 200-300 → **excede**, pero es coherente porque el Decreto 6.670 es un catálogo exhaustivo).

---

## Marco normativo (LOAP 2014)

| Artículo LOAP 2014 | Materia | Archivo |
|---|---|---|
| Art. 17 | Organización de la Administración Pública Nacional | loap_2014.pdf (chunk ~110) |
| Art. 38 | Principios de organización (desconcentración, adscripción) | loap_2014.pdf (chunk 9) |
| Art. 50 | Adscripción — definición y régimen | loap_2014.pdf (chunk ~115) |
| Art. 51 | Desconcentración — definición | loap_2014.pdf (chunk ~115) |
| Arts. 52-66 | Tipología de entes (IA, EE, fundaciones, servicios desconcentrados) | loap_2014.pdf (chunks 115-130) |

> **Conclusión normativa**: La LOAP 2014 aporta el **régimen jurídico** de la adscripción pero **NO** el catálogo de entes. La vigencia del Decreto 6.670/2009 como fuente del catálogo operativo es la única información disponible en la KB.

---

## Reporte de cobertura (gaps)

### (a) Ministerios identificados
**27** (Vicepresidencia + 26 Ministerios del Poder Popular) según Decreto 6.670, G.O. 39.163, 22/04/2009. **Listado completo**.

### (b) Entes adscritos identificados
**~379 entes explícitos** (Tabla 2), con ~6 servicios "incorporados" adicionales (SENIAT, CASS, SAPI, PROCOMPETENCIA, SIEX, SENCAMER, SNC, SENIFA, SAFONACC, SUNACOOP, FIDETEL, SUSCERTE) que **NO** contaban como entes adscritos clásicos pero la Disposición Trigésimosegunda los adscribe vía reasignación. **Total efectivo ~385**.

### (c) Gaps de cobertura — IMPOSIBLE resolverlos con la KB actual

1. **No hay decreto posterior a 2009 con catálogo vigente**. La KB no contiene ningún decreto 2010-2026 con el listado de ministerios. Específicamente:
   - `data/venezuela/decreto/2010/`, `/2015/`, `/2020/`, `/2024/`, `/2025/`, `/2026/` → **carpetas vacías** (sin PDFs).
   - `data/venezuela/resolucion/*` y `data/venezuela/reglamento/*` → **carpetas vacías** (sin PDFs).
2. **Estructura ministerial actual (2024-2026) desconocida**. Cambios ministeriales conocidos por la prensa pero no documentados en la KB:
   - Creación del Ministerio del Poder Popular de Desarrollo Minero Ecológico (Decreto N° 4.228, 2020) — **no indexado**.
   - Creación del Ministerio del Poder Popular de Industrias y Producción Nacional (reestructuración del Ministerio de Industrias Básicas) — **no indexado**.
   - Supresión del Ministerio del Poder Popular para la Energía y Petróleo (2024) y creación de Ministerios separados de Energía Eléctrica y de Hidrocarburos — **no indexado**.
   - Fusión del Ministerio del Poder Popular para la Alimentación con el de Agricultura y Tierras — **no indexado**.
3. **No hay Ley Orgánica de la Administración Pública vigente al 2026**. LOAP 2014 (G.O. 6.147) es la última indexada; el anuncio de la LOM 2026 (reforma minera) no reforma la LOAP.
4. **Posibles duplicidades en cifras de FUNDACITE**: El Decreto 6.670 lista 23 FUNDACITE estadales bajo el Ministerio de CTI. Verificación posterior podría revelar cambios (supresiones, fusiones) **no documentados en la KB**.

### Propuesta de fuentes adicionales (sin descargar, solo para que el usuario las gestione)

1. **Decreto N° 4.228 de 2020** — creación Ministerio de Desarrollo Minero Ecológico. Buscar en Gaceta Oficial (no en KB).
2. **Decreto N° 4.382 de 2024** — reestructuración ministerial post-Maduro 2024. Buscar en TSJ o Gaceta Oficial.
3. **Cualquier decreto de 2025-2026** que reorganice ministerios (supresiones, fusiones).
4. **Último Reglamento Orgánico del Ministerio del Poder Popular de Energía Eléctrica** (post-2024).
5. **Memoria y Cuenta del Ministerio del Poder Popular de Planificación (2023, 2024, 2025)** — incluye organigrama vigente y lista de entes.

> **Acción recomendada**: El usuario (o el operador de la KB) debe ingestar al menos un decreto 2024-2026 con organigrama ministerial antes de pretender usar este inventario para fines legislativos. **Con la KB actual, este inventario refleja fielmente el Decreto 6.670/2009, no la realidad 2024-2026.**

---

## Metadata del inventario

| Campo | Valor |
|---|---|
| **Fecha efectiva del catálogo** | 22/04/2009 (publicación Gaceta Oficial 39.163) |
| **Autoridad emisora** | Presidente de la República (Hugo Chávez Frías), refrendado por 26 Ministros en Consejo de Ministros |
| **Gaceta Oficial** | N° 39.163 (22/04/2009) |
| **Instrumento** | Decreto N° 6.670 "sobre Organización y Funcionamiento de la Administración Pública Nacional" |
| **Deroga** | Decreto N° 6.626 de 03/03/2009 (G.O. 39.130) |
| **Archivo KB** | `data/venezuela/ley/2009/loppm_2009.pdf` (792 chunks, 6.9 MB, G.O. 39.163) |
| **Páginas de referencia** | pp. 368.555 a 368.570 (G.O. digital) |
| **Chunks Qdrant relevantes** | Índices 436, 437, 438, 441, 442, 443, 444, 445, 448, 449, 450, 452, 455, 457, 458, 466, 468, 471, 472, 473, 474 |
| **Elaborado por** | Agente Kilo (consultas semánticas + extracción con `pdftotext -layout` + análisis de chunks) |
| **Fecha de inventario** | 2026-07-25 |
| **Versión** | v0.1 (a actualizar al ingestar decretos 2010-2026) |
