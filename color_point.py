from point import Point  # This imports the base Point class from another file
import random

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        This sets up a point with a position (x, y) and a color
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        # This makes the object print nicely like: <x, y>(color)
        return f"<{self.x},{self.y}>({self.color})"

# Example usage below (commented out)

# color_points = []  # This would store a list of random ColorPoint objects
# colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
# for _ in range(5):
#     # This creates 5 random ColorPoints
#     p = ColorPoint(
#         random.randint(-100, 100),
#         random.randint(-100, 100),
#         random.choice(colors))
#     color_points.append(p)

# print("random color points:")
# print(color_points)

# color_points.sort()  # This only works if Point has a comparison method like __lt__
# print("color points in order:")
# print(color_points)
