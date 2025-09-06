from circle import Circle
from rectangle import Rectangle
from square import Square

def main():
    # Create shapes
    shapes = [
        Rectangle(4, 5),
        Rectangle(2, 6),
        Circle(3),
        Circle(5),
        Square(4)
    ]

    # Display each shape's name and area/perimeter
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print()  # Add blank line between shapes

if __name__ == "__main__":
    main()
