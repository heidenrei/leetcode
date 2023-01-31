class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        ans = 0
        for x in piles:
            ans ^= x
        return ans > 0