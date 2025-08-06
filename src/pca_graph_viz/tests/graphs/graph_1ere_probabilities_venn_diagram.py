import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Probabilities and Conditional Probabilities
# Subsection: Venn Diagram for Events
# Description: Overlapping circles or ovals representing different events within a rectangular universe.
# The overlap shows intersection of events, useful for visualizing P(A∩B), P(A∪B), and complement events.
# Areas can be proportional to probabilities.

# Generate Venn diagram with two overlapping circles
# Circle A: center at (-0.5, 0), radius 1
# Circle B: center at (0.5, 0), radius 1

# Generate circle A
theta = np.linspace(0, 2*np.pi, 100)
x_circle_a = -0.5 + np.cos(theta)
y_circle_a = np.sin(theta)

# Generate circle B
x_circle_b = 0.5 + np.cos(theta)
y_circle_b = np.sin(theta)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
circle_a_color = "#6b46c1"  # Purple for circle A
circle_b_color = "#ab0084"  # Pink for circle B

# All visual elements in lines array
lines = [
    # Circle A
    {
        "type": "curve",
        "id": "circle_a",
        "data": {"x": x_circle_a.tolist(), "y": y_circle_a.tolist()},
        "stroke": circle_a_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "circle event-a",
    },
    # Circle B
    {
        "type": "curve",
        "id": "circle_b",
        "data": {"x": x_circle_b.tolist(), "y": y_circle_b.tolist()},
        "stroke": circle_b_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "circle event-b",
    },
]

foreign_objects = [
    {
        "x": -0.5,
        "y": 1.2,
        "latex": r"Event A",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": circle_a_color,
    },
    {
        "x": 0.5,
        "y": 1.2,
        "latex": r"Event B",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": circle_b_color,
    },
    {
        "x": 0,
        "y": 0.2,
        "latex": r"A \cap B",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0,
        "y": -1.2,
        "latex": r"P(A \cap B)",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_probabilities_venn_diagram",
        "title": "Venn Diagram for Events",
        "description": "Two overlapping circles representing events A and B, showing intersection A∩B",
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
