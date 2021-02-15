class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if any([i == z for i in [x, y]]) or z == 0:
            return True
        if any([i == 0 for i in [x, y]]) or x + y < z:
            return False
        return z % math.gcd(x, y) == 0