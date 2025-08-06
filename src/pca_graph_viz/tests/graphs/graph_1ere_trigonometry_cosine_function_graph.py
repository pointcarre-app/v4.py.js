import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Trigonometry
# Subsection: Cosine Function Graph
# Description: Similar wave to sine but shifted. Starts at maximum (0,1). Same period and amplitude as sine. Phase difference from sine clearly visible. Both axes labeled with key values.

# Generate cosine function data
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#ab0084"  # Pink/magenta to distinguish from sine

# All visual elements in lines array
lines = [
    # Cosine curve
    {
        "type": "curve",
        "id": "cosine_curve",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve cosine-wave",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2*np.pi,
        "y1": 0,
        "x2": 2*np.pi,
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
        "y1": -1.5,
        "x2": 0,
        "y2": 1.5,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 1.2,
        "latex": r"f(x) = \cos(x)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#ab0084",
    },
    {
        "x": 0,
        "y": -0.3,
        "latex": r"0",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": np.pi,
        "y": -0.3,
        "latex": r"\pi",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_trigonometry_cosine_function_graph",
        "title": "Cosine Function Graph",
        "description": "Cosine function f(x) = cos(x) showing phase difference from sine function",
        "svg": {
            "width": 400,
            "height": 300,
            "viewBox": "0 0 400 300",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 20,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }
