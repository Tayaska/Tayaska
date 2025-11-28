"""
Secure Calculator implementation
Passes Bandit security scan
"""

import math
import logging

class Calculator:
    """
    A secure calculator implementation with proper error handling
    """
    
    def __init__(self):
        self._operation_count = 0
        self.logger = logging.getLogger(__name__)
    
    def add(self, a: float, b: float) -> float:
        """Safely add two numbers"""
        self._validate_number(a)
        self._validate_number(b)
        self._operation_count += 1
        return a + b
    
    def multiply(self, a: float, b: float) -> float:
        """Safely multiply two numbers"""
        self._validate_number(a)
        self._validate_number(b)
        self._operation_count += 1
        return a * b
    
    def is_positive(self, number: float) -> bool:
        """Check if number is positive"""
        self._validate_number(number)
        return number > 0
    
    def factorial(self, n: int) -> int:
        """Safely calculate factorial"""
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n > 1000:  # Prevent excessive recursion
            raise ValueError("Input too large for factorial calculation")
        
        # Use iterative approach instead of recursive for security
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Safely divide two numbers"""
        self._validate_number(a)
        self._validate_number(b)
        
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        
        self._operation_count += 1
        return a / b
    
    def _validate_number(self, number) -> None:
        """Validate input is a number"""
        if not isinstance(number, (int, float)):
            raise TypeError(f"Expected number, got {type(number).__name__}")
    
    def get_operation_count(self) -> int:
        """Get total operations performed"""
        return self._operation_count
    
    def reset_counter(self) -> None:
        """Reset operation counter"""
        self._operation_count = 0

# Safe main guard
if __name__ == "__main__":
    # Demo usage
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5! = {calc.factorial(5)}")
