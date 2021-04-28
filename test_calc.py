from .calc import Calculator


def test_sum():
    calc = Calculator()
    result = calc.sum(3,7)
    assert result == 10
