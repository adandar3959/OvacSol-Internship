import numpy as np

def simulate_coin_flips(n_flips):
    results = np.random.choice(['H', 'T'], size=n_flips)
    heads_count = np.sum(results == 'H')
    experimental_prob = heads_count / n_flips
    theoretical_prob = 0.5
    return experimental_prob, theoretical_prob, results

def simulate_dice_rolls(n_rolls):
    results = np.random.randint(1, 7, size=n_rolls)
    experimental_probs = {i: np.sum(results == i) / n_rolls for i in range(1, 7)}
    theoretical_prob = 1/6
    return experimental_probs, theoretical_prob, results
