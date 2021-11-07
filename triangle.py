import figure

class Triangle(figure.Figure):
    
    def __init__(self, color, x1, y1, x2, y2, x3, y3):
        super().__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    
    def get_area(self):
        a = (abs(self.x1 - self.x2) ** 2 + abs(self.y1 - self.y2) ** 2) ** 0.5
        b = (abs(self.x3 - self.x2) ** 2 + abs(self.y3 - self.y2) ** 2) ** 0.5
        c = (abs(self.x1 - self.x3) ** 2 + abs(self.y1 - self.y3) ** 2) ** 0.5
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
if __name__ == '__main__':
    obj = Triangle('красный', 1, 1, 2, 2, 3, 3)
        
        