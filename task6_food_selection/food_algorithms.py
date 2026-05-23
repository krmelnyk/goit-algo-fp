ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """Select food items greedily by the best calories-to-cost ratio."""
    items_sorted = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )
    total_cost = 0
    total_calories = 0
    chosen = []

    for item, data in items_sorted:
        if total_cost + data["cost"] <= budget:
            chosen.append(item)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    """Find the optimal food set using 0/1 knapsack dynamic programming."""
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = names[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        for current_budget in range(budget + 1):
            dp[i][current_budget] = dp[i - 1][current_budget]
            if cost <= current_budget:
                candidate = dp[i - 1][current_budget - cost] + calories
                dp[i][current_budget] = max(dp[i][current_budget], candidate)

    chosen = []
    current_budget = budget
    for i in range(n, 0, -1):
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            item = names[i - 1]
            chosen.append(item)
            current_budget -= items[item]["cost"]

    chosen.reverse()
    total_cost = sum(items[item]["cost"] for item in chosen)
    total_calories = dp[n][budget]
    return chosen, total_cost, total_calories


def main():
    """Compare greedy and dynamic-programming selections for a fixed budget."""
    budget = 100
    greedy_result = greedy_algorithm(ITEMS, budget)
    dp_result = dynamic_programming(ITEMS, budget)

    print(f"Budget: {budget}")
    print("Greedy:", greedy_result)
    print("Dynamic programming:", dp_result)


if __name__ == "__main__":
    main()
