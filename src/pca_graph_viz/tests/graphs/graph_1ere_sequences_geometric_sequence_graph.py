import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Sequences
# Subsection: Geometric Sequence Graph
# Description: Discrete points showing exponential growth or decay pattern.
# Each point represents a term, with x-coordinate as term number (n) and y-coordinate as term value (uₙ).
# The common ratio q is visible as the ratio between consecutive terms.

# Generate geometric sequence: uₙ = 2^n (first term u₁ = 2, common ratio q = 2)
n = np.arange(1, 6)  # Term numbers 1 to 5
u_n = 2**n  # Term values: 2, 4, 8, 16, 32

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
point_color = "#6b46c1"  # Purple for points
line_color = "#ab0084"  # Pink for connecting lines

# All visual elements in lines array
lines = [
    # Connecting lines between points
    {
        "type": "curve",
        "id": "sequence_line",
        "data": {"x": n.tolist(), "y": u_n.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,5",
        "fill": "none",
        "class": "sequence-line",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": 0,
        "x2": 6,
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
        "y2": 35,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 3,
        "y": 37,
        "latex": r"Geometric Sequence: u_n = 2^n",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 3,
        "y": 35.5,
        "latex": r"u_1 = 2, q = 2",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.2,
        "y": 2.2,
        "latex": r"u_1 = 2",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 2.2,
        "y": 4.2,
        "latex": r"u_2 = 4",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 3.2,
        "y": 8.2,
        "latex": r"u_3 = 8",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 4.2,
        "y": 16.2,
        "latex": r"u_4 = 16",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 5.2,
        "y": 32.2,
        "latex": r"u_5 = 32",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_sequences_geometric_sequence_graph",
        "title": "Geometric Sequence Graph",
        "description": "Geometric sequence uₙ = 2^n showing exponential growth with common ratio q = 2",
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
