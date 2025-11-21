# Python file to define a Circle class

# Import the required module(s)
import math # Allows us to access the inbuilt value of pi and pow() function

class Circle:
    """
    A class to represent a geometric circle.

    Attributes:
    -----------
    radius (float): the radius of the circle in cm.

    Methods:
    -------
    calc_area():
        calculates & returns the area of the circle.

    calc_perimeter():
        calculates & returns the perimeter of the circle.

    __str__():
        Returns a formatted string representing the circle's dimensions.
    """
    def __init__(self, radius = 0):
        """
        Initialise the Circle with a given radius.

        Parameters:
        ----------
        radius : float, default 0
            the radius of the circle in units (e.g. metres, cm , feet or inches).
        """
        self.radius = radius

    def calc_area(self):
        """
        Calculates the area of the circle.

        Returns:
        --------
        float
            the area of the circle using the formula π * r².
        """
        # return math.pi * self.radius ** 2 # Same as below code
        return math.pi * math.pow(self.radius, 2)

    def calc_perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
        --------
        float
            the perimeter of the circle using the formula π * (2 * r).
        """
        return math.pi * (2 * self.radius)

    def __str__(self): # dunder method works like toString() in Java or ToString() in C#
        """
        Returns a formatted string representing the circle's dimensions.

        Returns:
        -------
        str
            A readable summary of the radius, area and circumference of the circle.
        """
        return (f"Circle's dimensions"
                f"\n"  + "-" * 40 +
                f"\nRadius: {self.radius} cm."
                f"\nArea: {self.calc_area():.2f} cm^2."
                f"\nPerimeter: {self.calc_perimeter():.2f} cm."
                f"\n"  + "-" * 40 )

# print(f"The documentation string of the calc_area() method is:\n{Circle().calc_area.__doc__}")