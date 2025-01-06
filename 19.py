from math import pi


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        print(self.width * self.length)

    def perimeter(self):
        print((self.width + self.length) * 2)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print((self.radius ** 2) * pi)

    def perimeter(self):
        print(self.radius * 2 * pi)


# polymorphic methods
def show_area(shape):
    shape.area()


def show_perimeter(shape):
    shape.perimeter()


shape1 = Circle(4)
shape2 = Rectangle(5, 6)
show_area(shape2)
show_perimeter(shape2)
