class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width

rect = Rectangle(5, 3)
print("Area of rectangle: ", rect.area())
