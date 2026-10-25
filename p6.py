class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
# methods
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

# Testing 

# First line test with r = Rectangle(4, 6)
r = Rectangle(4, 6)
print(r, r.area(), r.perimeter(), r.is_square())

# Second line Test with Rectangle(5, 5)
r2 = Rectangle(5, 5)
print(r2.is_square())