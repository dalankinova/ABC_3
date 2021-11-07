class Figure:
    
    def __init__(self, color):
        self.color = color
    
    def get_area(self):
        return 0
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.color}, {self.get_area()})'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.get_area()})'