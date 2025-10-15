import pytest

from calculator import Calculator


@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3),
    (-1, 8, 7),
    (-2, 6, 4),
    (-4, -1, -5)
])
def test_addition(a, b, result):
    calc = Calculator()
    r = calc.add(a, b)
    assert r == result

@pytest.mark.parametrize("a, b, result", [
    (4, 1, 3),
    (1, 4, -3),
    (-23, 1, -24),
    (23, -1, 24),
    (-10, -3, -7)
])
def test_subtract(a, b, result):
    calc = Calculator()
    r = calc.subtract(a, b)
    assert r == result

@pytest.mark.parametrize("a, b, result", [
    (4, 2, 8),
    (-3, 2, -6),
    (3, -2, -6),
    (-5, -2, 10)
])
def test_multiply(a, b, result):
    calc = Calculator()
    r = calc.multiply(a, b)
    assert r == result

@pytest.mark.parametrize("a, b, result", [
    (4, 2, 2),
    (-10, 2, -5),
    (6, -3, -2),
    (-8, -2, 4)
])
def test_divide(a, b, result):
    calc = Calculator()
    r = calc.divide(a, b)
    assert r == result

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Can't divide by zero"):
        calc.divide(10, 0)

@pytest.mark.parametrize("a, result", [
    (0, False),
    (1, False),
    (-3, False),
    (2, True),
    (10, False),
    (5, True)
])
def test_prime(a, result):
    calc = Calculator()
    r = calc.isPrime(a)
    assert r == result