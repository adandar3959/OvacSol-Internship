import numpy as np

def vector_add(v1, v2):
    return np.array(v1) + np.array(v2)

def vector_subtract(v1, v2):
    return np.array(v1) - np.array(v2)

def dot_product(v1, v2):
    return np.dot(v1, v2)

def magnitude(v):
    return np.sqrt(np.sum(np.array(v) ** 2))
