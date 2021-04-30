from .calc import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_sum(calc):
    result = calc.sum(3,7)
    assert result == 10

def test_sub(calc):
    result = calc.sub(3,7)
    assert result == -4

def test_mult(calc):
    result = calc.mult(3,7)
    assert result == 21