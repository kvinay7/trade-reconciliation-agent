import json
from lib.llm.factory import get_llm
from lib.llm.models import CanonicalSchema
from lib.schema_extractor import extract_schema

def generate_canonical_schema(df):
    schema_info = extract_schema(df)

    prompt = f"""
You are a financial data expert.

CSV schema & samples:
{json.dumps(schema_info, indent=2)}

Return JSON strictly matching:
{CanonicalSchema.model_json_schema()}
"""

    llm = get_llm()
    raw = llm.invoke(prompt)

    return CanonicalSchema.model_validate_json(raw)
