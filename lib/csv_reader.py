import pandas as pd
from io import BytesIO

def read_csv_any(file_bytes: bytes) -> pd.DataFrame:
    """
    Accept ANY CSV file.
    No schema assumptions.
    """
    df = pd.read_csv(BytesIO(file_bytes))
    df.columns = [c.strip() for c in df.columns]
    return df
