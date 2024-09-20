import math

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed"
    
    def square(self):
        return self.num1 ** 2
    
    def cube(self):
        return self.num1 ** 3
    
    def sqrtroot(self):
        if self.num1 >= 0:
            return math.sqrt(self.num1)
        else:
            return "can not calculate the sqaure root\
            a negative number"
    
    def __str__(self):
        return (f"Results:\n"
                f"Addition: {self.add()}\n"
                f"Subtraction: {self.subtract()}\n"
                f"Multiplication: {self.multiply()}\n"
                f"Division: {self.divide()}\n"
                f"Square: {self.square()}\n"
                f"Cube: {self.cube()}\n"
                f"Square Root: {self.sqrtroot()}")
        
calc = Calculator(-16, 10)
print(calc)