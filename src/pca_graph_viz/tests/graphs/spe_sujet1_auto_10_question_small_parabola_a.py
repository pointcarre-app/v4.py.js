import numpy as np

# CONFIGURABLE CONSTANTS
PARABOLA_SIGN = 1  # +1 for y = x^2 + a, -1 for y = -x^2 + a
A_SHIFT = 0  # allowed values include -10, -5, 0, 5, 10

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
    - If function is entirely above (or below) zero, include at least 2 units
      on the opposite side so the x-axis is visible with margin.
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

    func_span = max(1.0, func_y_max - func_y_min)
    pad = 0.15 * func_span

    if func_y_min >= 0.0:
        Y_MIN = min(-2.0, func_y_min - pad)
        Y_MAX = func_y_max + pad
    elif func_y_max <= 0.0:
        Y_MAX = max(2.0, func_y_max + pad)
        Y_MIN = func_y_min - pad
    else:
        Y_MIN = func_y_min - pad
        Y_MAX = func_y_max + pad

    return X_MIN, X_MAX, Y_MIN, Y_MAX


# Globals derived from configuration
X_MIN: float
X_MAX: float
Y_MIN: float
Y_MAX: float
x: np.ndarray
y: np.ndarray


def configure(parabola_sign: int, a_shift: float) -> None:
    """Set parameters and recompute derived arrays and ranges."""
    global PARABOLA_SIGN, A_SHIFT, X_MIN, X_MAX, Y_MIN, Y_MAX, x, y
    PARABOLA_SIGN = int(parabola_sign)
    A_SHIFT = float(a_shift)
    x = np.linspace(_X_BASE_MIN, _X_BASE_MAX, SAMPLES)
    y = PARABOLA_SIGN * (x**2) + A_SHIFT
    X_MIN, X_MAX, Y_MIN, Y_MAX = _compute_display_ranges(
        PARABOLA_SIGN, A_SHIFT, _X_BASE_MIN, _X_BASE_MAX
    )


# Initialize with default configuration
configure(PARABOLA_SIGN, A_SHIFT)


def get_graph_dict():
    """Return the graph dictionary for the current configuration."""
    sign_label = "plus" if PARABOLA_SIGN == 1 else "minus"
    x_span = X_MAX - X_MIN
    y_span = Y_MAX - Y_MIN

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

    foreign_objects = [
        # X axis label at right end, slightly below the axis
        {
            "x": X_MAX - 0.04 * x_span,
            "y": 0 - 0.06 * y_span,
            "latex": "x",
            "width": 20,
            "height": 10,
            "class": "svg-latex fill-base-content",
        },
        # Y axis label near top, slightly to the right of the axis
        {
            "x": 0 + 0.04 * x_span,
            "y": Y_MAX - 0.02 * y_span,
            "latex": "y",
            "width": 20,
            "height": 20,
            "class": "svg-latex fill-base-content",
        },
    ]

    return {
        "id": f"parabola_sign_{PARABOLA_SIGN}_a_{int(A_SHIFT)}_small",
        "title": "spe_sujet1_auto_10_question_small_parabola_a.py",
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
