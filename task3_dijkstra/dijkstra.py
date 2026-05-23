import heapq


def dijkstra(graph, start):
    """Compute shortest distances from start using Dijkstra and a binary heap."""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def create_graph():
    """Return a sample weighted directed graph for demonstrating Dijkstra."""
    return {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("B", 1), ("D", 8), ("E", 10)],
        "D": [("E", 2), ("F", 6)],
        "E": [("F", 3)],
        "F": [],
    }


def main():
    """Run Dijkstra on the sample graph and print distances from the start."""
    graph = create_graph()
    start = "A"
    distances = dijkstra(graph, start)
    print(f"Shortest distances from vertex {start}:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")


if __name__ == "__main__":
    main()
