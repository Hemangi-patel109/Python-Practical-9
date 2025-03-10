# Write a python program to demonstrate overloading of add (+) operator

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type for +")

p1 = Point(2, 3)
p2 = Point(4, 5)

print("p1:", p1)
print("p2:", p2)

p3 = p1 + p2
print("p1 + p2:", p3)

p4 = p1 + 10
print("p1 + 10:", p4)