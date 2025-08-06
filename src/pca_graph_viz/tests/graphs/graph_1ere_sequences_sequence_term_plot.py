import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Sequences
# Subsection: Sequence Term Plot (Discrete)
# Description: A coordinate system with discrete points (n, uₙ) plotted. X-axis shows term number n (integers only), y-axis shows term value uₙ. Points are not connected (emphasize discrete nature). First few terms labeled u₁, u₂, u₃, etc.

# Generate discrete sequence: uₙ = n² (square numbers)
n = np.arange(1, 6)  # Term numbers 1 to 5
u_n = n**2  # Term values: 1, 4, 9, 16, 25

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
point_color = "#6b46c1"  # Purple for points

# All visual elements in lines array
lines = [
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
        "y2": 26,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 3,
        "y": 28,
        "latex": r"Discrete Sequence: u_n = n^2",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 1.2,
        "y": 1.2,
        "latex": r"u_1 = 1",
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
        "y": 9.2,
        "latex": r"u_3 = 9",
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
        "y": 25.2,
        "latex": r"u_5 = 25",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": point_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_sequences_sequence_term_plot",
        "title": "Sequence Term Plot (Discrete)",
        "description": "Discrete sequence uₙ = n² showing individual points without connecting lines",
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
