import json
import pandas as pd
from lib.llm.factory import get_llm
from lib.llm.models import NormalizationMapping

def normalize_to_canonical(canonical_schema, source_schema, df):
    prompt = f"""
Canonical schema:
{canonical_schema.model_dump_json(indent=2)}

Source schema:
{json.dumps(source_schema, indent=2)}

Return JSON strictly matching:
{NormalizationMapping.model_json_schema()}
"""

    llm = get_llm()
    raw = llm.invoke(prompt)
    mapping = NormalizationMapping.model_validate_json(raw)

    normalized = {}
    for src, canon in mapping.mapping.items():
        if src in df.columns:
            normalized[canon] = df[src]

    return pd.DataFrame(normalized)
