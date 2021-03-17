from random import uniform

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.min_x = x_center - radius
        self.max_x = x_center + radius
        self.min_y = y_center - radius
        self.max_y = y_center + radius
        
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def randPoint(self) -> List[float]:
        while 1:
            random_x = uniform(self.min_x, self.max_x)
            random_y = uniform(self.min_y, self.max_y)
            if math.sqrt((random_x - self.x_center)**2 + (random_y - self.y_center)**2) <= self.radius:
                return [random_x, random_y]