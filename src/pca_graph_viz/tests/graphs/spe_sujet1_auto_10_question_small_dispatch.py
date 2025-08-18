import numpy as np

# Rendering/domain constants
SAMPLES = 1000
_X_BASE_MIN, _X_BASE_MAX = -4, 4


def _compute_display_ranges(
    parabola_sign: int, a_shift: float, x_base_min: float, x_base_max: float
) -> tuple[float, float, float, float]:
    """Compute display X/Y ranges for y = sign * x^2 + a.

    Ensures:
    - X range has small padding around [x_base_min, x_base_max]
    - Y range fully contains the function range on that domain
    - Always includes 0 for axis visibility with adequate margin
    """
    # X range with mild padding
    x_min_raw, x_max_raw = float(x_base_min), float(x_base_max)
    x_span = x_max_raw - x_min_raw
    x_pad = 0.1 * x_span
    X_MIN, X_MAX = x_min_raw - x_pad, x_max_raw + x_pad

    # Analytic Y range on symmetric domain
    if parabola_sign == 1:
        func_y_min = a_shift
        func_y_max = a_shift + (x_base_max**2)
    else:
        func_y_max = a_shift
        func_y_min = a_shift - (x_base_max**2)

    # Handle special cases for extreme shifts to ensure axes are visible
    if parabola_sign == -1 and a_shift == -10:
        # Function range is [-26, -10]
        Y_MIN = -30  # Show the full parabola with padding
        Y_MAX = 3  # Include 0 with reasonable margin above
    elif parabola_sign == -1 and a_shift == -5:
        # Function range is [-21, -5]
        Y_MIN = -24  # Show the full parabola with padding
        Y_MAX = 3  # Include 0 with reasonable margin above
    elif parabola_sign == 1 and a_shift == 10:
        # Function range is [10, 26]
        Y_MIN = -3  # Include 0 with reasonable margin below
        Y_MAX = 30  # Show the full parabola with padding
    elif parabola_sign == 1 and a_shift == 5:
        # Function range is [5, 21]
        Y_MIN = -3  # Include 0 with reasonable margin below
        Y_MAX = 24  # Show the full parabola with padding
    else:
        # Default logic for other cases
        func_span = max(1.0, func_y_max - func_y_min)
        pad = 0.15 * func_span

        if func_y_min >= 0.0:
            # Entirely above zero: ensure we go at least 2 below 0
            Y_MIN = min(-2.0, func_y_min - pad)
            Y_MAX = func_y_max + pad
        elif func_y_max <= 0.0:
            # Entirely below zero: ensure we go at least 2 above 0
            Y_MAX = max(2.0, func_y_max + pad)
            Y_MIN = func_y_min - pad
        else:
            # Crosses zero naturally
            Y_MIN = func_y_min - pad
            Y_MAX = func_y_max + pad

    return X_MIN, X_MAX, Y_MIN, Y_MAX


def generate_parabola_graph(parabola_sign: int, a_shift: float, filename: str):
    """Generate a parabola graph with the given parameters.

    Args:
        parabola_sign: +1 for y = x^2 + a, -1 for y = -x^2 + a
        a_shift: The vertical shift value 'a'
        filename: The filename to use as the title

    Returns:
        A dictionary containing the graph data
    """
    # Generate data
    x = np.linspace(_X_BASE_MIN, _X_BASE_MAX, SAMPLES)
    y = parabola_sign * (x**2) + a_shift

    # Compute display ranges
    X_MIN, X_MAX, Y_MIN, Y_MAX = _compute_display_ranges(
        parabola_sign, a_shift, _X_BASE_MIN, _X_BASE_MAX
    )

    x_span = X_MAX - X_MIN
    y_span = Y_MAX - Y_MIN

    # Visual elements
    lines = [
        # X-axis
        {
            "type": "axis",
            "x1": X_MIN,
            "y1": 0,
            "x2": X_MAX,
            "y2": 0,
            "stroke-width": 1.5,
            "class": "axis x-axis stroke-base-content",
        },
        # Y-axis
        {
            "type": "axis",
            "x1": 0,
            "y1": Y_MIN,
            "x2": 0,
            "y2": Y_MAX + 0.2,
            "stroke-width": 1.5,
            "class": "axis y-axis stroke-base-content",
        },
        # Parabola curve
        {
            "type": "curve",
            "id": "parabola",
            "data": {"x": x.tolist(), "y": y.tolist()},
            "stroke-width": 2,
            "fill": "none",
            "class": "curve stroke-primary",
        },
    ]

    # Handle label positioning for extreme shifts
    if parabola_sign == -1 and a_shift in [-10, -5]:
        # For negative parabolas shifted far below
        x_label_y = -1.0
        y_label_y = 2.5
    elif parabola_sign == 1 and a_shift == 10:
        # For positive parabola shifted far above
        x_label_y = -1.0
        y_label_y = 28.5
    elif parabola_sign == 1 and a_shift == 5:
        # For positive parabola shifted moderately above
        x_label_y = -1.0
        y_label_y = 22.5
    else:
        # Default positioning
        x_label_y = 0 - 0.06 * y_span
        y_label_y = Y_MAX - 0.02 * y_span

    foreign_objects = [
        # X axis label at right end, slightly below the axis
        {
            "x": 3.5
            if (parabola_sign in [-1, 1] and abs(a_shift) in [5, 10])
            else X_MAX - 0.04 * x_span,
            "y": x_label_y,
            "latex": "x",
            "width": 20,
            "height": 10,
            "class": "svg-latex fill-base-content",
        },
        # Y axis label near top, slightly to the right of the axis
        {
            "x": 0.3
            if (parabola_sign in [-1, 1] and abs(a_shift) in [5, 10])
            else 0 + 0.04 * x_span,
            "y": y_label_y,
            "latex": "y",
            "width": 20,
            "height": 20,
            "class": "svg-latex fill-base-content",
        },
    ]

    return {
        "id": f"parabola_sign_{parabola_sign}_a_{int(a_shift)}_small",
        "title": filename,
        "description": f"Parabola y = {'x^2' if parabola_sign == 1 else '-x^2'} + a with a={a_shift}",
        "svg": {
            "width": 150,
            "height": 150,
            "viewBox": "0 0 150 150",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": {"top": 10, "right": 10, "bottom": 28, "left": 10},
            "show_axes": False,
            "show_grid": False,
            "x_range": [X_MIN, X_MAX],
            "y_range": [Y_MIN, Y_MAX],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }


# For direct testing/usage
def get_graph_dict():
    """Default graph for testing - can be overridden by importing modules."""
    return generate_parabola_graph(1, 0, "spe_sujet1_auto_10_question_small_dispatch.py")
