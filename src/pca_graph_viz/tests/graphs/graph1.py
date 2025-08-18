import numpy as np

# Graph 1: Identity and Minus Identity on [-1, 1]
x = np.linspace(-1, 1, 100)
y_identity = x  # y = x
y_minus_identity = -x  # y = -x

# Colors will be handled by CSS classes
# No need for explicit color definitions when using DaisyUI theme classes

# All visual elements in lines array
lines = [
    # First curve: y = x
    {
        "type": "curve",
        "id": "identity",
        "data": {"x": x.tolist(), "y": y_identity.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve identity-curve stroke-primary",
    },
    # Second curve: y = -x
    {
        "type": "curve",
        "id": "minus-identity",
        "data": {"x": x.tolist(), "y": y_minus_identity.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve minus-identity-curve stroke-secondary",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1,
        "y1": 0,
        "x2": 1,
        "y2": 0,
        "stroke-width": 1.5,
        "class": "axis x-axis stroke-base-content",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -1,
        "x2": 0,
        "y2": 1,
        "stroke-width": 1.5,
        "class": "axis y-axis stroke-base-content",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 0.5,
        "latex": r"y=x",
        "width": 50,
        "height": 20,
        "class": "svg-latex text-primary",
    },
    {
        "x": 0.5,
        "y": -0.5,
        "latex": r"y=-x",
        "width": 50,
        "height": 20,
        "class": "svg-latex text-secondary",
    },
    {
        "x": -0.5,
        "y": 0.5,
        "latex": r"a^2+b^2=c^2",
        "width": 100,
        "height": 20,
        "class": "svg-latex text-primary",
    },
    {
        "x": -0.5,
        "y": -0.5,
        "latex": r"E=mc^2",
        "width": 100,
        "height": 20,
        "class": "svg-latex text-secondary",
    },
    {
        "x": 1,
        "y": 1,
        "latex": r"x",
        "width": 20,
        "height": 20,
        "class": "svg-latex text-accent",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary (V2 format - curves in lines)."""
    return {
        "id": "graph1",
        "title": "Mathematical Functions and Famous Equations",
        "description": "Shows y = x and y = -x with classic mathematical formulas",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": 5,
            "show_axes": False,  # We define axes in lines
            "show_grid": False,  # We define grid in lines with classes
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }
