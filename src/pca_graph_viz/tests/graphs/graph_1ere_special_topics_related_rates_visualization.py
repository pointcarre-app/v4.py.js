import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Related Rates Visualization
# Description: A changing geometric situation (e.g., ladder sliding down wall). Multiple positions shown with time stamps. Rates of change (dx/dt, dy/dt) indicated with arrows. Pythagorean or other relationship highlighted.

# Generate related rates problem: Ladder sliding down wall
# Ladder length = 10, positions at different times
# x² + y² = 100 (Pythagorean theorem)

# Different positions of the ladder
x_positions = [8, 6, 4, 2]  # x-coordinates
y_positions = [np.sqrt(100 - x**2) for x in x_positions]  # y-coordinates

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
ladder_color = "#6b46c1"  # Purple for ladder

# All visual elements in lines array
lines = [
    # Wall (y-axis)
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": 0,
        "y2": 10,
        "stroke": "#666666",
        "stroke-width": 3,
        "class": "wall",
    },
    # Ground (x-axis)
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": 10,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 3,
        "class": "ground",
    },
]

# Add ladder positions
for i, (x, y) in enumerate(zip(x_positions, y_positions)):
    lines.append(
        {
            "type": "line",
            "x1": 0,
            "y1": y,
            "x2": x,
            "y2": 0,
            "stroke": ladder_color,
            "stroke-width": 2,
            "stroke-opacity": 0.7 - i * 0.15,
            "class": f"ladder-position-{i}",
        }
    )

foreign_objects = [
    {
        "x": 0.5,
        "y": 9.5,
        "latex": r"Related Rates: Ladder Problem",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 0.5,
        "y": 9,
        "latex": r"x^2 + y^2 = 100",
        "width": 120,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 8.5,
        "y": 6,
        "latex": r"t = 0",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": ladder_color,
    },
    {
        "x": 6.5,
        "y": 8,
        "latex": r"t = 1",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": ladder_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_related_rates_visualization",
        "title": "Related Rates Visualization",
        "description": "Ladder sliding down wall problem showing multiple positions over time",
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
