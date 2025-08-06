import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Piecewise Function Graph
# Description: Function with different rules on different intervals. Clear breaks or continuity at transition points. Each piece labeled with its rule. Open/closed circles at endpoints to show inclusion/exclusion.

# Generate piecewise function: f(x) = x² for x < 0, f(x) = x for x ≥ 0
x_negative = np.linspace(-2, -0.1, 50)
x_positive = np.linspace(0, 2, 50)

y_negative = x_negative**2
y_positive = x_positive

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color_1 = "#6b46c1"  # Purple for x²
line_color_2 = "#ab0084"  # Pink for x

# All visual elements in lines array
lines = [
    # First piece: f(x) = x² for x < 0
    {
        "type": "curve",
        "id": "piece_1",
        "data": {"x": x_negative.tolist(), "y": y_negative.tolist()},
        "stroke": line_color_1,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve piecewise-1",
    },
    # Second piece: f(x) = x for x ≥ 0
    {
        "type": "curve",
        "id": "piece_2",
        "data": {"x": x_positive.tolist(), "y": y_positive.tolist()},
        "stroke": line_color_2,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve piecewise-2",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2,
        "y1": 0,
        "x2": 2,
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
        "y2": 4,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": -1.5,
        "y": 3.5,
        "latex": r"f(x) = \begin{cases} x^2 & \text{if } x < 0 \\ x & \text{if } x \geq 0 \end{cases}",
        "width": 200,
        "height": 40,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -1.5,
        "y": 2.5,
        "latex": r"f(x) = x^2",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#6b46c1",
    },
    {
        "x": 1.5,
        "y": 1.5,
        "latex": r"f(x) = x",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ab0084",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_piecewise_function_graph",
        "title": "Piecewise Function Graph",
        "description": "Piecewise function with f(x) = x² for x < 0 and f(x) = x for x ≥ 0",
        "svg": {
            "width": 400,
            "height": 350,
            "viewBox": "0 0 400 350",
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
