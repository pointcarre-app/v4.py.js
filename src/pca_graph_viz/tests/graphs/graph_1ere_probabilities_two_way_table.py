# Graph: Première Spécialité Mathématiques
# Section: Probabilities and Conditional Probabilities
# Subsection: Two-Way Table
# Description: A rectangular table with rows and columns representing different categories.
# Each cell contains the count or frequency for the intersection of row and column categories.
# Row and column totals are shown, useful for calculating conditional probabilities.

# Generate two-way table visualization
# Example: Gender vs. Favorite Color
# Rows: Male, Female
# Columns: Red, Blue, Green

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
table_color = "#6b46c1"  # Purple for table lines

# All visual elements in lines array
lines = [
    # Table border
    {
        "type": "line",
        "x1": -2,
        "y1": 1,
        "x2": 2,
        "y2": 1,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-top",
    },
    {
        "type": "line",
        "x1": -2,
        "y1": 1,
        "x2": -2,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-left",
    },
    {
        "type": "line",
        "x1": 2,
        "y1": 1,
        "x2": 2,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-right",
    },
    {
        "type": "line",
        "x1": -2,
        "y1": -2,
        "x2": 2,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-bottom",
    },
    # Vertical dividers
    {
        "type": "line",
        "x1": -0.5,
        "y1": 1,
        "x2": -0.5,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
    {
        "type": "line",
        "x1": 0.5,
        "y1": 1,
        "x2": 0.5,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
    # Horizontal dividers
    {
        "type": "line",
        "x1": -2,
        "y1": 0,
        "x2": 2,
        "y2": 0,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
    {
        "type": "line",
        "x1": -2,
        "y1": -1,
        "x2": 2,
        "y2": -1,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
]

foreign_objects = [
    {
        "x": 0,
        "y": 1.5,
        "latex": r"Two-Way Table",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -1.25,
        "y": 0.5,
        "latex": r"Male",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": -1.25,
        "y": -0.5,
        "latex": r"Female",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": -0.25,
        "y": 0.5,
        "latex": r"Red",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.25,
        "y": 0.5,
        "latex": r"Blue",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.25,
        "y": 0.5,
        "latex": r"Green",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": -0.25,
        "y": -0.5,
        "latex": r"15",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 0.25,
        "y": -0.5,
        "latex": r"20",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 1.25,
        "y": -0.5,
        "latex": r"25",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": -0.25,
        "y": -1.5,
        "latex": r"10",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 0.25,
        "y": -1.5,
        "latex": r"30",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": 1.25,
        "y": -1.5,
        "latex": r"15",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_probabilities_two_way_table",
        "title": "Two-Way Table",
        "description": "Contingency table showing gender vs. favorite color with frequency counts",
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
