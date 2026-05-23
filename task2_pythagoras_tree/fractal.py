import math

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def _square_from_bottom(left_bottom, right_bottom):
    """Build square vertices from its bottom side and return its top side."""
    x1, y1 = left_bottom
    x2, y2 = right_bottom
    dx = x2 - x1
    dy = y2 - y1
    left_top = (x1 - dy, y1 + dx)
    right_top = (x2 - dy, y2 + dx)
    return [left_bottom, right_bottom, right_top, left_top], left_top, right_top


def draw_pythagoras_tree(ax, left_bottom, right_bottom, level):
    """Draw a Pythagoras tree recursively on the provided matplotlib axes."""
    if level == 0:
        return

    square, left_top, right_top = _square_from_bottom(left_bottom, right_bottom)
    color = plt.cm.Greens(0.25 + 0.65 * level / max(level, 1))
    ax.add_patch(Polygon(square, closed=True, facecolor=color, edgecolor="darkgreen"))

    x1, y1 = left_top
    x2, y2 = right_top
    dx = x2 - x1
    dy = y2 - y1
    angle = math.radians(45)
    scale = math.cos(angle)

    left_dx = scale * (dx * math.cos(angle) - dy * math.sin(angle))
    left_dy = scale * (dx * math.sin(angle) + dy * math.cos(angle))
    peak = (x1 + left_dx, y1 + left_dy)

    draw_pythagoras_tree(ax, left_top, peak, level - 1)
    draw_pythagoras_tree(ax, peak, right_top, level - 1)


def create_pythagoras_tree(level):
    """Create a matplotlib figure with a Pythagoras tree of the given depth."""
    fig, ax = plt.subplots(figsize=(8, 8))
    draw_pythagoras_tree(ax, (-0.5, 0), (0.5, 0), level)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.autoscale_view()
    ax.set_title(f"Pythagoras tree, recursion level {level}")
    return fig, ax


def main():
    """Read recursion depth from the user and display the generated fractal."""
    level = int(input("Enter recursion depth: "))
    create_pythagoras_tree(level)
    plt.show()


if __name__ == "__main__":
    main()
