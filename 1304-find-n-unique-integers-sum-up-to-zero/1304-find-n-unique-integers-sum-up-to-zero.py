class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n & 1:
            ans = [0]
            n -= 1
        else:
            ans = []
        for x in range(1, n//2+1):
            ans.extend([x, -x])
        return ans
        