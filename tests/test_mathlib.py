import pytest
from src.mathlib import factorial

@pytest.mark.parametrize("number", [0, 1])
def test_factorial_0_or_1_return_1(number):
    assert factorial(number) == 1
