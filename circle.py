import figure
import math

class Circle(figure.Figure):
    
    def __init__(self, color, x, y, r):
        super().__init__(color)
        self.x = x
        self.y = y
        self.r = r
    
    def get_area(self):
        return math.pi * self.r ** 2