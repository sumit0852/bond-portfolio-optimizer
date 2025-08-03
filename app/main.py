from data import generate_sample_bond_data
from optimizer import optimize_portfolio

def main():
    bond_ids, returns, cov, durations = generate_sample_bond_data()
    weights = optimize_portfolio(returns, cov, durations)

    print("🔍 Optimal Bond Portfolio Weights:\n")
    for i, w in zip(bond_ids, weights):
        print(f"{i}: {w:.2%}")

if __name__ == "__main__":
    main()
