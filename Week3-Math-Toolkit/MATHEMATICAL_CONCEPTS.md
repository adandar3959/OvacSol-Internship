# Mathematical Concepts Used

## 1. Vectors (vectors.py)
- **Addition/Subtraction**: Element-wise operations
- **Dot Product**: v1·v2 = Σ(v1[i] × v2[i])
- **Magnitude**: |v| = √(Σv[i]²)

**Used in**: Linear regression predictions and error calculations

## 2. Matrices (matrices.py)
- **Addition**: Element-wise
- **Multiplication**: Row × column dot products
- **Transpose**: Flip rows/columns (A^T)
- **Determinant**: Matrix scalar value
- **Inverse**: AA⁻¹ = I
- **Linear System**: Solve Ax = b

**Used in**: System of equations, data transformations

## 3. Calculus (calculus.py)
- **Numerical Derivative**: f'(x) ≈ (f(x+h) - f(x-h)) / 2h
- **Gradient**: Vector of partial derivatives
- **Gradient Descent**: x_new = x_old - α × ∇f(x)

**Used in**: Training regression model, minimizing cost function

## 4. Probability (probability.py)
- **Experimental Probability**: (favorable outcomes) / (total trials)
- **Theoretical Probability**: Expected probability
- **Law of Large Numbers**: Convergence with large samples

**Used in**: Coin flips P(H)=0.5, Dice rolls P(face)=1/6

## 5. Statistics (statistics.py)
- **Mean**: μ = Σx / n
- **Median**: Middle value
- **Mode**: Most frequent value
- **Variance**: σ² = Σ(x - μ)² / (n-1)
- **Std Deviation**: σ = √variance

**Used in**: Data analysis and understanding distributions

## 6. Linear Regression (main.py)
**Model**: y = mx + b  
**Cost Function**: MSE = (1/n) × Σ(ŷ - y)²  
**Gradients**:
- ∂MSE/∂m = (2/n) × Σ((mx + b - y) × x)
- ∂MSE/∂b = (2/n) × Σ(mx + b - y)

**Updates**:
- m_new = m_old - α × ∂MSE/∂m
- b_new = b_old - α × ∂MSE/∂b

**Combines**: Calculus (optimization), linear algebra (predictions), statistics (error measurement)

## Summary

| Module | Math Topics | ML Application |
|--------|-------------|----------------|
| Vectors | Linear algebra | Feature representation |
| Matrices | Systems of equations | Data transformations |
| Calculus | Optimization | Model training |
| Probability | Random experiments | Uncertainty |
| Statistics | Data analysis | Performance metrics |
| Regression | All above | Predictive modeling |
