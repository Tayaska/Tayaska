import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))

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
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            self.calc.factorial(-5)
    
    def test_invalid_types_add(self):
        with pytest.raises(TypeError):
            self.calc.add("2", 3)
    
    def test_process_list_invalid_input(self):
        with pytest.raises(TypeError):
            self.calc.process_list("not_a_list")
    
    # Performance tests
    def test_factorial_performance(self):
        import time
        start_time = time.time()
        result = self.calc.factorial(100)
        end_time = time.time()
        assert (end_time - start_time) < 1.0  # Should complete in under 1 second
    
    # Edge cases
    def test_divide_edge_cases(self):
        assert self.calc.divide(0, 5) == 0.0
        assert self.calc.divide(5, 2) == 2.5
    
    def test_process_list_edge_cases(self):
        assert self.calc.process_list([]) == ""
        assert self.calc.process_list(["a", "b"]) == "AB"

# Integration tests
class TestCalculatorIntegration:
    def test_combined_operations(self):
        calc = Calculator()
        result = calc.add(calc.multiply(2, 3), calc.divide(10, 2))
        assert result == 11
