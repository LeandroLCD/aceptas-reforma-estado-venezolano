#!/usr/bin/env python3
"""
v2: Aplica convencion de siglas con deteccion robusta de "ya definido".

Reglas mejoradas:
- Detecta estos patrones y NO expande (ya estan definidos):
  1. **SIGLA** ya expandido: **(Full Name (SIGLA))**
  2. **SIGLA** (Full Name) en negrita seguido de nada o texto
  3. SIGLA seguido inmediatamente de (Full Name) en cualquier formato
  4. Full Name (SIGLA) en cualquier sitio
- Compuestos tipo "VePass-Firma" se preservan (no se inserta expansion).
- Solo tablas: mantener sigla limpia, sin expansion.
- Solo headings: dejarlos como estan.
- Frontmatter YAML: ignorar (no expandir).
- Code blocks: ignorar.
- Glosario al pie solo si no existe ya.
"""

import os
import re
import sys
import argparse
from pathlib import Path

REPO = Path("/home/develop/Documentos/aceptas-reforma-estado-venezolano")

SIGLAS = {
    "CRBV": "Constitución de la República Bolivariana de Venezuela",
    "LOAP": "Ley Orgánica de la Administración Pública",
    "LOAFSP": "Ley Orgánica de la Administración Financiera del Sector Público",
    "LOPP": "Ley Orgánica de Planificación Pública",
    "LCA": "Ley de Carrera Administrativa",
    "LOM": "Ley Orgánica de Minas",
    "LOH": "Ley Orgánica de Hidrocarburos",
    "LORAFEE": "Ley Orgánica del Régimen de Adquisición Forzosa de Acciones de Empresas Estratégicas",
    "LORPSP": "Ley Orgánica de Reforma del Sector Público",
    "LOBCV": "Ley Orgánica del Banco Central de Venezuela",
    "LOESPM": "Ley Orgánica del Servicio de Policía y Cuerpo de Policía Municipal",
    "LOSPCN": "Ley Orgánica del Servicio de Policía y Cuerpo de Policía Nacional",
    "LOTTT": "Ley Orgánica del Trabajo, los Trabajadores y las Trabajadoras",
    "LOT": "Ley Orgánica del Trabajo",
    "LOTSJ": "Ley Orgánica del Tribunal Supremo de Justicia",
    "LOSCM": "Ley Orgánica del Servicio Civil Meritocrático",
    "LOE": "Ley Orgánica de Educación",
    "COT": "Código Orgánico Tributario",
    "COPP": "Código Orgánico Procesal Penal",
    "AN": "Asamblea Nacional",
    "BCV": "Banco Central de Venezuela",
    "CGR": "Contraloría General de la República",
    "CNE": "Consejo Nacional Electoral",
    "FAN": "Fuerza Armada Nacional",
    "PG": "Procuraduría General de la República",
    "TSJ": "Tribunal Supremo de Justicia",
    "BND": "Banco Nacional de Datos",
    "CDF": "Certificado de Defunción Fetal",
    "CICPC": "Cuerpo de Investigaciones Científicas, Penales y Criminalísticas",
    "CNSC": "Comisión Nacional del Servicio Civil",
    "CONAELEC": "Comisión Nacional de Energía Eléctrica",
    "CPNP": "Cuerpo de Policía Nacional Profesional",
    "DNA-RB": "Dirección Nacional Anticorrupción y Recuperación de Bienes",
    "DNPEP": "Dirección Nacional de Planificación Estratégica y Prospectiva",
    "FEM": "Fondo de Estabilización Macroeconómica",
    "FNIP": "Fondo Nacional de Inversión Productiva",
    "FOSEIP": "Fondo Soberano de Estabilización e Inversión Productiva",
    "JNEM": "Junta Nacional de Evaluación Médica",
    "MEDI": "Ministerio del Desarrollo de la Inteligencia",
    "MIED-LAM": "Ministerio del Desarrollo de la Inteligencia, Educación y Deporte Dr. Luis Alberto Machado",
    "RTER": "Régimen de Tres Exámenes Rigurosos",
    "RUI": "Registro Único de Inmuebles",
    "RUP": "Registro Único de Profesionales",
    "RUVI": "Registro Único de Víctimas",
    "SNI": "Sistema Nacional de Identidad",
    "SPDP": "Superintendencia de Protección de Datos Personales",
    "SUNAA": "Superintendencia Nacional de Aguas y Saneamiento",
    "VePass": "Clave Única de Identidad Digital",
    "Cédula-RUT": "Cédula con Rol Único Tributario",
    "BANAVIH": "Banco Nacional de Vivienda y Hábitat",
    "CADAFE": "Compañía Anónima de Administración y Fomento Eléctrico",
    "CANTV": "Compañía Anónima Nacional Teléfonos de Venezuela",
    "CORPOELEC": "Corporación Eléctrica Nacional",
    "CVG": "Corporación Venezolana de Guayana",
    "IVSS": "Instituto Venezolano de los Seguros Sociales",
    "INCRET": "Instituto de Capacitación y Recreación de los Trabajadores",
    "INJ": "Instituto Nacional de la Juventud",
    "MERCAL": "Mercado de Alimentos C.A.",
    "PDVSA": "Petróleos de Venezuela S.A.",
    "PEQUIVEN": "Petroquímica de Venezuela S.A.",
    "SAIME": "Servicio Administrativo de Identificación, Migración y Extranjería",
    "SENIAT": "Servicio Nacional Integrado de Administración Aduanera y Tributaria",
    "SUDEBAN": "Superintendencia de las Instituciones del Sector Bancario",
    "SUSCERTE": "Superintendencia de Servicios de Certificación Electrónica",
    "DGCIM": "Dirección General de Contrainteligencia Militar",
    "GNB": "Guardia Nacional Bolivariana",
    "DDDHH": "Defensor del Pueblo",
    "ACNUR": "Alto Comisionado de las Naciones Unidas para los Refugiados",
    "BCRA": "Banco Central de la República Argentina",
    "BID": "Banco Interamericano de Desarrollo",
    "BIS": "Bank for International Settlements",
    "CAF": "Corporación Andina de Fomento",
    "CEPAL": "Comisión Económica para América Latina y el Caribe",
    "CIDH": "Comisión Interamericana de Derechos Humanos",
    "CPI": "Corte Penal Internacional",
    "CPIB": "Corrupt Practices Investigation Bureau",
    "FMI": "Fondo Monetario Internacional",
    "FRONTEX": "Agencia Europea de la Guardia de Fronteras y Costas",
    "GAFI": "Grupo de Acción Financiera Internacional",
    "INTERPOL": "Organización Internacional de Policía Criminal",
    "OACNUDH": "Oficina del Alto Comisionado de las Naciones Unidas para los Derechos Humanos",
    "OCDE": "Organización para la Cooperación y el Desarrollo Económicos",
    "OEA": "Organización de los Estados Americanos",
    "PNUD": "Programa de las Naciones Unidas para el Desarrollo",
    "UNESCO": "Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura",
    "BNDES": "Banco Nacional de Desenvolvimento Econômico e Social",
    "CPF": "Central Provident Fund",
    "CSC": "Civil Service College",
    "GPFG": "Government Pension Fund Global",
    "PCA": "Prevention of Corruption Act",
    "PSC": "Public Service Commission",
    "FOIA": "Freedom of Information Act",
    "KPI": "Key Performance Indicator",
    "OPI": "Oferta Pública Inicial",
    "OPA": "Oferta Pública de Adquisición",
    "OCR": "Optical Character Recognition",
    "CLAP": "Comité Local de Abastecimiento y Producción",
}


def is_compound_token(line, pos, sigla):
    """Detect if siglas at position pos is part of a compound like VePass-Firma or Sigla/Sigla."""
    # Check character before
    before = line[pos-1] if pos > 0 else ""
    after_start = pos + len(sigla)
    after = line[after_start:after_start+1] if after_start < len(line) else ""

    if before in ("-", "/", "_") or after in ("-", "/", "_", "."):
        return True
    return False


def line_already_has_expansion(line, sigla, full_name):
    """Check if line contains an expansion of this sigla already (don't double-expand).

    Faster version: precompiled patterns, limited backtracking.
    """
    # Pattern: Full Name (SIGLA)
    p1 = re.escape(full_name) + r"\s*\(" + re.escape(sigla) + r"\)"
    if re.search(p1, line):
        return True
    # Pattern: (SIGLA) (Full Name)
    p2 = r"\(" + re.escape(sigla) + r"\)\s*\(" + re.escape(full_name) + r"\)"
    if re.search(p2, line):
        return True
    # Pattern: **Full Name (SIGLA)**
    p3 = r"\*\*" + re.escape(full_name) + r"\s*\(" + re.escape(sigla) + r"\)" + r"\*\*"
    if re.search(p3, line):
        return True
    # Pattern: **(SIGLA)** followed by (Full Name) -- e.g., "**CNSC** (Comisión Nacional...)"
    p4 = r"\*\*\(" + re.escape(sigla) + r"\)\*\*\s*\(" + re.escape(full_name) + r"\)"
    if re.search(p4, line):
        return True
    # Pattern: **(SIGLA)** followed by parenthesis (any definition)
    p5 = r"\*\*" + re.escape(sigla) + r"\*\*"
    m5 = re.search(p5, line)
    if m5:
        # Tail after bold sigla
        tail = line[m5.end():].lstrip(" :-,.").strip()
        if tail.startswith("("):
            return True
    # Pattern: SIGLA preceded by a significant word from full name in same line
    sig_pattern = rf"\b{re.escape(sigla)}\b"
    m_sig = re.search(sig_pattern, line)
    if m_sig:
        before = line[max(0, m_sig.start()-60):m_sig.start()].lower()
        full_words = full_name.lower().split()
        significant = [w for w in full_words if len(w) > 4]
        if any(w in before for w in significant):
            return True
    return False


def is_in_table(line):
    return line.lstrip().startswith("|")


def detect_frontmatter_bounds(content):
    lines = content.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return (0, i)
    return None


def expand_prose_line(line, seen_siglas, file_siglas_used):
    """Expand sigla in prose line. Apply convention only once per file per sigla."""
    if is_in_table(line):
        # Tables: track siglas used but don't expand
        for sigla in SIGLAS:
            if re.search(rf"\b{re.escape(sigla)}\b", line):
                file_siglas_used.add(sigla)
        return line

    # Skip headings
    if line.lstrip().startswith("#"):
        return line

    # Skip YAML frontmatter
    if line.strip() == "---":
        return line

    # Sort by descending length to handle multi-char siglas first
    sorted_siglas = sorted(SIGLAS.keys(), key=len, reverse=True)
    new_line = line

    for sigla in sorted_siglas:
        if sigla in seen_siglas:
            continue
        full_name = SIGLAS[sigla]
        if line_already_has_expansion(new_line, sigla, full_name):
            seen_siglas.add(sigla)
            file_siglas_used.add(sigla)
            continue
        # Find first whole-word occurrence in line
        pattern = rf"(?<![A-Za-zÁ-Úá-ú0-9]){re.escape(sigla)}(?![A-Za-zÁ-Úá-ú0-9\-/])"
        match = re.search(pattern, new_line)
        if not match:
            continue
        # Check if part of compound
        start, end = match.span()
        if is_compound_token(new_line, start, sigla):
            continue
        # Check if any non-trivial word in the full name precedes the sigla in the same line
        # (e.g., "Régimen RTER" where "Régimen" is in full name "Régimen de Tres...")
        preceding_chars = new_line[:start].rstrip()
        # Last word before sigla
        m_prev = re.search(r"([A-Za-zÁ-Úá-ú]+)\s*$", preceding_chars)
        if m_prev:
            prev_word = m_prev.group(1).lower()
            full_lower = full_name.lower()
            if prev_word and prev_word in full_lower.split():
                # Some word in the full name appears just before the sigla -- already defined in this context
                seen_siglas.add(sigla)
                file_siglas_used.add(sigla)
                continue
        # Replace this first occurrence with "Full Name (SIGLA)"
        new_line = new_line[:start] + f"{full_name} ({sigla})" + new_line[end:]
        seen_siglas.add(sigla)
        file_siglas_used.add(sigla)
    return new_line


def already_has_glosario(content):
    return re.search(r"(?im)^#{1,3}\s+glosario\s+de\s+siglas", content) is not None


def build_glosario_table(used_siglas):
    sig = sorted(used_siglas, key=str.lower)
    lines = ["", "---", "", "## Glosario de siglas", "",
             "| Sigla | Nombre completo |", "|---|---|"]
    for s in sig:
        full = SIGLAS.get(s, "[definición pendiente]")
        full_clean = full.replace("|", "\\|")
        lines.append(f"| **{s}** | {full_clean} |")
    return "\n".join(lines) + "\n"


def process_file(filepath):
    text = filepath.read_text(encoding="utf-8")
    if not text.strip():
        return False, "empty"

    has_any_sigla = any(re.search(rf"\b{re.escape(s)}\b", text) for s in SIGLAS.keys())
    if not has_any_sigla:
        return False, "no sigils"

    # Don't re-process if already has glosario
    if already_has_glosario(text):
        return False, "glosario ya presente"

    lines = text.splitlines()
    new_lines = []
    seen_siglas = set()
    file_siglas_used = set()

    fm_bounds = detect_frontmatter_bounds(text)
    fm_end = fm_bounds[1] if fm_bounds else -1

    in_codeblock = False
    for idx, line in enumerate(lines):
        # Track code block state
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_codeblock = not in_codeblock
            new_lines.append(line)
            continue
        if in_codeblock:
            new_lines.append(line)
            continue
        # Frontmatter
        if fm_bounds and fm_bounds[0] <= idx <= fm_end:
            new_lines.append(line)
            continue
        # Expand prose
        expanded = expand_prose_line(line, seen_siglas, file_siglas_used)
        new_lines.append(expanded)

    new_content = "\n".join(new_lines)
    if not already_has_glosario(new_content):
        glosario = build_glosario_table(file_siglas_used)
        if not new_content.endswith("\n"):
            new_content += "\n"
        new_content = new_content.rstrip() + "\n" + glosario + "\n"

    if new_content == text:
        return False, "no changes"

    filepath.write_text(new_content, encoding="utf-8")
    return True, f"applied ({len(file_siglas_used)} siglas)"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Single file")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.file:
        paths = [REPO / args.file]
    elif args.all:
        skip_subdirs = {".git", "anexos"}
        paths = []
        for p in REPO.rglob("*.md"):
            if any(s in p.parts for s in skip_subdirs):
                continue
            paths.append(p)
    else:
        print("Specify --file or --all")
        sys.exit(1)

    paths = sorted(set(paths))
    changed = 0
    for p in paths:
        rel = p.relative_to(REPO)
        try:
            ok, msg = process_file(p)
            print(f"{'✓ CHANGED' if ok else 'SKIP':10s} {rel}: {msg}")
            if ok:
                changed += 1
        except Exception as e:
            print(f"ERROR  {rel}: {e}")
            import traceback
            traceback.print_exc()
    print(f"\n{changed} archivos modificados de {len(paths)} totales")


if __name__ == "__main__":
    main()
