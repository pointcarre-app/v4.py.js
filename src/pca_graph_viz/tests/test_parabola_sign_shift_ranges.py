import importlib
import types


def _load(module_path: str) -> types.ModuleType:
    return importlib.import_module(module_path)


def _compute_function_range(sign: int, a: float, x_max: float) -> tuple[float, float]:
    if sign == 1:
        return a, a + x_max**2
    else:
        return a - x_max**2, a


def _assert_display_ok(m):
    # Access constants from the module
    sign = m.PARABOLA_SIGN
    a = m.A_SHIFT
    X_MIN, X_MAX = m.X_MIN, m.X_MAX
    Y_MIN, Y_MAX = m.Y_MIN, m.Y_MAX

    # Function range should lie within display Y range
    func_y_min, func_y_max = _compute_function_range(sign, a, 4.0)
    assert Y_MIN < func_y_min < Y_MAX
    assert Y_MIN < func_y_max < Y_MAX

    # If function is entirely above or below 0, ensure x-axis margin >= 2
    if func_y_min >= 0:
        assert Y_MIN <= -2
    if func_y_max <= 0:
        assert Y_MAX >= 2

    # Sanity on X padding
    assert X_MIN < -4 and X_MAX > 4


def test_all_combinations():
    # ten combinations: sign in {1,-1} x a in {-10, -5, 0, 5, 10}
    signs = [1, -1]
    shifts = [-10, -5, 0, 5, 10]

    # We'll reuse the two graph modules by monkey-patching constants via importlib.reload
    # Use the configurable module for systematic testing
    mod = _load("pca_graph_viz.tests.graphs.spe_sujet1_auto_10_question_small_parabola_a")
    for s in signs:
        for a in shifts:
            mod.configure(s, a)
            _assert_display_ok(mod)
