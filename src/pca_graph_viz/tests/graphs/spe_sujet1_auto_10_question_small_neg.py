import numpy as np

# CONSTANTS (only these differ between the two files)
PARABOLA_SIGN = -1  # +1 for y = x^2 + a, -1 for y = -x^2 + a
A_SHIFT = 4  # a in [1, 10]

# Rendering/domain constants (x-range is expanded dynamically for display)
SAMPLES = 1000


# Data generation
_X_BASE_MIN, _X_BASE_MAX = -4, 4
x = np.linspace(_X_BASE_MIN, _X_BASE_MAX, SAMPLES)
y = PARABOLA_SIGN * (x**2) + A_SHIFT


def _compute_display_ranges(
    parabola_sign: int, a_shift: float, x_base_min: float, x_base_max: float
) -> tuple[float, float, float, float]:
    """Compute display X/Y ranges for y = sign * x^2 + a.

    Ensures:
    - X range has small padding
    - Y range fully contains the function range
    - If the function is entirely above (or below) 0, include at least 2 units beyond 0
      on the opposite side so the x-axis is visible with breathing room.
    """
    # X range with mild padding
    x_min_raw, x_max_raw = float(x_base_min), float(x_base_max)
    x_span = x_max_raw - x_min_raw
    x_pad = 0.1 * x_span
    X_MIN, X_MAX = x_min_raw - x_pad, x_max_raw + x_pad

    # Analytic Y range for quadratic on symmetric domain
    if parabola_sign == 1:
        func_y_min = a_shift
        func_y_max = a_shift + (x_base_max**2)
    else:
        func_y_max = a_shift
        func_y_min = a_shift - (x_base_max**2)

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


X_MIN, X_MAX, Y_MIN, Y_MAX = _compute_display_ranges(
    PARABOLA_SIGN, A_SHIFT, _X_BASE_MIN, _X_BASE_MAX
)


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
    # Parabola curve y = sign*x^2 + a
    {
        "type": "curve",
        "id": "parabola",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve stroke-primary",
    },
]


_x_span = X_MAX - X_MIN
_y_span = Y_MAX - Y_MIN
foreign_objects = [
    # X axis label at right end, slightly below the axis
    {
        "x": X_MAX - 0.04 * _x_span,
        "y": 0 - 0.06 * _y_span,
        "latex": "x",
        "width": 20,
        "height": 10,
        "class": "svg-latex fill-base-content",
    },
    # Y axis label near top, slightly to the right of the axis
    {
        "x": 0 + 0.04 * _x_span,
        "y": Y_MAX - 0.02 * _y_span,
        "latex": "y",
        "width": 20,
        "height": 20,
        "class": "svg-latex fill-base-content",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary for y = sign*x^2 + a."""
    sign_label = "plus" if PARABOLA_SIGN == 1 else "minus"
    return {
        "id": f"parabola-{sign_label}-x2-plus-a-small",
        "title": "spe_sujet1_auto_10_question_small_neg.py",
        "description": f"Parabola y = {'x^2' if PARABOLA_SIGN == 1 else '-x^2'} + a with a={A_SHIFT}",
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
