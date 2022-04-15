
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return (self.a + self.b)
    def subtract(self):
        return (self.a - self.b)
    def multiply(self):
        return (self.a * self.b)
    def divide(self):
        return (self.a / self.b)
demo1 = Calculator(20, 10)
print("Addition:", demo1.add())
print("Subtraction:", demo1.subtract())
print("Mutliplication:", demo1.multiply())
print("Division:", demo1.divide())



