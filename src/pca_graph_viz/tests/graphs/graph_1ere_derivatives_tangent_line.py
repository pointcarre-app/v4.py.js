import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Derivatives and Functions
# Subsection: Tangent Line to a Curve
# Description: A graph showing a smooth curve with a straight line touching it at exactly one point.
# The x-axis and y-axis are labeled, the point of tangency is marked, and the slope of the tangent line
# represents the derivative at that point. Include the equation of the tangent line.

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
        "id": "graph_1ere_derivatives_tangent_line",
        "title": "Tangent Line to a Curve",
        "description": "Placeholder for tangent line visualization",
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
