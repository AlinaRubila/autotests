class Calculator():
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by zero")
        return a / b
    def isPrime(self, a):
        if a <= 1:
            return False
        for d in range(2, int(a ** 0.5) + 1):
            if a % d == 0:
                return False
        return True