"""
Upward parabola with negative shift (y = x^2 - a).

When executed via Nagini from JavaScript (sujets0-app-simple.js),
the A_SHIFT_MAGNITUDE variable is injected into this module's namespace
before execution, allowing dynamic configuration of the label display.

The value can be changed using the control panel in sujets0-simple.html.
"""

from spe_sujet1_auto_10_question_small_dispatch import generate_parabola_graph

# Try to get the value from the namespace injected by Nagini/Pyodide
# If not found (e.g., when running locally without Nagini), use default value
try:
    # When executed via Nagini, this value is injected into globals()
    A_SHIFT_MAGNITUDE = globals()["A_SHIFT_MAGNITUDE"]
    print(f"✅ Using injected A_SHIFT_MAGNITUDE = {A_SHIFT_MAGNITUDE} for s1_a_m label")
except KeyError:
    # Default value when not running via Nagini or value not injected
    A_SHIFT_MAGNITUDE = 5
    print(f"⚠️ Using default A_SHIFT_MAGNITUDE = {A_SHIFT_MAGNITUDE} for s1_a_m label")

# Configuration for this specific parabola
PARABOLA_SIGN = 1  # +1 for y = x^2 + a
A_SHIFT_FOR_CASE = -5  # Fixed value for matching graph case
A_SHIFT_FOR_LABEL = -A_SHIFT_MAGNITUDE  # Dynamic value for label display
A_ADJUST = 0  # Fine-tuning adjustment for curve position (not shown in labels)


def get_graph_dict():
    """Return the graph dictionary for this configuration."""
    return generate_parabola_graph(
        PARABOLA_SIGN,
        A_SHIFT_FOR_CASE,
        "spe_sujet1_auto_10_question_small_parabola_a_s1_a_m.py",
        A_SHIFT_FOR_LABEL,
        A_ADJUST,
    )
