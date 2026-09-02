# Model Performance & Insights

## Dataset Summary

- **Samples**: 1,200 rows
- **Features**: 8 numerical predictors (MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude)
- **Target**: `HousePrice` (Median value in $100,000s)

---

## Model Performance

| Metric | Simple Linear Regression (`MedInc`) | Multiple Linear Regression (All) |
| :--- | :--- | :--- |
| **Train RMSE** | 0.4291 | **0.3662** |
| **Test RMSE** | 0.4101 | **0.3601** |
| **Train R²** | 0.7798 | **0.8397** |
| **Test R²** | 0.7827 | **0.8325** |
| **Test MAE** | 0.3156 | **0.2710** |
| **Adjusted R²** | N/A | **0.8267** |

---

## Key Insights

1. **Multiple Regression Improvement**: Adding all features increased Test R² from `0.7827` to `0.8325` and reduced Test RMSE by 12.2%.
2. **Dominant Feature**: `MedInc` (Median Income) has the strongest positive impact on house prices (standardized coef = `0.7138`).
3. **No Overfitting**: Train R² (`0.8397`) and Test R² (`0.8325`) are closely aligned, proving strong model generalization on unseen data.
4. **Gradient Descent**: Custom implementation converged to minimum MSE cost (`J = 0.0905`) within 100 iterations.

---

## Visualizations Generated

- `charts/01_feature_correlations.png` - Correlation heatmap
- `charts/02_actual_vs_predicted.png` - Actual vs predicted scatter plot
- `charts/03_residuals_distribution.png` - Residual error distribution & fitted plot
- `charts/04_feature_coefficients.png` - Standardized feature coefficients
- `charts/05_simple_vs_multiple_regression.png` - Performance comparison
- `charts/06_gradient_descent_convergence.png` - Cost function convergence curve
