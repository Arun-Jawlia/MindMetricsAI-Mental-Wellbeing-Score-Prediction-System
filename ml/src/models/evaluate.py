from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

import numpy as np


def evaluate_regression(
    y_true,
    y_pred,
) -> dict:

    mae = mean_absolute_error(
        y_true,
        y_pred,
    )

    mse = mean_squared_error(
        y_true,
        y_pred,
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_true,
        y_pred,
    )

    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2,
    }