import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Trigonometry
# Subsection: Unit Circle with Angles
# Description: A circle of radius 1 centered at origin. Key angles marked in both degrees and radians (0°, 30°, 45°, 60°, 90°, etc.). Coordinates of points shown as (cos θ, sin θ). Positive direction (counterclockwise) indicated.

# Generate unit circle data
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple

# All visual elements in lines array
lines = [
    # Unit circle
    {
        "type": "curve",
        "id": "unit_circle",
        "data": {"x": x_circle.tolist(), "y": y_circle.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve unit-circle",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1.5,
        "y1": 0,
        "x2": 1.5,
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
        "latex": r"Unit Circle",
        "width": 80,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 1.05,
        "y": 0.05,
        "latex": r"(1,0)",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.05,
        "y": 1.05,
        "latex": r"(0,1)",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.7,
        "y": 0.7,
        "latex": r"45°",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#e6b45d",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_trigonometry_unit_circle_with_angles",
        "title": "Unit Circle with Angles",
        "description": "Unit circle showing key angles in degrees and radians with coordinate points marked",
        "svg": {
            "width": 350,
            "height": 350,
            "viewBox": "0 0 350 350",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 25,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }
