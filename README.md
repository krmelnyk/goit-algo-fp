# Final Project: Algorithms and Data Structures

This project contains implementations of seven algorithmic tasks: a singly
linked list, a recursive fractal, Dijkstra's algorithm, heap visualization,
tree traversals, greedy and dynamic programming algorithms, and the Monte Carlo
method.

## Installing Dependencies

```bash
pip install -r requirements.txt
```

## Running the Tasks

```bash
python task1_linked_list/demo.py
python task2_pythagoras_tree/fractal.py
python task3_dijkstra/dijkstra.py
python task4_heap_visualization/heap_visualization.py
python task5_tree_traversal/traversal_visual.py
python task6_food_selection/food_algorithms.py
python task7_monte_carlo/monte_carlo_dice.py
```

## Task 1

The `task1_linked_list/linked_list.py` file implements:

- `reverse_linked_list` - reverses a singly linked list by changing references
  between nodes;
- `merge_sort` - merge sort for a singly linked list;
- `merge_sorted_lists` - merges two sorted linked lists into one sorted list.

## Task 2

The `task2_pythagoras_tree/fractal.py` file implements recursive construction
of the "Pythagoras tree" fractal using `matplotlib`. The user enters the
recursion level when running the program.

## Task 3

The `task3_dijkstra/dijkstra.py` file implements Dijkstra's algorithm using the
binary heap module `heapq`. The file also contains an example weighted graph
and prints the shortest distances from the starting vertex to all other
vertices.

## Task 4

The `task4_heap_visualization/heap_visualization.py` file implements conversion
of a list of values into a binary min-heap, builds a tree from that heap, and
visualizes it using `networkx` and `matplotlib`.

## Task 5

The `task5_tree_traversal/traversal_visual.py` file implements:

- DFS using a stack;
- BFS using a queue;
- node coloring in hex RGB from dark to light according to traversal order.

Recursion is not used for the traversal algorithms.

## Task 6

The `task6_food_selection/food_algorithms.py` file implements two approaches to
food selection within a budget:

- `greedy_algorithm` selects items by descending calories-to-cost ratio;
- `dynamic_programming` finds the optimal item set for maximum total calories.

For a budget of 100, the greedy algorithm selects `cola`, `potato`, `pepsi`,
and `hot-dog` for 870 calories. Dynamic programming finds the optimal set:
`pizza`, `pepsi`, `cola`, and `potato` for 970 calories.

## Task 7

The `task7_monte_carlo/monte_carlo_dice.py` file implements a simulation of a
large number of rolls of two dice, counts sums from 2 to 12, prints a
probability table, and plots a comparison with analytical probabilities.

Analytical probabilities:

| Sum | Probability |
|---:|---:|
| 2 | 2.78% |
| 3 | 5.56% |
| 4 | 8.33% |
| 5 | 11.11% |
| 6 | 13.89% |
| 7 | 16.67% |
| 8 | 13.89% |
| 9 | 11.11% |
| 10 | 8.33% |
| 11 | 5.56% |
| 12 | 2.78% |

With a large number of simulations, the Monte Carlo results approach the
analytical values. The highest probability corresponds to the sum 7, while the
lowest probabilities correspond to sums 2 and 12. Small deviations are normal
for a random experiment and decrease as the number of rolls increases.

## Complexity

- Merge sort for the linked list: `O(n log n)`.
- Dijkstra's algorithm with a binary heap: `O((V + E) log V)`.
- Dynamic programming for food selection: `O(n * budget)`.
- Monte Carlo simulation: `O(n)`, where `n` is the number of rolls.
