import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area:.2f}"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("Can only add two Circle instances")
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        raise TypeError("Comparison must be with another Circle")
    
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        raise TypeError("Comparison must be with another Circle")
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False
