from pathlib import Path

import pandas as pd

def load_dataset(file_path: str) -> pd.DataFrame:
    """Load CSV File"""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    if path.suffix.lower() == '.csv':
        df = pd.read_csv(path)
    
    elif path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(path)

    else:
        raise ValueError(
            "Unsupported file format. "
            "Use CSV or Excel."
        )

    return df