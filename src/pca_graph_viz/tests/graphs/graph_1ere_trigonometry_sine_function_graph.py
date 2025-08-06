import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Trigonometry
# Subsection: Sine Function Graph
# Description: A smooth wave oscillating between -1 and 1. Period of 2π clearly marked. Key points at 0, π/2, π, 3π/2, 2π. X-axis in radians or degrees. Amplitude = 1, shows one complete cycle minimum.

# Generate sine function data
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple

# All visual elements in lines array
lines = [
    # Sine curve
    {
        "type": "curve",
        "id": "sine_curve",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve sine-wave",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2*np.pi,
        "y1": 0,
        "x2": 2*np.pi,
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
        "x": 0.5,
        "y": 1.2,
        "latex": r"f(x) = \sin(x)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": np.pi/2,
        "y": -0.3,
        "latex": r"\frac{\pi}{2}",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": np.pi,
        "y": -0.3,
        "latex": r"\pi",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_trigonometry_sine_function_graph",
        "title": "Sine Function Graph",
        "description": "Sine function f(x) = sin(x) showing one complete cycle with key points marked",
        "svg": {
            "width": 400,
            "height": 300,
            "viewBox": "0 0 400 300",
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
