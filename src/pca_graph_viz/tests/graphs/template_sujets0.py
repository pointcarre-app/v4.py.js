"""
Template for creating new Sujets 0 graphs.

To use this template:
1. Copy this file and rename it to: graph_sujets0_spe_sujet{N}_automatismes_question{M}.py
   where N is the subject number and M is the question number
2. Update the graph content with your specific visualization
3. Add the file to scenery/sujets0-app.js in the pythonFiles array
4. Add question data to the questionData object in sujets0-app.js
"""

import numpy as np

# Graph: [sujets0][spé][sujet-{N}][automatismes][question-{M}]
# Question: [Your question text here]
# Topic: [Mathematical topic]

# Generate your data here
x = np.linspace(-5, 5, 100)
y = x**2  # Example: parabola

# Define colors
bg_color = "#f8f9fb"
grid_color = "#e0e4eb"
curve_color = "#4a90e2"

# Define visual elements
lines = [
    # Grid (optional)
    # X-axis
    {
        "type": "axis",
        "x1": -5,
        "y1": 0,
        "x2": 5,
        "y2": 0,
        "stroke": "#333333",
        "stroke-width": 1.5,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -5,
        "x2": 0,
        "y2": 5,
        "stroke": "#333333",
        "stroke-width": 1.5,
        "class": "axis y-axis",
    },
    # Main curve
    {
        "type": "curve",
        "id": "main-curve",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": curve_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "curve",
    },
    # Add more visual elements as needed
]

# Define text labels with LaTeX
foreign_objects = [
    {
        "x": 0.5,
        "y": 4.5,
        "latex": r"y = x^2",  # Example formula
        "width": 70,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.95)",
        "text_color": curve_color,
    },
    # Add more labels as needed
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "[sujets0][spé][sujet-{N}][automatismes][question-{M}]",
        "title": "Question {M} - [Brief description]",
        "description": "[Detailed description of what the graph shows]",
        "svg": {
            "width": 400,
            "height": 400,
            "viewBox": "0 0 400 400",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 20,
            "show_axes": False,  # We draw our own axes
            "show_grid": False,   # We draw our own grid if needed
            "grid_color": grid_color,
            "axes_color": "#333333",
            "x_range": [-5, 5],
            "y_range": [-5, 5],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }


