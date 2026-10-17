"""
MindMetrics AI
ML Training Entry Point
"""
from src.data.loader import load_dataset
from src.data.preprocessing import validate_dataset
from src.features.engineering import create_features


DATA_PATH = "./data/raw/Student Social Media And Mental Health Impact.csv"

def main():

    # 1. Load
    df = load_dataset(DATA_PATH)

    # 2. Validate
    validate_dataset(df)

    # 3. Feature engineering
    df = create_features(df)

    # 4. Select target
    # TARGET = "..."

    # 5. Split
    # X = df.drop(columns=[TARGET])
    # y = df[TARGET]

    # 6. Train models

    # 7. Evaluate models

    # 8. Tune best model

    # 9. Save model

    print("MindMetrics ML pipeline completed.")


if __name__ == "__main__":
    main()