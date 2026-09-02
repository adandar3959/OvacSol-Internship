# Linear Regression - House Price Prediction

Supervised Learning project building and evaluating Linear & Multiple Regression models using Scikit-Learn.

## Setup & Run

```bash
cd Week6-Regression-Project
python -m venv venv
venv\Scripts\activate
python regression_project.py
```

## Methods & Models

- **Exploratory Data Analysis**: Correlation analysis & feature distributions
- **Simple Linear Regression**: Single predictor (`MedInc`)
- **Multiple Linear Regression**: All features with `StandardScaler`
- **Gradient Descent**: Custom iterative optimization implementation
- **Evaluation Metrics**: RMSE, R², MAE, Adjusted R²

## Key Results

- **Multiple Linear Regression R²**: `0.8325` (83.3% variance explained)
- **Multiple Linear Regression RMSE**: `0.3601` ($36,010 error)
- **Top Predictor**: Median Income (`MedInc`, coef = `0.7138`)

## Output

- `housing_data.csv` - Housing dataset (1,200 samples)
- `charts/` - 6 visualization charts
- `MODEL_PERFORMANCE.md` - Performance summary report
