#!/usr/bin/env python3
"""Test that the dispatch module works for any value of a between -10 and 10."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from pca_graph_viz.tests.graphs.spe_sujet1_auto_10_question_small_dispatch import (
    _compute_display_ranges,
    generate_parabola_graph,
)


def test_various_a_values():
    """Test with various values of a to ensure they all work."""
    test_values = [
        # Original hardcoded values
        (-1, -10),
        (-1, -5),
        (-1, 0),
        (1, 0),
        (1, 5),
        (1, 10),
        # New test values
        (-1, -7.5),
        (-1, -2.5),
        (-1, 2.5),
        (-1, 7.5),
        (1, -7.5),
        (1, -2.5),
        (1, 2.5),
        (1, 7.5),
        # Edge cases
        (-1, -9.99),
        (1, 9.99),
    ]

    print("Testing dispatch module with various a values:")
    print("-" * 60)

    for sign, a in test_values:
        try:
            # Test range computation
            X_MIN, X_MAX, Y_MIN, Y_MAX = _compute_display_ranges(sign, a, -4, 4)

            # Test graph generation
            graph = generate_parabola_graph(sign, a, f"test_s{sign}_a{a}.py")

            # Check that ranges are reasonable
            x_span = X_MAX - X_MIN
            y_span = Y_MAX - Y_MIN

            status = "✓"
            if y_span > 40:
                status = "⚠️ (large Y span)"
            elif y_span < 5:
                status = "⚠️ (small Y span)"

            sign_str = "+" if sign == 1 else "-"
            func = f"y = {sign_str}x² + {a:6.2f}"
            print(f"{status} {func} -> Y:[{Y_MIN:6.2f}, {Y_MAX:6.2f}] span:{y_span:5.2f}")

        except Exception as e:
            print(f"❌ Failed for sign={sign}, a={a}: {e}")

    print("-" * 60)
    print("Test complete!")


if __name__ == "__main__":
    test_various_a_values()
