import random
from ftplib import parse227  # not used in this script, can probably be removed

class Point:
    """
    Class modeling a real life 2D point
    """
    def __init__(self, x, y):
        # This sets up the point with x and y coordinates
        self.x = x
        self.y = y

    def __str__(self):
        # Makes it print like: <x, y>
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        # Reuse the same string format for printing in lists, etc.
        return self.__str__()

    def distance_orig(self):
        # Calculates the distance from the origin (0,0)
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        # This allows us to compare points based on distance to origin
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        # Checks if two points are the same distance from origin
        return self.distance_orig() == other.distance_orig()

if __name__ == "__main__":
    points = []
    for i in range(5):
        # Create random points and add to list
        p = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        points.append(p)

    print("unsorted points")
    print(points)

    print("sorted points")
    # Sorts based on distance to origin because of __gt__
    points.sort()
    print(points)

    found_equal = 0
    count = 0
    while True:
        if found_equal == 10000:
            break
        # Create two random points and check if they are equal in distance
        p1 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        p2 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        count += 1
        if p1 == p2:
            found_equal += 1

    # Prints the estimated probability of generating two equal-distance points
    print(f"probability is 1 in {count/found_equal} ")
