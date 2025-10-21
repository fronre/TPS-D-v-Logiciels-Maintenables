import pytest
from src.mathlib import factorial

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120)
])
def test_factorial_values(n, expected):
    assert factorial(n) == expected

@pytest.mark.parametrize("base, exp, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (3, 2, 9)
])
def test_power_values(base, exp, expected):
    from src.mathlib import power
    assert power(base, exp) == expected
