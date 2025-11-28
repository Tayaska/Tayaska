import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_is_positive():
    calc = Calculator()
    assert calc.is_positive(5) == True
    assert calc.is_positive(-5) == False

def test_factorial():
    calc = Calculator()
    assert calc.factorial(5) == 120

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_process_list():
    calc = Calculator()
    assert calc.process_list(["a", "b"]) == "ab"
