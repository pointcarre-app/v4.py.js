import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Trigonometry
# Subsection: Angle Wrapping Visualization
# Description: A number line being wrapped around unit circle. Shows how real numbers correspond to angles. Point at x on line maps to angle x radians on circle. Demonstrates periodic nature of trig functions.

# Generate angle wrapping visualization
# Number line from -2π to 4π wrapped around unit circle

# Unit circle
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
circle_color = "#6b46c1"  # Purple for circle
line_color = "#ec3059"  # Red for number line

# All visual elements in lines array
lines = [
    # Unit circle
    {
        "type": "curve",
        "id": "unit_circle",
        "data": {"x": x_circle.tolist(), "y": y_circle.tolist()},
        "stroke": circle_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve unit-circle",
    },
    # Number line (horizontal)
    {
        "type": "line",
        "x1": -2,
        "y1": -1.5,
        "x2": 2,
        "y2": -1.5,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "number-line",
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
        "y2": 1.5,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.2,
        "y": 1.3,
        "latex": r"Angle Wrapping",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.2,
        "y": 1.1,
        "latex": r"x \mapsto \theta = x \bmod 2\pi",
        "width": 150,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.05,
        "y": 0.05,
        "latex": r"0",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 0.05,
        "y": 1.05,
        "latex": r"\frac{\pi}{2}",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": -1.05,
        "y": 0.05,
        "latex": r"\pi",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_trigonometry_angle_wrapping_visualization",
        "title": "Angle Wrapping Visualization",
        "description": "Number line wrapped around unit circle showing how real numbers map to angles modulo 2π",
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
