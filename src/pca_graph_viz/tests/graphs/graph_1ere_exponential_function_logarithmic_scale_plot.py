import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Exponential Function
# Subsection: Logarithmic Scale Plot
# Description: A semi-log plot where y-axis uses logarithmic scale. Exponential functions appear as straight lines. Useful for comparing exponential growth rates. Include grid lines at powers of 10 or e.

# Generate logarithmic scale plot
# On log scale, exponential functions become straight lines
x = np.linspace(0, 3, 100)
y1 = np.exp(x)  # y = e^x
y2 = np.exp(2 * x)  # y = e^(2x)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line1_color = "#6b46c1"  # Purple for e^x
line2_color = "#ec3059"  # Red for e^(2x)

# All visual elements in lines array
lines = [
    # Line 1: y = e^x (appears straight on log scale)
    {
        "type": "curve",
        "id": "exp_x_log",
        "data": {"x": x.tolist(), "y": y1.tolist()},
        "stroke": line1_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve exp-x-log",
    },
    # Line 2: y = e^(2x) (appears straight on log scale)
    {
        "type": "curve",
        "id": "exp_2x_log",
        "data": {"x": x.tolist(), "y": y2.tolist()},
        "stroke": line2_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve exp-2x-log",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": 1,
        "x2": 3,
        "y2": 1,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis x-axis",
    },
    # Y-axis (log scale)
    {
        "type": "axis",
        "x1": 0,
        "y1": 1,
        "x2": 0,
        "y2": 20,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 1.5,
        "y": 22,
        "latex": r"Logarithmic Scale Plot",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 1.5,
        "y": 21.5,
        "latex": r"y = e^x",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line1_color,
    },
    {
        "x": 1.5,
        "y": 21,
        "latex": r"y = e^{2x}",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line2_color,
    },
    {
        "x": 0.2,
        "y": 1.5,
        "latex": r"1",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.2,
        "y": 2.7,
        "latex": r"e",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.2,
        "y": 7.4,
        "latex": r"e^2",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_exponential_function_logarithmic_scale_plot",
        "title": "Logarithmic Scale Plot",
        "description": "Semi-log plot showing exponential functions as straight lines",
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
