class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return round(math.log(n, 3), 9) % 1 == 0 if n > 0 else False