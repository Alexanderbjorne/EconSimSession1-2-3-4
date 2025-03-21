from color_point import ColorPoint

class AdvancedPoint(ColorPoint): #This means that advanced point inherit everything from Colorpoint
    COLORS = ["red", "green", "blue", "black", "white"]
    def __init__(self, x, y, color):
      if not isinstance(x,(int, float)):
          raise TypeError("x must be a number")
      if not isinstance(y,(int, float)):
        raise TypeError("y must be a number")
      if not color in self.COLORS:
          raise ValueError(f"color must be one of: {self.COLORS}")
      # super().__init__(x, y, color) #Call the init method of the parent
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
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        cls.COLORS.append(new_color)

p = AdvancedPoint(1, 2, "red")
print(p)
print(p.distance_orig())

# p = AdvancedPoint("jon", "jeb", "blue")
# print(p)
# print(p.distance_orig())

AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(9, 3, "amber")
# print(p2)
# print(p2.distance_orig())
# print(p2.color)
# p2.color = "Bob"
# print(p2.color)

p2.color = "blue"

print(p2)
# print(p2.x)
# print(p2.y)
# print(p2.color)

