import random
from collections import Counter

import matplotlib.pyplot as plt


ANALYTICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def simulate_rolls(n=1_000_000, seed=None):
    """Simulate rolls of two dice and return counts and probabilities by sum."""
    if seed is not None:
        random.seed(seed)

    results = [
        random.randint(1, 6) + random.randint(1, 6)
        for _ in range(n)
    ]
    counts = Counter(results)
    probabilities = {total: counts[total] / n for total in range(2, 13)}
    return counts, probabilities


def compare_probabilities(probabilities):
    """Compare Monte Carlo probabilities with analytical dice probabilities."""
    rows = []
    for total in range(2, 13):
        monte_carlo = probabilities[total]
        analytical = ANALYTICAL_PROBABILITIES[total]
        rows.append(
            {
                "sum": total,
                "monte_carlo": monte_carlo,
                "analytical": analytical,
                "difference": abs(monte_carlo - analytical),
            }
        )
    return rows


def print_table(rows):
    """Print a formatted probability comparison table."""
    print("Sum | Monte Carlo | Analytical | Difference")
    print("--------------------------------------------")
    for row in rows:
        print(
            f"{row['sum']:>3} | "
            f"{row['monte_carlo'] * 100:>10.2f}% | "
            f"{row['analytical'] * 100:>9.2f}% | "
            f"{row['difference'] * 100:>9.2f}%"
        )


def plot_probabilities(rows):
    """Plot Monte Carlo and analytical probabilities side by side."""
    sums = [row["sum"] for row in rows]
    monte_carlo = [row["monte_carlo"] * 100 for row in rows]
    analytical = [row["analytical"] * 100 for row in rows]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([value - 0.2 for value in sums], monte_carlo, width=0.4, label="Monte Carlo")
    ax.bar([value + 0.2 for value in sums], analytical, width=0.4, label="Analytical")
    ax.set_xlabel("Sum of two dice")
    ax.set_ylabel("Probability, %")
    ax.set_title("Monte Carlo dice probabilities vs analytical probabilities")
    ax.set_xticks(sums)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    return fig, ax


def main():
    """Run the Monte Carlo simulation, print the table, and show the plot."""
    rolls = 1_000_000
    _, probabilities = simulate_rolls(rolls)
    rows = compare_probabilities(probabilities)
    print_table(rows)
    plot_probabilities(rows)
    plt.show()


if __name__ == "__main__":
    main()
