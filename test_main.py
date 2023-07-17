# test_app.py
from calc import Calc


def test_add():
    calc = Calc()
    result = calc.add(2, 3)
    assert result == 5


def test_sub():
    calc = Calc()
    result = calc.sub(5, 2)
    assert result == 3


def test_mult():
    calc = Calc()
    result = calc.mult(4, 2)
    assert result == 8


def test_div():
    calc = Calc()
    result = calc.div(10, 2)
    assert result == 5
