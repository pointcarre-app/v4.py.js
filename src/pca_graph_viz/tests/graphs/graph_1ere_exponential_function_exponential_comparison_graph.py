import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Exponential Function
# Subsection: Exponential Comparison Graph
# Description: Multiple exponential curves on the same axes: y = eˣ, y = e²ˣ, y = e⁻ˣ. Different colors distinguish each curve. Shows how coefficient of x affects growth rate. Include y = eˣ as reference curve.

# Generate exponential comparison curves
x = np.linspace(-2, 2, 100)
y1 = np.exp(x)  # y = e^x
y2 = np.exp(2 * x)  # y = e^(2x)
y3 = np.exp(-x)  # y = e^(-x)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
curve1_color = "#6b46c1"  # Purple for e^x
curve2_color = "#ec3059"  # Red for e^(2x)
curve3_color = "#10b981"  # Green for e^(-x)

# All visual elements in lines array
lines = [
    # Curve 1: y = e^x
    {
        "type": "curve",
        "id": "exp_x",
        "data": {"x": x.tolist(), "y": y1.tolist()},
        "stroke": curve1_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve exp-x",
    },
    # Curve 2: y = e^(2x)
    {
        "type": "curve",
        "id": "exp_2x",
        "data": {"x": x.tolist(), "y": y2.tolist()},
        "stroke": curve2_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve exp-2x",
    },
    # Curve 3: y = e^(-x)
    {
        "type": "curve",
        "id": "exp_neg_x",
        "data": {"x": x.tolist(), "y": y3.tolist()},
        "stroke": curve3_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve exp-neg-x",
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
        "latex": r"Exponential Comparison",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": 7,
        "latex": r"y = e^x",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve1_color,
    },
    {
        "x": 0.5,
        "y": 6.5,
        "latex": r"y = e^{2x}",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve2_color,
    },
    {
        "x": 0.5,
        "y": 6,
        "latex": r"y = e^{-x}",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": curve3_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_exponential_function_exponential_comparison_graph",
        "title": "Exponential Comparison Graph",
        "description": "Multiple exponential curves showing different growth rates",
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
