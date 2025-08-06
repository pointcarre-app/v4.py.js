import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Derivatives and Functions
# Subsection: Derivative Graph vs Original Function
# Description: Two coordinate systems stacked vertically: top shows original function f(x), bottom shows derivative f'(x). Where f has maximum/minimum, f' crosses x-axis. Where f increases, f' is positive (above x-axis). Where f decreases, f' is negative.

# Generate derivative comparison
# Original: f(x) = x^2 - 2x
# Derivative: f'(x) = 2x - 2
x = np.linspace(-1, 3, 100)
y_original = x**2 - 2 * x
y_derivative = 2 * x - 2

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
original_color = "#6b46c1"  # Purple for original
derivative_color = "#ec3059"  # Red for derivative

# All visual elements in lines array
lines = [
    # Original function: f(x) = x^2 - 2x
    {
        "type": "curve",
        "id": "original",
        "data": {"x": x.tolist(), "y": y_original.tolist()},
        "stroke": original_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve original",
    },
    # Derivative function: f'(x) = 2x - 2
    {
        "type": "curve",
        "id": "derivative",
        "data": {"x": x.tolist(), "y": y_derivative.tolist()},
        "stroke": derivative_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,5",
        "fill": "none",
        "class": "curve derivative",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1,
        "y1": 0,
        "x2": 3,
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
        "y1": -3,
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
        "x": 1,
        "y": 3.5,
        "latex": r"Derivative vs Original",
        "width": 160,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 1,
        "y": 3,
        "latex": r"f(x) = x^2 - 2x",
        "width": 120,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": original_color,
    },
    {
        "x": 1,
        "y": 2.5,
        "latex": r"f'(x) = 2x - 2",
        "width": 110,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": derivative_color,
    },
    {
        "x": 1,
        "y": 2,
        "latex": r"Min at x = 1",
        "width": 90,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_derivatives_and_functions_derivative_graph_vs_original_function",
        "title": "Derivative Graph vs Original Function",
        "description": "Comparison of original function f(x) = x² - 2x and its derivative f'(x) = 2x - 2",
        "svg": {
            "width": 400,
            "height": 400,
            "viewBox": "0 0 400 400",
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
