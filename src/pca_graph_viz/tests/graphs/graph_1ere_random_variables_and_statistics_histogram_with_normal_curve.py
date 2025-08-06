import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Random Variables and Statistics
# Subsection: Histogram with Normal Curve
# Description: Bars showing frequency distribution of data. Smooth bell curve overlaid showing theoretical normal distribution. X-axis shows data values or intervals, y-axis shows frequency or relative frequency. Mean and standard deviation marked.

# Simple y=1 line for now (to be implemented)
x = np.linspace(-2, 2, 100)
y = np.ones_like(x)  # y = 1

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple

# All visual elements in lines array
lines = [
    # Horizontal line: y = 1
    {
        "type": "curve",
        "id": "y_equals_1",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve horizontal-line",
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
        "y1": -2,
        "x2": 0,
        "y2": 2,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 1,
        "y": 1.2,
        "latex": r"y=1",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_random_variables_and_statistics_histogram_with_normal_curve",
        "title": "Histogram with Normal Curve",
        "description": "Placeholder for histogram with normal curve visualization",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 5,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }
