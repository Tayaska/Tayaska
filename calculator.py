"""
Secure Calculator implementation
Passes Bandit security scan
"""

import math
import logging

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def is_positive(self, number):
        return number > 0
    
    def factorial(self, n):
        if n <= 1:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    # Додаємо відсутні методи
    def divide(self, a, b):
        """Divide two numbers with zero division check"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    def process_list(self, data):
        """Process list of strings - basic implementation"""
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        return "".join(str(item) for item in data)

# Safe main guard
if __name__ == "__main__":
    # Demo usage
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5! = {calc.factorial(5)}")
