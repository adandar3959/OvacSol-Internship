import numpy as np

def matrix_add(m1, m2):
    return np.array(m1) + np.array(m2)

def matrix_multiply(m1, m2):
    return np.dot(m1, m2)

def transpose(m):
    return np.array(m).T

def determinant(m):
    return np.linalg.det(m)

def inverse(m):
    return np.linalg.inv(m)

def solve_linear_system(A, b):
    return np.linalg.solve(A, b)
