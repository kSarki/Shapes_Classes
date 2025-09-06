from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        # Call Rectangle constructor with length = width = side
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square with side {self.side}"
