import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Inequality Region Shading
# Description: Coordinate plane with one or more regions shaded. Boundary lines (solid for ≤ or ≥, dashed for < or >) clearly shown. Test point to verify correct region. Intersection of multiple inequalities if applicable.

# Generate inequality region: y ≥ x and y ≤ 2 - x
x = np.linspace(-1, 2, 100)
y1 = x  # y = x (boundary for y ≥ x)
y2 = 2 - x  # y = 2 - x (boundary for y ≤ 2 - x)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color_1 = "#6b46c1"  # Purple for y ≥ x
line_color_2 = "#ab0084"  # Pink for y ≤ 2 - x

# All visual elements in lines array
lines = [
    # Boundary line: y = x (solid for ≥)
    {
        "type": "curve",
        "id": "boundary_1",
        "data": {"x": x.tolist(), "y": y1.tolist()},
        "stroke": line_color_1,
        "stroke-width": 2,
        "fill": "none",
        "class": "boundary-line",
    },
    # Boundary line: y = 2 - x (solid for ≤)
    {
        "type": "curve",
        "id": "boundary_2",
        "data": {"x": x.tolist(), "y": y2.tolist()},
        "stroke": line_color_2,
        "stroke-width": 2,
        "fill": "none",
        "class": "boundary-line",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1,
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
        "y2": 3,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 2.5,
        "latex": r"y \geq x",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color_1,
    },
    {
        "x": 1.5,
        "y": 0.5,
        "latex": r"y \leq 2 - x",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color_2,
    },
    {
        "x": 0.5,
        "y": 1.5,
        "latex": r"Feasible Region",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#2a88c0",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_inequality_region_shading",
        "title": "Inequality Region Shading",
        "description": "System of inequalities: y ≥ x and y ≤ 2 - x, showing the feasible region",
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
