import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Probabilities and Conditional Probabilities
# Subsection: Probability Tree Diagram
# Description: A branching diagram starting from a single point, with branches representing different outcomes.
# Each branch is labeled with its probability, and the sum of probabilities from any node equals 1.
# Multiple levels show sequential events, with conditional probabilities on second-level branches.

# Generate probability tree diagram
# Example: Coin flip followed by dice roll
# Level 1: Heads (0.5) or Tails (0.5)
# Level 2: If Heads, roll 1-3 (0.5) or 4-6 (0.5)
# Level 2: If Tails, roll 1-2 (0.33) or 3-6 (0.67)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for branches

# All visual elements in lines array
lines = [
    # Root to Heads
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": -1,
        "y2": -1,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "branch heads",
    },
    # Root to Tails
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": 1,
        "y2": -1,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "branch tails",
    },
    # Heads to 1-3
    {
        "type": "line",
        "x1": -1,
        "y1": -1,
        "x2": -1.5,
        "y2": -2,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "branch dice-1-3",
    },
    # Heads to 4-6
    {
        "type": "line",
        "x1": -1,
        "y1": -1,
        "x2": -0.5,
        "y2": -2,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "branch dice-4-6",
    },
    # Tails to 1-2
    {
        "type": "line",
        "x1": 1,
        "y1": -1,
        "x2": 0.5,
        "y2": -2,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "branch dice-1-2",
    },
    # Tails to 3-6
    {
        "type": "line",
        "x1": 1,
        "y1": -1,
        "x2": 1.5,
        "y2": -2,
        "stroke": line_color,
        "stroke-width": 2,
        "class": "branch dice-3-6",
    },
]

foreign_objects = [
    {
        "x": 0,
        "y": 0.3,
        "latex": r"Start",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -1,
        "y": -0.7,
        "latex": r"Heads (0.5)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color,
    },
    {
        "x": 1,
        "y": -0.7,
        "latex": r"Tails (0.5)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color,
    },
    {
        "x": -1.5,
        "y": -1.7,
        "latex": r"1-3 (0.5)",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": -0.5,
        "y": -1.7,
        "latex": r"4-6 (0.5)",
        "width": 70,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 0.5,
        "y": -1.7,
        "latex": r"1-2 (0.33)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 1.5,
        "y": -1.7,
        "latex": r"3-6 (0.67)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_probabilities_tree_diagram",
        "title": "Probability Tree Diagram",
        "description": "Probability tree showing coin flip followed by conditional dice roll outcomes",
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
