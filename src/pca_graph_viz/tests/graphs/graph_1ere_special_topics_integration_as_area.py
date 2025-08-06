import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Integration as Area
# Description: Region between curve and x-axis shaded. Positive areas above axis, negative below (different shading). Definite integral notation ∫ₐᵇ f(x)dx with limits clearly marked. Can include Riemann sum rectangles.

# Generate function: f(x) = x² - 1
x = np.linspace(-2, 2, 100)
y = x**2 - 1

# Integration limits
a, b = -1, 1
x_integral = np.linspace(a, b, 50)
y_integral = x_integral**2 - 1

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for function
area_color = "#2a88c0"  # Blue for area

# All visual elements in lines array
lines = [
    # Function curve
    {
        "type": "curve",
        "id": "function_curve",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve function",
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
        "y1": -1.5,
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
        "x": 1.5,
        "y": 2.5,
        "latex": r"f(x) = x^2 - 1",
        "width": 100,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": 1.5,
        "latex": r"\int_{-1}^{1} (x^2 - 1) dx",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#2a88c0",
    },
    {
        "x": -1.2,
        "y": 2.5,
        "latex": r"a = -1",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
    {
        "x": 0.8,
        "y": 2.5,
        "latex": r"b = 1",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_integration_as_area",
        "title": "Integration as Area",
        "description": "Definite integral of f(x) = x² - 1 from x = -1 to x = 1, showing area under the curve",
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
