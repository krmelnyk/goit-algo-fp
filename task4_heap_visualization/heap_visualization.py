import heapq
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    """A binary-tree node used to visualize heap elements."""

    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_values, index=0):
    """Build a binary tree from heap array positions using child index formulas."""
    if index >= len(heap_values):
        return None

    node = Node(heap_values[index])
    node.left = build_heap_tree(heap_values, 2 * index + 1)
    node.right = build_heap_tree(heap_values, 2 * index + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Add tree nodes and edges to a NetworkX graph with drawing coordinates."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary heap"):
    """Draw the binary tree representation of a heap and return the figure."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    fig, ax = plt.subplots(figsize=(9, 6))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2200,
        node_color=colors,
        font_size=10,
        ax=ax,
    )
    ax.set_title(title)
    return fig, ax


def visualize_heap(values):
    """Heapify input values, convert the heap array to a tree, and visualize it."""
    if not values:
        raise ValueError("Heap values list cannot be empty")

    heap_values = list(values)
    heapq.heapify(heap_values)
    root = build_heap_tree(heap_values)
    return draw_tree(root, title=f"Binary min-heap: {heap_values}")


def main():
    """Visualize a sample binary min-heap."""
    values = [10, 4, 15, 20, 1, 8, 7, 3]
    visualize_heap(values)
    plt.show()


if __name__ == "__main__":
    main()
