# Graph: Première Spécialité Mathématiques
# Section: Random Variables and Statistics
# Subsection: Box Plot
# Description: A box plot showing the five-number summary: minimum, first quartile (Q1), median, third quartile (Q3), and maximum.
# The box shows the interquartile range (IQR), and whiskers extend to the most extreme non-outlier points.
# Outliers are marked as individual points beyond the whiskers.

# Generate sample data for box plot
# Example: [2, 3, 4, 5, 6, 7, 8, 9, 10, 15] (with outlier 15)
data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
q1 = 4.5  # First quartile
median = 6.5  # Median
q3 = 8.5  # Third quartile
min_val = 2  # Minimum
max_val = 10  # Maximum (excluding outlier)
outlier = 15  # Outlier

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
box_color = "#6b46c1"  # Purple for box
whisker_color = "#ab0084"  # Pink for whiskers

# All visual elements in lines array
lines = [
    # Box (Q1 to Q3)
    {
        "type": "line",
        "x1": q1,
        "y1": 0.5,
        "x2": q3,
        "y2": 0.5,
        "stroke": box_color,
        "stroke-width": 8,
        "class": "box",
    },
    # Median line
    {
        "type": "line",
        "x1": median,
        "y1": 0.2,
        "x2": median,
        "y2": 0.8,
        "stroke": "#ec3059",
        "stroke-width": 2,
        "class": "median",
    },
    # Lower whisker
    {
        "type": "line",
        "x1": min_val,
        "y1": 0.5,
        "x2": q1,
        "y2": 0.5,
        "stroke": whisker_color,
        "stroke-width": 2,
        "class": "whisker",
    },
    # Upper whisker
    {
        "type": "line",
        "x1": q3,
        "y1": 0.5,
        "x2": max_val,
        "y2": 0.5,
        "stroke": whisker_color,
        "stroke-width": 2,
        "class": "whisker",
    },
    # Whisker caps
    {
        "type": "line",
        "x1": min_val,
        "y1": 0.3,
        "x2": min_val,
        "y2": 0.7,
        "stroke": whisker_color,
        "stroke-width": 2,
        "class": "whisker-cap",
    },
    {
        "type": "line",
        "x1": max_val,
        "y1": 0.3,
        "x2": max_val,
        "y2": 0.7,
        "stroke": whisker_color,
        "stroke-width": 2,
        "class": "whisker-cap",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": 0,
        "x2": 16,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis x-axis",
    },
]

foreign_objects = [
    {
        "x": 8,
        "y": 1.5,
        "latex": r"Box Plot",
        "width": 80,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 8,
        "y": 1.2,
        "latex": r"Q1 = 4.5, Q2 = 6.5, Q3 = 8.5",
        "width": 180,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 2.2,
        "y": -0.3,
        "latex": r"2",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 6.5,
        "y": -0.3,
        "latex": r"6.5",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
    {
        "x": 10.2,
        "y": -0.3,
        "latex": r"10",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 15.2,
        "y": 0.2,
        "latex": r"15*",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_random_variables_and_statistics_box_plot",
        "title": "Box Plot",
        "description": "Box plot showing five-number summary with outlier marked",
        "svg": {
            "width": 400,
            "height": 200,
            "viewBox": "0 0 400 200",
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
