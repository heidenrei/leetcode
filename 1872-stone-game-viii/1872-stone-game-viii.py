class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        N = len(stones)
        s = sum(stones)
        best = s
        for i in range(N-1, 1, -1):
            s -= stones[i]
            best = max(best, s-best)
        return best