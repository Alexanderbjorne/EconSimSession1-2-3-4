from color_point import ColorPoint

class AdvancedPoint(ColorPoint):  # This makes AdvancedPoint inherit everything from ColorPoint
    COLORS = ["red", "green", "blue", "black", "white"]

    def __init__(self, x, y, color):
        # This makes sure x and y are numbers
        if not isinstance(x,(int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y,(int, float)):
            raise TypeError("y must be a number")
        # This checks that the color is one of the allowed options
        if not color in self.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        # This sets the values manually (without calling the parent init)
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        # This makes sure we only set valid colors
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        # This lets us add more colors to the class list
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        # This can calculate the distance between two points
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)**0.5

    @staticmethod
    def from_dictionary(dict):
        # This makes it possible to create a point from a dictionary
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x, y, color)

# This uses the dictionary method with default values
p4 = AdvancedPoint.from_dictionary({})
print(p4)

# Creating a point the normal way
p2 = AdvancedPoint(1, 2, "red")

# Adding a new allowed color
AdvancedPoint.add_color("amber")

# Creating another point using the new color
p3 = AdvancedPoint(-1, -2, "amber")

# Printing the distance between two points
print(AdvancedPoint.distance_2_points(p3, p2))
