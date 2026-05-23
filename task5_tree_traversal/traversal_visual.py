from collections import deque
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    """A binary-tree node with a stable id and a visualization color."""

    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Add tree nodes and edges to a NetworkX graph with layout positions."""
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


def color_gradient(steps, start="#123A6F", end="#B7E4FF"):
    """Generate unique hex colors from dark to light for traversal order."""
    if steps <= 1:
        return [end]

    start_rgb = tuple(int(start[i:i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end[i:i + 2], 16) for i in (1, 3, 5))
    colors = []

    for step in range(steps):
        ratio = step / (steps - 1)
        rgb = tuple(
            round(start_rgb[channel] + (end_rgb[channel] - start_rgb[channel]) * ratio)
            for channel in range(3)
        )
        colors.append("#{0:02X}{1:02X}{2:02X}".format(*rgb))

    return colors


def dfs_order(root):
    """Return depth-first traversal order using an explicit stack, not recursion."""
    if root is None:
        return []

    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs_order(root):
    """Return breadth-first traversal order using a queue."""
    if root is None:
        return []

    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def apply_traversal_colors(order):
    """Assign progressively lighter colors to nodes in their visit order."""
    colors = color_gradient(len(order))
    for node, color in zip(order, colors):
        node.color = color
    return colors


def draw_tree(tree_root, title):
    """Draw a colored binary tree and return the matplotlib figure and axes."""
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


def create_demo_tree():
    """Create a fixed sample tree for DFS and BFS visualization."""
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    root.right.right = Node(2)
    return root


def visualize_traversal(root, traversal="dfs"):
    """Apply the selected traversal colors and draw the resulting tree."""
    if traversal == "dfs":
        order = dfs_order(root)
        title = "DFS traversal, stack"
    elif traversal == "bfs":
        order = bfs_order(root)
        title = "BFS traversal, queue"
    else:
        raise ValueError("Traversal must be 'dfs' or 'bfs'")

    apply_traversal_colors(order)
    return draw_tree(root, title), [node.val for node in order]


def main():
    """Display DFS and BFS visualizations for the demo tree."""
    dfs_root = create_demo_tree()
    (_, _), dfs_values = visualize_traversal(dfs_root, "dfs")
    print("DFS order:", dfs_values)

    bfs_root = create_demo_tree()
    (_, _), bfs_values = visualize_traversal(bfs_root, "bfs")
    print("BFS order:", bfs_values)

    plt.show()


if __name__ == "__main__":
    main()
