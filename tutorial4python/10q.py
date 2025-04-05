class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def display(self):
        print(f"{self.real} + {self.imag}i")

complex1 = Complex(3, 4)
complex2 = Complex(1, 2)
result = complex1 + complex2
result.display()
