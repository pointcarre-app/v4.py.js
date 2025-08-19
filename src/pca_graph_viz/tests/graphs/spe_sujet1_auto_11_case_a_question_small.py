import numpy as np

# Cubic function visualization: y = (x - root1)(x - root2)(x - root3) (small 200x200)
# Case A: root1=-4, root2=2, root3=5

ROOT1 = -4
ROOT2 = 2
ROOT3 = 5

# Generate cubic function data
x = np.linspace(-5, 7, 1000)
y = (x - ROOT1) * (x - ROOT2) * (x - ROOT3)

# Visual elements using CSS utility classes
lines = [
    # X-axis
    {
        "type": "axis",
        "x1": -4.75,
        "y1": 0,
        "x2": 6.75,
        "y2": 0,
        "stroke-width": 1.5,  # Bigger tick
        "class": "axis x-axis stroke-base-content",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -100,
        "x2": 0,
        "y2": 100,
        "stroke-width": 1,
        "class": "axis y-axis stroke-base-content",
    },
    # Cubic curve
    {
        "type": "curve",
        "id": "cubic",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke-width": 1.5,
        "fill": "none",
        "class": "curve stroke-primary",
    },
]

# Mark the roots with small circles
root_markers = [
    # Root 1
    {
        "type": "circle",
        "cx": ROOT1,
        "cy": 0,
        "r": 2,
        "class": "fill-base-content stroke-base-content",
    },
    # Root 2
    {
        "type": "circle",
        "cx": ROOT2,
        "cy": 0,
        "r": 2,
        "class": "fill-base-content stroke-base-content",
    },
    # Root 3
    {
        "type": "circle",
        "cx": ROOT3,
        "cy": 0,
        "r": 2,
        "class": "fill-base-content stroke-base-content",
    },
]

lines.extend(root_markers)

foreign_objects = [
    # Function label with background
    {
        "x": 6.75,
        "y": 35,
        "latex": "C_f",
        "width": 18,
        "height": 18,
        "class": "svg-latex text-primary text-sm",
        "style": "background-color: rgba(255, 255, 255, 0.7); border-radius: var(--rounded-box, 0.5rem); padding: 1px 3px;",
    },
    # X axis label
    {
        "x": 7,
        "y": -5.5,
        "latex": "x",
        "width": 16,
        "height": 16,
        "class": "svg-latex fill-base-content text-sm",
    },
    # Y axis label
    {
        "x": 0.5,
        "y": 105,
        "latex": "y",
        "width": 16,
        "height": 16,
        "class": "svg-latex fill-base-content text-sm",
    },
    # Root labels (positioned below dots with better control)
    {
        "x": ROOT1,  # Centered at root position
        "y": -9.75,  # Higher position (scaled for small version)
        "latex": str(ROOT1),
        "width": 12,  # Appropriate width for small version
        "height": 12,
        "class": "svg-latex fill-base-content text-sm",
        "style": "overflow: visible; text-align: center; background: rgba(255, 255, 255, 0.8); border-radius: 2px;",
    },
    {
        "x": ROOT2,  # Centered at root position
        "y": -9.75,  # Higher position (scaled for small version)
        "latex": str(ROOT2),
        "width": 12,  # Appropriate width for small version
        "height": 12,
        "class": "svg-latex fill-base-content text-sm",
        "style": "overflow: visible; text-align: center; background: rgba(255, 255, 255, 0.8); border-radius: 2px;",
    },
    {
        "x": ROOT3,  # Centered at root position
        "y": -9.75,  # Higher position (scaled for small version)
        "latex": str(ROOT3),
        "width": 12,  # Appropriate width for small version
        "height": 12,
        "class": "svg-latex fill-base-content text-sm",
        "style": "overflow: visible; text-align: center; background: rgba(255, 255, 255, 0.8); border-radius: 2px;",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "cubic-function-small-case-a",
        "title": "spe_sujet1_auto_11_case_a_question_small.py",
        "description": "Small visualization of cubic function with three roots - Case A (200x200)",
        "svg": {
            "width": 200,
            "height": 200,
            "viewBox": "0 0 200 200",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": 0,
            "show_axes": False,
            "show_grid": False,
            "x_range": [-5, 7],
            "y_range": [-100, 100],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }
