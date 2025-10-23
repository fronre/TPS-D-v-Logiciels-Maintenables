import pytest
from src.mathlib import factorial

import pytest
from src.mathlib import factorial

@pytest.mark.parametrize("n, expected_result", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial(n, expected_result):
    actual_result = factorial(n)
    assert actual_result == expected_result
