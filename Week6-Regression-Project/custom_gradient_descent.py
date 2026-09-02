import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_gradient_descent_demo():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'housing_data.csv')
    charts_dir = os.path.join(script_dir, 'charts')
    os.makedirs(charts_dir, exist_ok=True)

    print("=" * 70)
    print("      GRADIENT DESCENT FROM SCRATCH (LINEAR REGRESSION CORE)     ")
    print("=" * 70)

    if not os.path.exists(data_path):
        from generate_dataset import generate_housing_dataset
        df = generate_housing_dataset()
        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)

    # Use MedInc feature for 1D Gradient Descent visualization
    X = df[['MedInc']].values
    y = df['HousePrice'].values.reshape(-1, 1)

    # Standardize X for smooth gradient step sizes
    X_mean = np.mean(X)
    X_std = np.std(X)
    X_scaled = (X - X_mean) / X_std

    # Add column of 1s for Intercept (theta_0)
    m = len(y)
    X_b = np.c_[np.ones((m, 1)), X_scaled]

    # Hyperparameters
    learning_rate = 0.05
    n_iterations = 100

    # Initialize weights randomly
    np.random.seed(42)
    theta = np.random.randn(2, 1)

    cost_history = []
    theta_history = [theta.copy()]

    print(f"Initial Random Weights: theta_0 (intercept) = {theta[0,0]:.4f}, theta_1 (slope) = {theta[1,0]:.4f}")
    print(f"Learning Rate alpha = {learning_rate} | Total Iterations = {n_iterations}\n")

    # Gradient Descent Optimization Loop
    for iteration in range(1, n_iterations + 1):
        # 1. Predictions: h_theta(X) = X * theta
        predictions = X_b @ theta
        
        # 2. Errors: h_theta(X) - y
        errors = predictions - y
        
        # 3. Cost Function J(theta) = 1/(2m) * sum((predictions - y)^2)
        cost = (1 / (2 * m)) * np.sum(errors ** 2)
        cost_history.append(cost)

        # 4. Compute Gradients: grad = (1/m) * X^T * (predictions - y)
        gradients = (1 / m) * (X_b.T @ errors)

        # 5. Parameter Update Rule: theta = theta - alpha * gradients
        theta = theta - learning_rate * gradients
        theta_history.append(theta.copy())

        if iteration in [1, 5, 10, 25, 50, 100]:
            print(f"Iteration {iteration:3d} | Cost J(theta): {cost:.6f} | theta_0: {theta[0,0]:.4f} | theta_1: {theta[1,0]:.4f}")

    print("\nFinal Optimized Weights:")
    print(f"Intercept (theta_0): {theta[0,0]:.4f}")
    print(f"Slope     (theta_1): {theta[1,0]:.4f}")

    # Plot Cost Function Convergence Curve
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, n_iterations + 1), cost_history, color='#e63946', linewidth=2.5, label='MSE Cost J(theta)')
    plt.title('Gradient Descent Cost Convergence Curve', fontsize=13, fontweight='bold')
    plt.xlabel('Iteration Step', fontsize=11, fontweight='bold')
    plt.ylabel('Cost Function J(theta)', fontsize=11, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    chart_gd_path = os.path.join(charts_dir, '06_gradient_descent_convergence.png')
    plt.savefig(chart_gd_path, dpi=300)
    plt.close()
    print(f"\n[SAVED] Convergence Plot: {chart_gd_path}")
    print("=" * 70)

if __name__ == '__main__':
    run_gradient_descent_demo()
