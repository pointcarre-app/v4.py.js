import numpy as np

# Graph 1: Identity and Minus Identity on [-1, 1]
x = np.linspace(-1, 1, 100)
y_identity = x  # y = x
y_minus_identity = -x  # y = -x

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
curve1_color = "#6b46c1"  # Purple
curve2_color = "#c7366f"  # Red-pink

# All visual elements in lines array
lines = [
    # First curve: y = x
    {
        "type": "curve",
        "id": "identity",
        "data": {"x": x.tolist(), "y": y_identity.tolist()},
        "stroke": curve1_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve identity-curve",
    },
    # Second curve: y = -x
    {
        "type": "curve",
        "id": "minus-identity",
        "data": {"x": x.tolist(), "y": y_minus_identity.tolist()},
        "stroke": curve2_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve minus-identity-curve",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1,
        "y1": 0,
        "x2": 1,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -1,
        "x2": 0,
        "y2": 1,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 0.5,
        "latex": r"y=x",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": -0.5,
        "latex": r"y=-x",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#ab0084",
    },
    {
        "x": -0.5,
        "y": 0.5,
        "latex": r"a^2+b^2=c^2",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -0.5,
        "y": -0.5,
        "latex": r"E=mc^2",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#ab0084",
    },
    {
        "x": 1,
        "y": 1,
        "latex": r"x",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#e6b45d",
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
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 5,
            "show_axes": False,  # We define axes in lines
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }
