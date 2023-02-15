class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        @cache
        def go(x, y):
            if x < sx or y < sy:
                return False
            if x == sx:
                return sy % x == y % x
            if y == sy:
                return sx % y == x % y
            if x > y:
                if (x%y)+y < x and go((x%y)+y, y):
                    return True
                return go(x%y, y)
            else:
                if (y%x)+x < y and go(x, ((y%x)+x)):
                    return True
                return go(x, y%x)
            
        return go(tx, ty)