# Bonus P2, P6, P9 - Combined

# P2 Extra
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
print("P2:", count_vowels("Programming"))

# P6 Extra
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

print("P6:", Square(5).area())

# P9 Extra
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __len__(self):
        return round(math.sqrt(self.x**2 + self.y**2))
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(1, 1)
print("P9:", p1 - p2, len(p1))