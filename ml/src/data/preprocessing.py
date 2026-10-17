import pandas as pd


def validate_dataset(df: pd.DataFrame) -> None:
    """
    Perform basic dataset validation.
    """

    if df.empty:
        raise ValueError("Dataset is empty.")

    if df.shape[1] < 2:
        raise ValueError(
            "Dataset must contain at least two columns."
        )

    print("Dataset validation passed.")


def get_dataset_summary(df: pd.DataFrame) -> dict:
    """
    Return basic dataset information.
    """

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
    }