from basic_shape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, length, width):
        super().__init__()  # call parent constructor
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"
