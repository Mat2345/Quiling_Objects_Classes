import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Compute and print the area of the circle."""
        area = math.pi * self.radius**2
        print(f"The area of the circle with radius {self.radius} is: {area:.2f}")

    def perimeter(self):
        """Compute and print the perimeter of the circle."""
        perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle with radius {self.radius} is: {perimeter:.2f}")

# Example usage:
radius_value = float(input("Enter the circle's radius: "))
the_circle = Circle(radius_value)

the_circle.area()
the_circle.perimeter()

