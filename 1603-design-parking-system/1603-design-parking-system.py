class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.med = medium
        self.small = small

    def addCar(self, cartype: int) -> bool:
        if cartype == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif cartype == 2:
            if self.med > 0:
                self.med -= 1
                return True
            else:
                return False
        elif cartype == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False