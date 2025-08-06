import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Second Degree Functions
# Subsection: Parabola
# Description: A U-shaped curve (parabola) with vertex clearly marked. Axis of symmetry shown as vertical line.
# Can show standard form y = ax² + bx + c or vertex form y = a(x-h)² + k. Include key points like vertex,
# y-intercept, and x-intercepts if they exist.

# Generate parabola: f(x) = x² - 2x - 3 (vertex form: f(x) = (x-1)² - 4)
x = np.linspace(-2, 4, 100)
y = x**2 - 2*x - 3

# Key points
vertex_x = 1
vertex_y = vertex_x**2 - 2*vertex_x - 3  # = -4
y_intercept_x = 0
y_intercept_y = y_intercept_x**2 - 2*y_intercept_x - 3  # = -3
x_intercept_1 = -1  # f(-1) = 0
x_intercept_2 = 3   # f(3) = 0

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
parabola_color = "#6b46c1"  # Purple for parabola
axis_color = "#ab0084"  # Pink for axis of symmetry

# All visual elements in lines array
lines = [
    # Parabola curve
    {
        "type": "curve",
        "id": "parabola",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": parabola_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve parabola",
    },
    # Axis of symmetry (vertical line through vertex)
    {
        "type": "line",
        "x1": vertex_x,
        "y1": -5,
        "x2": vertex_x,
        "y2": 5,
        "stroke": axis_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,5",
        "class": "axis-symmetry",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2,
        "y1": 0,
        "x2": 4,
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
        "y1": -5,
        "x2": 0,
        "y2": 5,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 4.5,
        "latex": r"f(x) = x^2 - 2x - 3",
        "width": 150,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": 4,
        "latex": r"f(x) = (x-1)^2 - 4",
        "width": 130,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.2,
        "y": -4.2,
        "latex": r"V(1, -4)",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": parabola_color,
    },
    {
        "x": 0.2,
        "y": -3.2,
        "latex": r"(0, -3)",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": -1.2,
        "y": 0.2,
        "latex": r"(-1, 0)",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 3.2,
        "y": 0.2,
        "latex": r"(3, 0)",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 1.2,
        "y": 2,
        "latex": r"x = 1",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": axis_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_second_degree_functions_parabola",
        "title": "Parabola",
        "description": "Quadratic function f(x) = x² - 2x - 3 showing vertex, axis of symmetry, and intercepts",
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
