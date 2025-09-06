import math
from basic_shape import BasicShape

class Circle(BasicShape):
    def __init__(self, radius):
        super().__init__()  # call the parent constructor
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"
