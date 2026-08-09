import numpy as np

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def gradient_descent(f, df, x_init, learning_rate=0.01, iterations=100):
    x = x_init
    history = [x]
    
    for i in range(iterations):
        grad = df(x)
        x = x - learning_rate * grad
        history.append(x)
    
    return x, history

def compute_gradient(cost_function, params, h=1e-5):
    grad = np.zeros_like(params)
    for i in range(len(params)):
        params_plus = params.copy()
        params_minus = params.copy()
        params_plus[i] += h
        params_minus[i] -= h
        grad[i] = (cost_function(params_plus) - cost_function(params_minus)) / (2 * h)
    return grad
