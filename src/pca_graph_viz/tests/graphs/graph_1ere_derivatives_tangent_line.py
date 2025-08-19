import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Derivatives and Functions
# Subsection: Tangent Line to a Curve
# Description: A graph showing a smooth curve with a straight line touching it at exactly one point.
# The x-axis and y-axis are labeled, the point of tangency is marked, and the slope of the tangent line
# represents the derivative at that point. Include the equation of the tangent line.

# Define the curve: f(x) = x³ - 2x + 1
x = np.linspace(-2, 2.5, 200)
y_curve = x**3 - 2 * x + 1

# Point of tangency
x0 = 1.0
y0 = x0**3 - 2 * x0 + 1  # f(1) = 0

# Derivative: f'(x) = 3x² - 2
# At x=1: f'(1) = 3 - 2 = 1
slope = 3 * x0**2 - 2

# Tangent line: y - y0 = slope*(x - x0)
x_tangent = np.linspace(-0.5, 2.5, 100)
y_tangent = slope * (x_tangent - x0) + y0

# Use nice hex colors directly
bg_color = "#fef3e2"  # Warm light background
grid_color = "#f5d5a8"  # Warm grid
curve_color = "#2563eb"  # Blue for curve
tangent_color = "#dc2626"  # Red for tangent
point_color = "#9333ea"  # Purple for point

# All visual elements in lines array
lines = [
    # The main curve
    {
        "type": "curve",
        "id": "cubic",
        "data": {"x": x.tolist(), "y": y_curve.tolist()},
        "stroke": curve_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "curve main-curve",
    },
    # The tangent line
    {
        "type": "curve",
        "id": "tangent",
        "data": {"x": x_tangent.tolist(), "y": y_tangent.tolist()},
        "stroke": tangent_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,3",
        "fill": "none",
        "class": "tangent-line",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2,
        "y1": 0,
        "x2": 2.5,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 1.5,
        "stroke-opacity": 0.7,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -3,
        "x2": 0,
        "y2": 4,
        "stroke": "#666666",
        "stroke-width": 1.5,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
    # Point of tangency
    {
        "type": "circle",
        "cx": float(x0),
        "cy": float(y0),
        "r": 4,
        "fill": point_color,
        "stroke": "#7c3aed",
        "stroke-width": 2,
        "class": "tangent-point",
    },
]

foreign_objects = [
    # Function equation
    {
        "x": -1.5,
        "y": 3.5,
        "latex": r"f(x) = x^3 - 2x + 1",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(37, 99, 235, 0.1)",
        "text_color": curve_color,
        "border_radius": "0.25rem",
    },
    # Derivative
    {
        "x": -1.5,
        "y": 3,
        "latex": r"f'(x) = 3x^2 - 2",
        "width": 100,
        "height": 25,
        "bg_color": "rgba(220, 38, 38, 0.1)",
        "text_color": tangent_color,
        "border_radius": "0.25rem",
    },
    # Point of tangency label
    {
        "x": x0 + 0.1,
        "y": y0 + 0.2,
        "latex": f"({x0:.0f}, {y0:.0f})",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(147, 51, 234, 0.9)",
        "text_color": "white",
        "border_radius": "0.25rem",
    },
    # Slope at point
    {
        "x": 1.5,
        "y": 1,
        "latex": f"f'({x0:.0f}) = {slope:.0f}",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(220, 38, 38, 0.1)",
        "text_color": tangent_color,
        "border_radius": "0.25rem",
    },
    # Tangent line equation
    {
        "x": 0.5,
        "y": -2.5,
        "latex": r"y = x - 1",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(220, 38, 38, 0.1)",
        "text_color": tangent_color,
        "border_radius": "0.25rem",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_derivatives_tangent_line",
        "title": "Tangent Line to a Curve",
        "description": "Tangent line to a cubic curve showing derivative at a point",
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
