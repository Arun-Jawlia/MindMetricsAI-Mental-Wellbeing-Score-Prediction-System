import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived features required by the ML pipeline.

    Dataset-specific transformations should be added here.
    """

    df = df.copy()

    # Example:
    # df["sleep_stress_ratio"] = (
    #     df["sleep_hours"] /
    #     (df["stress_level"] + 1)
    # )

    return df