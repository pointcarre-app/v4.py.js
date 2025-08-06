import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Random Variables and Statistics
# Subsection: Histogram with Normal Curve
# Description: A histogram showing the frequency distribution of data, with a smooth normal curve overlaid.
# The histogram shows the actual data distribution, while the normal curve shows the theoretical normal distribution.
# Useful for comparing empirical data to theoretical normal distribution.

# Generate histogram with normal curve
# Example: Data approximately normally distributed around mean μ = 5, σ = 1.5
x_hist = [2, 3, 4, 5, 6, 7, 8]  # Bin centers
frequencies = [0.05, 0.15, 0.25, 0.3, 0.2, 0.04, 0.01]  # Relative frequencies

# Normal curve parameters
mu = 5  # mean
sigma = 1.5  # standard deviation
x_normal = np.linspace(1, 9, 100)
y_normal = 0.3 * np.exp(-0.5 * ((x_normal - mu) / sigma) ** 2)  # Scaled normal curve

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
hist_color = "#6b46c1"  # Purple for histogram
curve_color = "#ec3059"  # Red for normal curve

# All visual elements in lines array
lines = [
    # Histogram bars
    {
        "type": "line",
        "x1": 2,
        "y1": 0,
        "x2": 2,
        "y2": 0.05,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    {
        "type": "line",
        "x1": 3,
        "y1": 0,
        "x2": 3,
        "y2": 0.15,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    {
        "type": "line",
        "x1": 4,
        "y1": 0,
        "x2": 4,
        "y2": 0.25,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    {
        "type": "line",
        "x1": 5,
        "y1": 0,
        "x2": 5,
        "y2": 0.3,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    {
        "type": "line",
        "x1": 6,
        "y1": 0,
        "x2": 6,
        "y2": 0.2,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    {
        "type": "line",
        "x1": 7,
        "y1": 0,
        "x2": 7,
        "y2": 0.04,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    {
        "type": "line",
        "x1": 8,
        "y1": 0,
        "x2": 8,
        "y2": 0.01,
        "stroke": hist_color,
        "stroke-width": 1.5,
        "class": "histogram-bar",
    },
    # Normal curve
    {
        "type": "curve",
        "id": "normal_curve",
        "data": {"x": x_normal.tolist(), "y": y_normal.tolist()},
        "stroke": curve_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve normal",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 1,
        "y1": 0,
        "x2": 9,
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
        "y2": 0.35,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 5,
        "y": 0.4,
        "latex": r"Histogram with Normal Curve",
        "width": 200,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 5,
        "y": 0.37,
        "latex": r"\mu = 5, \sigma = 1.5",
        "width": 120,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.2,
        "y": -0.05,
        "latex": r"0",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 5.2,
        "y": -0.05,
        "latex": r"5",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 8.2,
        "y": -0.05,
        "latex": r"8",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_random_variables_and_statistics_histogram_with_normal_curve",
        "title": "Histogram with Normal Curve",
        "description": "Histogram showing data distribution with overlaid normal curve (μ = 5, σ = 1.5)",
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
