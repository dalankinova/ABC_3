import figure

class Rectangle(figure.Figure):
    
    def __init__(self, color, x1, y1, x2, y2):
        super().__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def get_area(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)