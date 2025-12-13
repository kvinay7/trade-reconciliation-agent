from pydantic import BaseModel
from typing import Dict, List

class CanonicalSchema(BaseModel):
    canonical_fields: List[str]
    column_mapping: Dict[str, str]
    descriptions: Dict[str, str]

class NormalizationMapping(BaseModel):
    mapping: Dict[str, str]
