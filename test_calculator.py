import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    # Positive test cases
    def test_add_positive(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_multiply_positive(self):
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
    
    def test_is_positive_positive(self):
        assert self.calc.is_positive(5) == True
        assert self.calc.is_positive(0) == False
        assert self.calc.is_positive(-5) == False
    
    def test_factorial_positive(self):
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
    
    # Negative test cases - error handling
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
    
    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            self.calc.factorial(-5)
    
    # Simple tests without complex error handling
    def test_divide_normal(self):
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(5, 2) == 2.5

# Прості тести без класу
def test_basic_functionality():
    calc = Calculator()
    assert calc.add(2, 2) == 4
    assert calc.multiply(3, 4) == 12
    assert calc.factorial(3) == 6
