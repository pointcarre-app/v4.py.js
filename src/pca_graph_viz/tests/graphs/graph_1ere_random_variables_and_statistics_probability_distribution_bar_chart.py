# Graph: Première Spécialité Mathématiques
# Section: Random Variables and Statistics
# Subsection: Probability Distribution Bar Chart
# Description: A bar chart showing the probability mass function (PMF) for a discrete random variable.
# Each bar represents the probability P(X = x) for a specific value x.
# The sum of all probabilities equals 1.

# Generate probability distribution bar chart
# Example: Rolling a fair die (values 1-6, each with probability 1/6)
x_values = [1, 2, 3, 4, 5, 6]  # Outcomes
probabilities = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]  # Probabilities

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
bar_color = "#6b46c1"  # Purple for bars

# All visual elements in lines array
lines = [
    # Bar 1
    {
        "type": "line",
        "x1": 1,
        "y1": 0,
        "x2": 1,
        "y2": 1 / 6,
        "stroke": bar_color,
        "stroke-width": 0.8,
        "class": "bar",
    },
    # Bar 2
    {
        "type": "line",
        "x1": 2,
        "y1": 0,
        "x2": 2,
        "y2": 1 / 6,
        "stroke": bar_color,
        "stroke-width": 0.8,
        "class": "bar",
    },
    # Bar 3
    {
        "type": "line",
        "x1": 3,
        "y1": 0,
        "x2": 3,
        "y2": 1 / 6,
        "stroke": bar_color,
        "stroke-width": 0.8,
        "class": "bar",
    },
    # Bar 4
    {
        "type": "line",
        "x1": 4,
        "y1": 0,
        "x2": 4,
        "y2": 1 / 6,
        "stroke": bar_color,
        "stroke-width": 0.8,
        "class": "bar",
    },
    # Bar 5
    {
        "type": "line",
        "x1": 5,
        "y1": 0,
        "x2": 5,
        "y2": 1 / 6,
        "stroke": bar_color,
        "stroke-width": 0.8,
        "class": "bar",
    },
    # Bar 6
    {
        "type": "line",
        "x1": 6,
        "y1": 0,
        "x2": 6,
        "y2": 1 / 6,
        "stroke": bar_color,
        "stroke-width": 0.8,
        "class": "bar",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": 0,
        "x2": 7,
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
        "y2": 0.3,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 3.5,
        "y": 0.35,
        "latex": r"Probability Distribution",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 3.5,
        "y": 0.3,
        "latex": r"P(X = x) = \frac{1}{6}",
        "width": 120,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1,
        "y": 0.2,
        "latex": r"\frac{1}{6}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": bar_color,
    },
    {
        "x": 2,
        "y": 0.2,
        "latex": r"\frac{1}{6}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": bar_color,
    },
    {
        "x": 3,
        "y": 0.2,
        "latex": r"\frac{1}{6}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": bar_color,
    },
    {
        "x": 4,
        "y": 0.2,
        "latex": r"\frac{1}{6}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": bar_color,
    },
    {
        "x": 5,
        "y": 0.2,
        "latex": r"\frac{1}{6}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": bar_color,
    },
    {
        "x": 6,
        "y": 0.2,
        "latex": r"\frac{1}{6}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": bar_color,
    },
    {
        "x": 0.2,
        "y": -0.1,
        "latex": r"0",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.2,
        "y": -0.1,
        "latex": r"1",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 2.2,
        "y": -0.1,
        "latex": r"2",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 3.2,
        "y": -0.1,
        "latex": r"3",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 4.2,
        "y": -0.1,
        "latex": r"4",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 5.2,
        "y": -0.1,
        "latex": r"5",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 6.2,
        "y": -0.1,
        "latex": r"6",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_random_variables_and_statistics_probability_distribution_bar_chart",
        "title": "Probability Distribution Bar Chart",
        "description": "Bar chart showing probability mass function for fair die (P(X = x) = 1/6)",
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
