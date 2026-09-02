import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication style for matplotlib/seaborn
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# Ensure scikit-learn compatibility layer (imports sklearn if available, else numpy fallback)
try:
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    
    # Check for root_mean_squared_error (scikit-learn 1.4+)
    try:
        from sklearn.metrics import root_mean_squared_error
    except ImportError:
        def root_mean_squared_error(y_true, y_pred):
            return np.sqrt(mean_squared_error(y_true, y_pred))
            
    USING_SKLEARN_NATIVE = True
    print("[INFO] Using native scikit-learn library.")
except ImportError:
    USING_SKLEARN_NATIVE = False
    print("[INFO] scikit-learn not found in current environment. Using NumPy/SciPy ML core layer.")

    def train_test_split(X, y, test_size=0.2, random_state=42):
        if random_state is not None:
            np.random.seed(random_state)
        n_samples = len(X)
        n_test = int(n_samples * test_size)
        shuffled_indices = np.random.permutation(n_samples)
        test_indices = shuffled_indices[:n_test]
        train_indices = shuffled_indices[n_test:]
        
        if isinstance(X, pd.DataFrame) or isinstance(X, pd.Series):
            X_train, X_test = X.iloc[train_indices], X.iloc[test_indices]
        else:
            X_train, X_test = X[train_indices], X[test_indices]
            
        if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
            y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]
        else:
            y_train, y_test = y[train_indices], y[test_indices]
            
        return X_train, X_test, y_train, y_test

    class StandardScaler:
        def __init__(self):
            self.mean_ = None
            self.scale_ = None
            
        def fit(self, X):
            X_arr = np.asarray(X)
            self.mean_ = np.mean(X_arr, axis=0)
            self.scale_ = np.std(X_arr, axis=0, ddof=0)
            self.scale_[self.scale_ == 0] = 1.0
            return self

        def transform(self, X):
            X_arr = np.asarray(X)
            return (X_arr - self.mean_) / self.scale_

        def fit_transform(self, X):
            return self.fit(X).transform(X)

    class LinearRegression:
        def __init__(self):
            self.coef_ = None
            self.intercept_ = None

        def fit(self, X, y):
            X_arr = np.asarray(X)
            y_arr = np.asarray(y)
            
            if X_arr.ndim == 1:
                X_arr = X_arr.reshape(-1, 1)
                
            # Add bias term (column of 1s)
            X_b = np.c_[np.ones((X_arr.shape[0], 1)), X_arr]
            
            # Normal Equation: theta = (X^T * X)^(-1) * X^T * y
            theta = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y_arr
            
            self.intercept_ = theta[0]
            self.coef_ = theta[1:]
            return self

        def predict(self, X):
            X_arr = np.asarray(X)
            if X_arr.ndim == 1:
                X_arr = X_arr.reshape(-1, 1)
            return X_arr @ self.coef_ + self.intercept_

    def mean_squared_error(y_true, y_pred):
        return float(np.mean((np.asarray(y_true) - np.asarray(y_pred)) ** 2))

    def root_mean_squared_error(y_true, y_pred):
        return float(np.sqrt(mean_squared_error(y_true, y_pred)))

    def mean_absolute_error(y_true, y_pred):
        return float(np.mean(np.abs(np.asarray(y_true) - np.asarray(y_pred))))

    def r2_score(y_true, y_pred):
        y_t = np.asarray(y_true)
        y_p = np.asarray(y_pred)
        ss_res = np.sum((y_t - y_p) ** 2)
        ss_tot = np.sum((y_t - np.mean(y_t)) ** 2)
        if ss_tot == 0:
            return 1.0
        return float(1.0 - (ss_res / ss_tot))

def calculate_adjusted_r2(r2, n, p):
    """Calculates Adjusted R-squared metric."""
    if n - p - 1 <= 0:
        return r2
    return 1.0 - (1.0 - r2) * (n - 1) / (n - p - 1)

def run_regression_analysis():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'housing_data.csv')
    charts_dir = os.path.join(script_dir, 'charts')
    os.makedirs(charts_dir, exist_ok=True)

    print("=" * 70)
    print("        WEEK 6: SUPERVISED LEARNING - REGRESSION PROJECT       ")
    print("=" * 70)

    # 1. Load Data
    if not os.path.exists(data_path):
        from generate_dataset import generate_housing_dataset
        df = generate_housing_dataset()
        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)

    print(f"\n[1] DATASET OVERVIEW ({data_path})")
    print(f"Total Rows (Instances): {df.shape[0]}")
    print(f"Total Columns (Features + Target): {df.shape[1]}")
    print("\nDataset Summary Statistics:")
    print(df.describe().T[['mean', 'std', 'min', '50%', 'max']])

    # Target & Feature definitions
    target_col = 'HousePrice'
    feature_cols = [c for c in df.columns if c != target_col]

    X = df[feature_cols]
    y = df[target_col]

    # 2. Exploratory Data Analysis & Correlation Visualization
    correlations = df.corr()[target_col].sort_values(ascending=False)
    print("\n[2] FEATURE CORRELATIONS WITH HOUSE PRICE:")
    print(correlations)

    # Chart 1: Feature Correlations Heatmap
    plt.figure(figsize=(10, 7))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap=cmap, linewidths=0.5, vmin=-1, vmax=1)
    plt.title('Feature Correlation Matrix (California Housing Dataset)', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    chart1_path = os.path.join(charts_dir, '01_feature_correlations.png')
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[SAVED] Chart 1: {chart1_path}")

    # 3. Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"\n[3] DATA SPLIT: Train set size = {len(X_train)} | Test set size = {len(X_test)}")

    # 4. Model 1: Simple Linear Regression (Using top correlated feature: MedInc)
    single_feature = 'MedInc'
    X_train_single = X_train[[single_feature]]
    X_test_single = X_test[[single_feature]]

    simple_model = LinearRegression()
    simple_model.fit(X_train_single, y_train)

    y_train_pred_simple = simple_model.predict(X_train_single)
    y_test_pred_simple = simple_model.predict(X_test_single)

    simple_metrics = {
        'Train RMSE': root_mean_squared_error(y_train, y_train_pred_simple),
        'Test RMSE': root_mean_squared_error(y_test, y_test_pred_simple),
        'Train R2': r2_score(y_train, y_train_pred_simple),
        'Test R2': r2_score(y_test, y_test_pred_simple),
        'Test MAE': mean_absolute_error(y_test, y_test_pred_simple)
    }

    # 5. Model 2: Multiple Linear Regression (All Features)
    # Feature Scaling using StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    multiple_model = LinearRegression()
    multiple_model.fit(X_train_scaled, y_train)

    y_train_pred_multi = multiple_model.predict(X_train_scaled)
    y_test_pred_multi = multiple_model.predict(X_test_scaled)

    r2_multi_train = r2_score(y_train, y_train_pred_multi)
    r2_multi_test = r2_score(y_test, y_test_pred_multi)
    n_test = len(y_test)
    p_features = len(feature_cols)

    multi_metrics = {
        'Train RMSE': root_mean_squared_error(y_train, y_train_pred_multi),
        'Test RMSE': root_mean_squared_error(y_test, y_test_pred_multi),
        'Train R2': r2_multi_train,
        'Test R2': r2_multi_test,
        'Adjusted R2': calculate_adjusted_r2(r2_multi_test, n_test, p_features),
        'Test MAE': mean_absolute_error(y_test, y_test_pred_multi),
        'Test MSE': mean_squared_error(y_test, y_test_pred_multi)
    }

    # 6. Display Model Evaluation Results
    print("\n" + "=" * 70)
    print("                     MODEL EVALUATION SUMMARY                    ")
    print("=" * 70)
    print(f"{'Metric':<25} | {'Simple Linear Reg (' + single_feature + ')':<22} | {'Multiple Linear Reg (All)':<22}")
    print("-" * 75)
    print(f"{'Train RMSE':<25} | {simple_metrics['Train RMSE']:<22.4f} | {multi_metrics['Train RMSE']:<22.4f}")
    print(f"{'Test RMSE':<25} | {simple_metrics['Test RMSE']:<22.4f} | {multi_metrics['Test RMSE']:<22.4f}")
    print(f"{'Train R²':<25} | {simple_metrics['Train R2']:<22.4f} | {multi_metrics['Train R2']:<22.4f}")
    print(f"{'Test R²':<25} | {simple_metrics['Test R2']:<22.4f} | {multi_metrics['Test R2']:<22.4f}")
    print(f"{'Test MAE':<25} | {simple_metrics['Test MAE']:<22.4f} | {multi_metrics['Test MAE']:<22.4f}")
    print(f"{'Adjusted R²':<25} | {'N/A':<22} | {multi_metrics['Adjusted R2']:<22.4f}")
    print("=" * 75)

    # 7. Model Feature Coefficients Analysis
    coef_series = pd.Series(multiple_model.coef_, index=feature_cols).sort_values()
    print("\n[5] STANDARDIZED COEFFICIENTS (Feature Importance):")
    print(f"Intercept: {multiple_model.intercept_:.4f}")
    for feature, coef in coef_series.items():
        print(f"  {feature:<12}: {coef:>8.4f}")

    # Chart 2: Actual vs Predicted Scatter Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_test_pred_multi, alpha=0.6, color='#2b5c8f', edgecolors='w', s=50, label='Test Predictions')
    min_val = min(y_test.min(), y_test_pred_multi.min())
    max_val = max(y_test.max(), y_test_pred_multi.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Ideal Prediction Line (y=x)')
    plt.xlabel('Actual House Price ($100k)', fontsize=11, fontweight='bold')
    plt.ylabel('Predicted House Price ($100k)', fontsize=11, fontweight='bold')
    plt.title(f'Actual vs Predicted House Prices (Test R² = {multi_metrics["Test R2"]:.4f})', fontsize=13, fontweight='bold')
    plt.legend(frameon=True, facecolor='white')
    plt.tight_layout()
    chart2_path = os.path.join(charts_dir, '02_actual_vs_predicted.png')
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[SAVED] Chart 2: {chart2_path}")

    # Chart 3: Residual Diagnostics (Distribution & Heteroscedasticity Check)
    residuals = y_test - y_test_pred_multi
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Residuals Histogram
    sns.histplot(residuals, kde=True, ax=axes[0], color='#2a9d8f', bins=30)
    axes[0].axvline(0, color='red', linestyle='--', linewidth=1.5)
    axes[0].set_title('Residuals Error Distribution', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Prediction Error (y_test - y_pred)', fontsize=10)

    # Residuals vs Fitted Scatter
    axes[1].scatter(y_test_pred_multi, residuals, alpha=0.6, color='#e76f51', edgecolors='w', s=50)
    axes[1].axhline(0, color='red', linestyle='--', linewidth=1.5)
    axes[1].set_title('Residuals vs Predicted Values', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Predicted House Price', fontsize=10)
    axes[1].set_ylabel('Residual Error', fontsize=10)

    plt.tight_layout()
    chart3_path = os.path.join(charts_dir, '03_residuals_distribution.png')
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f"[SAVED] Chart 3: {chart3_path}")

    # Chart 4: Standardized Feature Coefficients Bar Plot
    plt.figure(figsize=(9, 5))
    colors = ['#e63946' if c < 0 else '#2a9d8f' for c in coef_series.values]
    bars = plt.barh(coef_series.index, coef_series.values, color=colors, edgecolor='black', alpha=0.85)
    plt.axvline(0, color='black', linestyle='-', linewidth=0.8)
    plt.title('Standardized Regression Coefficients (Feature Impact)', fontsize=13, fontweight='bold')
    plt.xlabel('Standardized Coefficient Weight', fontsize=11, fontweight='bold')
    
    for bar in bars:
        width = bar.get_width()
        offset = 0.01 if width >= 0 else -0.05
        plt.text(width + offset, bar.get_y() + bar.get_height()/2, f'{width:.3f}', 
                 va='center', fontsize=9, fontweight='bold')
                 
    plt.tight_layout()
    chart4_path = os.path.join(charts_dir, '04_feature_coefficients.png')
    plt.savefig(chart4_path, dpi=300)
    plt.close()
    print(f"[SAVED] Chart 4: {chart4_path}")

    # Chart 5: Simple vs Multiple Regression Model Comparison
    plt.figure(figsize=(9, 5))
    categories = ['Simple Linear Regression\n(MedInc)', 'Multiple Linear Regression\n(All Features)']
    r2_scores = [simple_metrics['Test R2'], multi_metrics['Test R2']]
    rmse_scores = [simple_metrics['Test RMSE'], multi_metrics['Test RMSE']]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax1 = plt.subplots(figsize=(8, 5))
    rects1 = ax1.bar(x - width/2, r2_scores, width, label='Test R² (Higher is Better)', color='#457b9d')
    ax2 = ax1.twinx()
    rects2 = ax2.bar(x + width/2, rmse_scores, width, label='Test RMSE (Lower is Better)', color='#e63946')

    ax1.set_ylabel('R² Score', color='#457b9d', fontweight='bold', fontsize=11)
    ax2.set_ylabel('RMSE ($100k)', color='#e63946', fontweight='bold', fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, fontweight='bold')
    ax1.set_ylim(0, 1.0)
    ax2.set_ylim(0, max(rmse_scores) * 1.3)
    
    plt.title('Simple vs Multiple Linear Regression Performance Comparison', fontsize=12, fontweight='bold', pad=15)
    fig.tight_layout()
    chart5_path = os.path.join(charts_dir, '05_simple_vs_multiple_regression.png')
    plt.savefig(chart5_path, dpi=300)
    plt.close()
    print(f"[SAVED] Chart 5: {chart5_path}")

    print("\n[SUCCESS] Regression analysis completed successfully!")
    print("=" * 70)

    # Automatically run Gradient Descent Demo
    from custom_gradient_descent import run_gradient_descent_demo
    run_gradient_descent_demo()

if __name__ == '__main__':
    run_regression_analysis()
