import numpy as np

def generate_sample_bond_data():
    # Simulate 5 bonds
    bond_ids = [f"Bond{i}" for i in range(1, 6)]

    expected_returns = np.array([0.03, 0.025, 0.04, 0.035, 0.028])  # annualized
    covariance_matrix = np.array([
        [0.001, 0.0002, 0.0001, 0.0003, 0.0002],
        [0.0002, 0.0012, 0.0003, 0.0002, 0.0001],
        [0.0001, 0.0003, 0.0011, 0.0004, 0.0003],
        [0.0003, 0.0002, 0.0004, 0.0013, 0.0004],
        [0.0002, 0.0001, 0.0003, 0.0004, 0.0012],
    ])
    durations = np.array([2.1, 3.5, 4.0, 5.2, 2.8])

    return bond_ids, expected_returns, covariance_matrix, durations
