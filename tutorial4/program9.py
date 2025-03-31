class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def center(self):
        return (self.corner_x + self.width / 2, self.corner_y + self.height / 2)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

rect = Rectangle(10, 5, 0, 0)
print("Center:", rect.center())
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())