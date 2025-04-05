class Arith:
    def read(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        return "Division by zero error"
    
arith = Arith()
arith.read()
print("Sum: ", arith.add())
print("Difference: ", arith.subtract())
print("Product: ", arith.multiply())
print("Division: ", arith.divide())
