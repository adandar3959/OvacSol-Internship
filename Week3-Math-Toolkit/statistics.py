import numpy as np
from collections import Counter

def mean(data):
    return np.mean(data)

def median(data):
    return np.median(data)

def mode(data):
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [k for k, v in counter.items() if v == max_count]
    return modes[0] if len(modes) == 1 else modes

def variance(data):
    return np.var(data, ddof=1)

def std_deviation(data):
    return np.std(data, ddof=1)
