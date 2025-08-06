import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Function Transformations
# Subsection: Translation of Functions
# Description: Original function and translated function on same axes. Use different colors or line styles. Arrows showing horizontal and vertical shifts. Label f(x) and f(x-a)+b with specific values.

# Generate function translation
# Original: f(x) = x^2
# Translated: f(x-1) + 2 = (x-1)^2 + 2
x = np.linspace(-2, 4, 100)
y_original = x**2
y_translated = (x - 1) ** 2 + 2

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
original_color = "#6b46c1"  # Purple for original
translated_color = "#ec3059"  # Red for translated

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
    # Translated function: f(x-1) + 2
    {
        "type": "curve",
        "id": "translated",
        "data": {"x": x.tolist(), "y": y_translated.tolist()},
        "stroke": translated_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,5",
        "fill": "none",
        "class": "curve translated",
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
        "x": 1,
        "y": 7.5,
        "latex": r"Function Translation",
        "width": 160,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 1,
        "y": 7,
        "latex": r"f(x) = x^2",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": original_color,
    },
    {
        "x": 1,
        "y": 6.5,
        "latex": r"f(x-1) + 2",
        "width": 90,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": translated_color,
    },
    {
        "x": 1.2,
        "y": 2.2,
        "latex": r"Right 1, Up 2",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_function_transformations_translation_of_functions",
        "title": "Translation of Functions",
        "description": "Function translation showing f(x) = x² and f(x-1) + 2",
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
