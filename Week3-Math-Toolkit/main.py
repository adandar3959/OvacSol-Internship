import numpy as np
import matplotlib.pyplot as plt
import os
from vectors import vector_add, vector_subtract, dot_product, magnitude
from matrices import matrix_add, matrix_multiply, transpose, determinant, inverse, solve_linear_system
from calculus import numerical_derivative, gradient_descent, compute_gradient
from probability import simulate_coin_flips, simulate_dice_rolls
from statistics import mean, median, mode, variance, std_deviation

os.makedirs('charts', exist_ok=True)

print("=" * 60)
print("MATHEMATICAL FOUNDATIONS TOOLKIT FOR AI")
print("=" * 60)

print("\n1. VECTOR OPERATIONS")
print("-" * 60)
v1 = [3, 4]
v2 = [1, 2]
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {vector_add(v1, v2)}")
print(f"v1 - v2 = {vector_subtract(v1, v2)}")
print(f"v1 · v2 = {dot_product(v1, v2)}")
print(f"|v1| = {magnitude(v1):.2f}")

print("\n2. MATRIX OPERATIONS")
print("-" * 60)
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(f"A = \n{np.array(A)}")
print(f"B = \n{np.array(B)}")
print(f"A + B = \n{matrix_add(A, B)}")
print(f"A × B = \n{matrix_multiply(A, B)}")
print(f"A^T = \n{transpose(A)}")
print(f"det(A) = {determinant(A):.2f}")

print("\n3. LINEAR SYSTEM SOLVER")
print("-" * 60)
A_sys = [[2, 1], [1, 3]]
b_sys = [8, 13]
x_solution = solve_linear_system(A_sys, b_sys)
print(f"System: Ax = b")
print(f"A = \n{np.array(A_sys)}")
print(f"b = {b_sys}")
print(f"Solution x = {x_solution}")

print("\n4. CALCULUS - GRADIENT DESCENT")
print("-" * 60)
def quadratic(x):
    return x**2 + 4*x + 4

def quadratic_derivative(x):
    return 2*x + 4

x_min, history = gradient_descent(quadratic, quadratic_derivative, x_init=10, learning_rate=0.1, iterations=50)
print(f"Function: f(x) = x² + 4x + 4")
print(f"Starting point: x = 10")
print(f"Minimum found at: x = {x_min:.4f}")
print(f"Minimum value: f(x) = {quadratic(x_min):.4f}")

print("\n5. PROBABILITY SIMULATION")
print("-" * 60)
exp_prob, theo_prob, coin_results = simulate_coin_flips(1000)
print(f"Coin flips (n=1000)")
print(f"Experimental P(Heads) = {exp_prob:.4f}")
print(f"Theoretical P(Heads) = {theo_prob:.4f}")
print(f"Difference = {abs(exp_prob - theo_prob):.4f}")

exp_dice, theo_dice, dice_results = simulate_dice_rolls(1000)
print(f"\nDice rolls (n=1000)")
for face in range(1, 7):
    print(f"P(Face={face}): Experimental={exp_dice[face]:.4f}, Theoretical={theo_dice:.4f}")

print("\n6. STATISTICS")
print("-" * 60)
data = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
print(f"Dataset: {data}")
print(f"Mean = {mean(data):.2f}")
print(f"Median = {median(data):.2f}")
print(f"Mode = {mode(data)}")
print(f"Variance = {variance(data):.2f}")
print(f"Standard Deviation = {std_deviation(data):.2f}")

print("\n7. LINEAR REGRESSION FROM SCRATCH")
print("-" * 60)

np.random.seed(42)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = 2.5 * X + 3 + np.random.randn(10) * 2

def predict(X, m, b):
    return m * X + b

def mse_cost(params):
    m, b = params
    predictions = predict(X, m, b)
    return np.mean((predictions - y) ** 2)

m, b = 0.0, 0.0
learning_rate = 0.01
iterations = 1000

for i in range(iterations):
    predictions = predict(X, m, b)
    error = predictions - y
    m_grad = (2/len(X)) * np.sum(error * X)
    b_grad = (2/len(X)) * np.sum(error)
    m = m - learning_rate * m_grad
    b = b - learning_rate * b_grad

print(f"Trained Linear Regression: y = {m:.2f}x + {b:.2f}")
print(f"True relationship: y = 2.5x + 3")
print(f"Final MSE: {mse_cost([m, b]):.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Data points', s=50)
plt.plot(X, predict(X, m, b), color='red', linewidth=2, label=f'Regression: y={m:.2f}x+{b:.2f}')
plt.xlabel('X', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Linear Regression from Scratch (Gradient Descent)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('charts/regression_plot.png', dpi=300)
print("\nRegression plot saved to 'charts/regression_plot.png'")

plt.figure(figsize=(10, 6))
faces = list(exp_dice.keys())
exp_probs = list(exp_dice.values())
theo_probs = [theo_dice] * 6
x_pos = np.arange(len(faces))
width = 0.35
plt.bar(x_pos - width/2, exp_probs, width, label='Experimental', color='skyblue')
plt.bar(x_pos + width/2, theo_probs, width, label='Theoretical', color='orange')
plt.xlabel('Dice Face', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title('Dice Roll Probability Distribution', fontsize=14, fontweight='bold')
plt.xticks(x_pos, faces)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('charts/probability_distribution.png', dpi=300)
print("Probability distribution saved to 'charts/probability_distribution.png'")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE!")
print("=" * 60)
