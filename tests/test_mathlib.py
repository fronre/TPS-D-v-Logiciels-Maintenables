import pytest
from src.mathlib import factorial

@pytest.mark.parametrize("n, expected_result", [(0, 1), (1, 1), (2, 2)] )
def test_factorial(n, expected_result):
    actual_result = factorial(n)
    assert factorial(n) == expected_result

