#!/usr/bin/env python3
"""Create the English public tables from the local review workspace.

This is a provenance utility: the public analysis pipeline consumes the
English files under data/ and does not depend on Zotero or local attachments.
"""
from __future__ import annotations

import argparse
import csv
import re
import shutil
from difflib import SequenceMatcher
from pathlib import Path

SCALAR = {
    "Nao Especificado": "Unspecified", "Não Especificado": "Unspecified",
    "Nao se aplica": "Not applicable", "Não se aplica": "Not applicable",
    "Sim": "Yes", "Nao": "No", "Não": "No",
    "Simulacao": "Simulation", "Simulação": "Simulation",
    "Hibrido": "Hybrid", "Híbrido": "Hybrid", "Outros": "Other",
    "Outras": "Other", "Outra": "Other", "Texto": "Text", "Voz": "Voice",
    "Domestico": "Domestic", "Doméstico": "Domestic", "Hospitalar": "Hospital",
    "Submarino": "Underwater", "Veicular": "Vehicular", "Colaborativo": "Collaborative",
    "Geral": "General", "Baixa": "Low", "Media": "Medium", "Média": "Medium",
    "Alta": "High", "Muito Alta": "Very high", "Nenhum": "None",
}
CHALLENGE = {
    "Vies": "Bias", "Complexidade": "Complexity", "Janela de contexto": "Context window",
    "Alucinacao": "Hallucination", "Latencia": "Latency", "Perda de contexto/estado": "Context/state loss",
    "Interpretacao incorreta": "Misinterpretation", "Erro de execucao/grounding": "Execution/grounding error",
    "Raciocinio espacial": "Spatial reasoning", "Generalizacao": "Generalization",
    "Ambiguidade": "Ambiguity", "Grounding (ancoragem)": "Grounding (anchoring)",
    "Tarefas de longo horizonte": "Long-horizon tasks", "Tempo real": "Real-time constraints",
    "Interrupcao": "Interruption", "Restricoes fisicas": "Physical constraints",
    "Erros de asr (voz)": "ASR errors (speech)", "Oclusao visual": "Visual occlusion",
    "Seguranca": "Safety", "Viabilidade fisica/colisao": "Physical feasibility/collision",
    "Sim-to-real gap": "Sim-to-real gap", "Falta de datasets": "Dataset scarcity",
    "Falha de planejamento": "Planning failure", "Erro de localizacao/objeto": "Localization/object error",
    "Ambientes dinamicos": "Dynamic environments", "Repeticao de respostas": "Repetitive responses",
}
FREE_TEXT = {
    "Prompt Engineering para alinhamento de valores eticos; Modelo formal (em consideracao) para raciocinio estruturado":
        "Prompt engineering for ethical-value alignment; formal model under consideration for structured reasoning",
    "LTL symbolic planner (myopic, de [32,69]) gera o proximo sub-tarefa NL e restricoes (Sigma_unsafe) para decomposicao hierarquica da missao LTL-NL":
        "LTL symbolic planner (myopic, references [32,69]) generates the next natural-language subtask and constraints for hierarchical LTL-NL mission decomposition",
    "Sintaxe & Viabilidade Logica (Pre-condicoes)": "Syntax and logical feasibility (preconditions)",
    "Alucinacao de argumentos (objetos/localizacoes)": "Argument hallucination (objects/locations)",
    "Explosao Combinatoria & Validade Logica": "Combinatorial explosion and logical validity",
    "Vies em alinhamento de valores e falta de inclusividade cultural": "Bias in value alignment and lack of cultural inclusivity",
    "Erro de Execucao/Grounding (via State Verification)": "Execution/grounding error (via State Verification)",
    "Erro de Localizacao/Objeto (via Object Alignment)": "Localization/object error (via Object Alignment)",
    "Viabilidade Fisica/Colisao (via Spatial Consistency)": "Physical feasibility/collision (via Spatial Consistency)",
    "Alucinacao e incerteza do LLM": "LLM hallucination and uncertainty",
    "Probabilidade de falha da missao (via conformal prediction)": "Mission-failure probability (via conformal prediction)",
}
FIELD_MAP = {
    "ID_Artigo": "study_id", "Titulo_Completo": "title", "Ano_Publicacao": "publication_year", "Autores": "authors",
    "RQ1_Tipo_Interface_Principal": "interface_modality", "RQ1_Detalhes_Interface": "interface_details",
    "RQ2_Usa_LLM": "uses_llm", "RQ2_Modelo_LLM_Familia": "llm_family", "RQ2_Modelo_LLM_Versao": "llm_version",
    "RQ2_Estrategia_Mitigacao": "mitigation_strategy", "RQ3_Realizou_Validacao": "performed_validation",
    "RQ3_Metodo_Validacao": "validation_method", "RQ3_Metricas_Utilizadas": "validation_metrics",
    "Contexto_Dominio_Aplicacao": "application_domain", "Contexto_Plataforma_Robotica": "robotic_platform",
    "RQ5_Desafios_Principais": "main_challenges", "RQ5_Trabalhos_Futuros": "future_work",
    "Papel_Metodo_Simbolico": "symbolic_method_role", "Tipo_Erro_Mitigado": "mitigated_error",
    "Dependencia_Expertise": "required_expertise", "Grupo": "taxonomy_group",
}
EVIDENCE_MAP = {
    "RQ1_Tipo_Interface_Principal": "interface_modality", "RQ1_Detalhes_Interface": "interface_details",
    "RQ2_Usa_LLM": "uses_llm", "RQ2_Modelo_LLM_Familia": "llm_family", "RQ2_Modelo_LLM_Versao": "llm_version",
    "RQ2_Estrategia_Mitigacao": "mitigation_strategy", "RQ3_Realizou_Validacao": "performed_validation",
    "RQ3_Metodo_Validacao": "validation_method", "RQ3_Metricas_Utilizadas": "validation_metrics",
    "Contexto_Dominio_Aplicacao": "application_domain", "Contexto_Plataforma_Robotica": "robotic_platform",
    "RQ5_Desafios_Principais": "main_challenges", "RQ5_Trabalhos_Futuros": "future_work",
    "Papel_Metodo_Simbolico": "symbolic_method_role", "Tipo_Erro_Mitigado": "mitigated_error",
    "Dependencia_Expertise": "required_expertise",
}
BASIS = {
    "A": "LLM use without a formal symbolic parser or verifier.",
    "B": "Lightweight symbolic structure or static translation without formal verification or autonomous recovery.",
    "C": "Formal planning, verification, or unrealizability checking without autonomous execution-recovery feedback.",
    "D": "Formal symbolic verification with an execution-feedback loop that can trigger autonomous replanning.",
}

def clean(value: str) -> str:
    return " ".join((value or "").split()).strip()

def key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", clean(value).lower())

def scalar(value: str) -> str:
    value = clean(value)
    return SCALAR.get(value, value)

def list_value(value: str, mapping: dict[str, str] | None = None) -> str:
    mapping = mapping or {}
    return "; ".join(mapping.get(clean(x), scalar(clean(x))) for x in clean(value).split(";")) if clean(value) else ""

def free(value: str) -> str:
    value = clean(value)
    if value in FREE_TEXT:
        return FREE_TEXT[value]
    if ";" in value:
        return "; ".join(FREE_TEXT.get(part.strip(), scalar(part.strip())) for part in value.split(";"))
    return FREE_TEXT.get(value, scalar(value))

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [{(k or "").lstrip("\ufeff").strip('"'): v for k, v in row.items()} for row in csv.DictReader(handle)]

def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def normalize_extraction(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for source in rows:
        row = {}
        for old, new in FIELD_MAP.items():
            value = source.get(old, "")
            if old == "RQ5_Desafios_Principais": value = list_value(value, CHALLENGE)
            elif old == "RQ2_Estrategia_Mitigacao": value = list_value(value)
            elif old in ("Papel_Metodo_Simbolico", "Tipo_Erro_Mitigado"): value = free(value)
            else: value = scalar(value)
            row[new] = value
        row["classification_note"] = BASIS.get(row["taxonomy_group"], "")
        for old, new in EVIDENCE_MAP.items():
            row[f"evidence_{new}"] = clean(source.get(f"evidence_{old}", ""))
        # Manual completion verified against the Patton et al. PDF; the source CSV
        # left this one interface-detail field blank.
        if row["study_id"] == "Patton2024":
            row["interface_details"] = "Programming-by-Demonstration traces for programmatic learning from demonstration."
            row["evidence_interface_details"] = '"learning more complex programs from demonstration traces"'
        output.append(row)
    return output

def normalize_screening(path: Path, output: Path) -> None:
    rows = read_csv(path)
    decisions = {"Incluir": "include", "Excluir": "exclude", "Incerto (Potencialmente Excluir)": "uncertain (potential exclusion)"}
    for row in rows:
        row["screening_decision"] = decisions.get(row.get("screening_decision", ""), row.get("screening_decision", ""))
    write_csv(output, rows, list(rows[0]))

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extraction", type=Path, required=True)
    parser.add_argument("--final", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("."))
    args = parser.parse_args()
    output = args.output

    extraction = normalize_extraction(read_csv(args.extraction))
    extraction_fields = list(extraction[0])
    write_csv(output / "data/extraction/study_extraction.csv", extraction, extraction_fields)

    final = read_csv(args.final)
    by_title = {key(row["title"]): row for row in extraction}
    studies = []
    for source in final:
        title = clean(source.get("Title", ""))
        match = by_title.get(key(title))
        if not match:
            candidates = sorted(((SequenceMatcher(None, key(title), key(row["title"])).ratio(), row) for row in extraction), key=lambda item: item[0])
            if candidates and candidates[-1][0] >= 0.82: match = candidates[-1][1]
        excluded = bool(re.search(r"Humanoid Robotics Powered|A Walk to Remember|Hi AirStar", title, re.I))
        if not match and not excluded:
            raise ValueError(f"Could not match included record: {title}")
        if excluded:
            study_id = {"Humanoid": "Smith2025", "Walk to Remember": "Vitharana2025", "Hi AirStar": "Wang2025HiAirStar"}[next(x for x in ("Humanoid", "Walk to Remember", "Hi AirStar") if x in title)]
            reason = "Full-text exclusion; see the screening decision table."
            status = "excluded_full_text"
        else:
            study_id, reason, status = match["study_id"], "", "included"
        studies.append({"study_id": study_id, "screening_status": status, "exclusion_reason": reason, "title": title,
                        "authors": clean(source.get("Author", "")), "publication_year": clean(source.get("Publication Year", "")),
                        "publication_date": clean(source.get("Date", "")), "item_type": clean(source.get("Item Type", "")),
                        "publication_title": clean(source.get("Publication Title", "")), "doi": clean(source.get("DOI", "")),
                        "url": clean(source.get("Url", ""))})
    write_csv(output / "data/studies.csv", studies, list(studies[0]))
    write_csv(output / "data/screening/full_text_decisions.csv", [{k: row[k] for k in ("study_id", "screening_status", "exclusion_reason", "title", "doi")} for row in studies], ["study_id", "screening_status", "exclusion_reason", "title", "doi"])

    archive = args.archive
    normalize_screening(archive / "screening/all_records.csv", output / "data/screening/all_records.csv")
    normalize_screening(archive / "screening/first_screening.csv", output / "data/screening/first_screening.csv")
    imported = read_csv(archive / "search/imported_records.csv")
    source_names = {
        "Busca 1 - Central (ACM).csv": "query_1_central_acm.csv", "Busca 1 - Central (IEEEX).csv": "query_1_central_ieeex.csv", "Busca 1 - Central (Scopus).csv": "query_1_central_scopus.csv",
        "Busca 2 - VLA (ACM).csv": "query_2_vla_acm.csv", "Busca 2 - VLA (IEEEX).csv": "query_2_vla_ieeex.csv", "Busca 2 - VLA (Scopus).csv": "query_2_vla_scopus.csv",
        "Busca 3 - Robótica Hospitalar (IEEEX).csv": "query_3_hospital_robotics_ieeex.csv", "Busca 3 - Robótica Hospitalar (Scopus).csv": "query_3_hospital_robotics_scopus.csv",
    }
    for row in imported: row["source_file"] = source_names.get(row.get("source_file", ""), row.get("source_file", ""))
    write_csv(output / "data/search/imported_records.csv", imported, list(imported[0]))
    for name in ("database_yields.csv", "search_strings.md"):
        (output / "data/search").mkdir(parents=True, exist_ok=True)
        shutil.copy2(archive / "search" / name, output / "data/search" / name)

    tax = [{"study_id": row["study_id"], "title": row["title"], "taxonomy_group": row["taxonomy_group"],
            "classification_basis": row["classification_note"], "symbolic_method_role": row["symbolic_method_role"],
            "mitigated_error": row["mitigated_error"]} for row in extraction]
    write_csv(output / "data/extraction/taxonomy_membership.csv", tax, list(tax[0]))
    print(f"normalized {len(extraction)} extraction rows and {len(studies)} full-text records")

if __name__ == "__main__":
    main()
