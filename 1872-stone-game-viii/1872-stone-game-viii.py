class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        N = len(stones)
        s = sum(stones)
        best = s
        for i in range(N-2, 0, -1):
            s -= stones[i+1]
            best = max(best, s-best)
        return best