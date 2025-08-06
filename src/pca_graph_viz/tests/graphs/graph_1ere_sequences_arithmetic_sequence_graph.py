import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Sequences
# Subsection: Arithmetic Sequence Graph
# Description: Discrete points on a coordinate plane showing terms of an arithmetic sequence.
# Each point represents a term, with x-coordinate as term number (n) and y-coordinate as term value (uₙ).
# The common difference d is visible as the constant slope between consecutive points.

# Generate arithmetic sequence: uₙ = 2n + 1 (first term u₁ = 3, common difference d = 2)
n = np.arange(1, 8)  # Term numbers 1 to 7
u_n = 2 * n + 1  # Term values: 3, 5, 7, 9, 11, 13, 15

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
        "x2": 8,
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
        "y2": 16,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 4,
        "y": 17,
        "latex": r"Arithmetic Sequence: u_n = 2n + 1",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 4,
        "y": 15.5,
        "latex": r"u_1 = 3, d = 2",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.2,
        "y": 3.2,
        "latex": r"u_1 = 3",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 2.2,
        "y": 5.2,
        "latex": r"u_2 = 5",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 3.2,
        "y": 7.2,
        "latex": r"u_3 = 7",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 4.2,
        "y": 9.2,
        "latex": r"u_4 = 9",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 5.2,
        "y": 11.2,
        "latex": r"u_5 = 11",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 6.2,
        "y": 13.2,
        "latex": r"u_6 = 13",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
    {
        "x": 7.2,
        "y": 15.2,
        "latex": r"u_7 = 15",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_sequences_arithmetic_sequence_graph",
        "title": "Arithmetic Sequence Graph",
        "description": "Arithmetic sequence uₙ = 2n + 1 showing discrete points with common difference d = 2",
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
