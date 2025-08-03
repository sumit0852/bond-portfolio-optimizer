import numpy as np
from scipy.optimize import minimize

def optimize_portfolio(returns, cov_matrix, durations, max_duration=4.0):
    n = len(returns)

    # Objective: minimize -return + penalty for risk
    def objective(weights):
        ret = np.dot(weights, returns)
        risk = np.dot(weights, np.dot(cov_matrix, weights))
        return -ret + 0.01 * risk  # Minimize negative return + risk penalty

    # Constraints
    constraints = [
        {"type": "eq", "fun": lambda w: np.sum(w) - 1},                         # Weights sum to 1
        {"type": "ineq", "fun": lambda w: max_duration - np.dot(w, durations)} # Duration <= max
    ]

    bounds = [(0, 1) for _ in range(n)]  # No shorting, max 100% per bond
    init_weights = np.ones(n) / n        # Start with equal weights

    result = minimize(objective, init_weights, method='SLSQP',
                      bounds=bounds, constraints=constraints)

    if not result.success:
        raise ValueError("Optimization failed: " + result.message)

    return result.x
