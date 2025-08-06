import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Function Transformations
# Subsection: Reflection and Stretching
# Description: Multiple curves showing: original f(x), reflection -f(x) or f(-x), vertical stretch af(x), horizontal stretch f(x/b). Each transformation in different color with clear legend.

# Generate function transformations
# Original: f(x) = x^2
# Reflection: -f(x) = -x^2
# Vertical stretch: 2f(x) = 2x^2
x = np.linspace(-2, 2, 100)
y_original = x**2
y_reflection = -(x**2)
y_stretch = 2 * x**2

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
original_color = "#6b46c1"  # Purple for original
reflection_color = "#ec3059"  # Red for reflection
stretch_color = "#10b981"  # Green for stretch

# All visual elements in lines array
lines = [
    # Original function: f(x) = x^2
    {
        "type": "curve",
        "id": "original",
        "data": {"x": x.tolist(), "y": y_original.tolist()},
        "stroke": original_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve original",
    },
    # Reflection: -f(x) = -x^2
    {
        "type": "curve",
        "id": "reflection",
        "data": {"x": x.tolist(), "y": y_reflection.tolist()},
        "stroke": reflection_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,5",
        "fill": "none",
        "class": "curve reflection",
    },
    # Vertical stretch: 2f(x) = 2x^2
    {
        "type": "curve",
        "id": "stretch",
        "data": {"x": x.tolist(), "y": y_stretch.tolist()},
        "stroke": stretch_color,
        "stroke-width": 2,
        "stroke-dasharray": "3,3",
        "fill": "none",
        "class": "curve stretch",
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
        "y1": -4,
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
        "x": 0,
        "y": 9,
        "latex": r"Reflection and Stretching",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0,
        "y": 8.5,
        "latex": r"f(x) = x^2",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": original_color,
    },
    {
        "x": 0,
        "y": 8,
        "latex": r"-f(x) = -x^2",
        "width": 90,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": reflection_color,
    },
    {
        "x": 0,
        "y": 7.5,
        "latex": r"2f(x) = 2x^2",
        "width": 90,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": stretch_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_function_transformations_reflection_and_stretching",
        "title": "Reflection and Stretching",
        "description": "Function transformations showing reflection and vertical stretching",
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
