
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

