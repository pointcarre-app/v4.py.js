# Graph: Première Spécialité Mathématiques
# Section: Random Variables and Statistics
# Subsection: Cumulative Distribution Function
# Description: A step function that starts at 0 and increases to 1, showing P(X ≤ x).
# For discrete variables, it's a step function with jumps at each value.
# For continuous variables, it's a smooth increasing function from 0 to 1.

# Generate cumulative distribution function for discrete random variable
# Example: X takes values 1, 2, 3 with probabilities 0.3, 0.5, 0.2
x_values = [0, 1, 1, 2, 2, 3, 3, 4]  # x-coordinates for step function
y_values = [0, 0, 0.3, 0.3, 0.8, 0.8, 1.0, 1.0]  # cumulative probabilities

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
step_color = "#6b46c1"  # Purple for step function

# All visual elements in lines array
lines = [
    # Step function (CDF)
    {
        "type": "curve",
        "id": "cdf",
        "data": {"x": x_values, "y": y_values},
        "stroke": step_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve cdf",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
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
        "y2": 1.2,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 2,
        "y": 1.4,
        "latex": r"Cumulative Distribution Function",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 2,
        "y": 1.2,
        "latex": r"F(x) = P(X \leq x)",
        "width": 120,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.2,
        "y": 0.4,
        "latex": r"0.3",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": step_color,
    },
    {
        "x": 2.2,
        "y": 0.9,
        "latex": r"0.8",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": step_color,
    },
    {
        "x": 3.2,
        "y": 1.1,
        "latex": r"1.0",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": step_color,
    },
    {
        "x": 0.2,
        "y": -0.2,
        "latex": r"0",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.2,
        "y": -0.2,
        "latex": r"1",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 2.2,
        "y": -0.2,
        "latex": r"2",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 3.2,
        "y": -0.2,
        "latex": r"3",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_random_variables_and_statistics_cumulative_distribution_function",
        "title": "Cumulative Distribution Function",
        "description": "Step function showing cumulative distribution function F(x) = P(X ≤ x)",
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
