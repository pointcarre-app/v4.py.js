import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Newton's Method Iteration
# Description: Function curve with tangent lines at successive approximations. Starting point x₀, tangent intersects x-axis at x₁, repeat. Shows convergence to root. Formula xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ) included.

# Generate Newton's method example: f(x) = x² - 2, f'(x) = 2x
# Starting with x₀ = 2, find √2
x = np.linspace(0, 3, 100)
y = x**2 - 2

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for function

# All visual elements in lines array
lines = [
    # Function curve: f(x) = x² - 2
    {
        "type": "curve",
        "id": "function",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve function",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -3,
        "x2": 3,
        "y2": -3,
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
        "y2": 7,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 6,
        "latex": r"Newton's Method: f(x) = x^2 - 2",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": 5.5,
        "latex": r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#ec3059",
    },
    {
        "x": 2.2,
        "y": 4,
        "latex": r"x_0 = 2",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 1.4,
        "y": -2.5,
        "latex": r"\sqrt{2} \approx 1.4142",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_newton_s_method_iteration",
        "title": "Newton's Method Iteration",
        "description": "Newton's method applied to f(x) = x² - 2 to find √2, showing tangent lines and convergence",
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
