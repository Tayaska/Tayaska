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
        return n * self.factorial(n - 1)
    
    # 🐛 Навмисні помилки для тестування AI
    def divide(self, a, b):
        return a / b  # Ділення на 0 не оброблено
    
    def process_list(self, data):
        result = ""
        for item in data:
            result += item.upper()  # Можливий AttributeError
        return result
