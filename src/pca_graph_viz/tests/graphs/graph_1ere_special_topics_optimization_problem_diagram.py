import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Optimization Problem Diagram
# Description: A geometric figure (rectangle, triangle, etc.) with variable dimensions labeled. Constraint equation shown. Function to optimize (area, perimeter) expressed in terms of one variable. Critical dimensions marked.

# Generate optimization problem: Maximize area of rectangle with perimeter = 20
# Let x = width, then length = 10 - x (since 2x + 2(10-x) = 20)
# Area = x(10-x) = 10x - x²

x = np.linspace(0, 10, 100)
area = x * (10 - x)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for area function

# All visual elements in lines array
lines = [
    # Area function: A(x) = 10x - x²
    {
        "type": "curve",
        "id": "area_function",
        "data": {"x": x.tolist(), "y": area.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve area-function",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": 0,
        "x2": 10,
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
        "y1": 0,
        "x2": 0,
        "y2": 25,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 23,
        "latex": r"Optimization Problem",
        "width": 150,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": 21,
        "latex": r"Maximize: A(x) = 10x - x^2",
        "width": 180,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color,
    },
    {
        "x": 0.5,
        "y": 19,
        "latex": r"Constraint: 2x + 2y = 20",
        "width": 160,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 5.5,
        "y": 15,
        "latex": r"x = 5",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_optimization_problem_diagram",
        "title": "Optimization Problem Diagram",
        "description": "Maximizing area of rectangle with fixed perimeter P = 20, showing A(x) = 10x - x²",
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
