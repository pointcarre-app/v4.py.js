import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Exponential Function
# Subsection: Exponential Growth Curve
# Description: A curve that increases rapidly, starting slowly and then accelerating.
# Shows the characteristic exponential shape f(x) = a^x where a > 1.
# Include key points like (0,1) and show the rapid growth rate.

# Generate exponential growth: f(x) = 2^x
x = np.linspace(-2, 3, 100)
y = 2**x

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
curve_color = "#6b46c1"  # Purple for exponential curve

# All visual elements in lines array
lines = [
    # Exponential growth curve
    {
        "type": "curve",
        "id": "exponential",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": curve_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve exponential",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2,
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
        "y1": 0,
        "x2": 0,
        "y2": 8,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.5,
        "y": 7.5,
        "latex": r"f(x) = 2^x",
        "width": 80,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.2,
        "y": 1.2,
        "latex": r"(0, 1)",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve_color,
    },
    {
        "x": 1.2,
        "y": 2.2,
        "latex": r"(1, 2)",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve_color,
    },
    {
        "x": 2.2,
        "y": 4.2,
        "latex": r"(2, 4)",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve_color,
    },
    {
        "x": -1.2,
        "y": 0.6,
        "latex": r"(-1, 0.5)",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve_color,
    },
    {
        "x": 0.5,
        "y": 6.5,
        "latex": r"Exponential Growth",
        "width": 150,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_exponential_function_exponential_growth_curve",
        "title": "Exponential Growth Curve",
        "description": "Exponential function f(x) = 2^x showing characteristic growth pattern",
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
