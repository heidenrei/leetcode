class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        @cache
        def go(i, j):
            if i == j:
                return 0
            
            turn = N - j - 1 + i
            
            if turn & 1:
                return min(go(i+1, j) - piles[i], go(i, j-1) - piles[j])
            else:
                return max(go(i+1, j) + piles[i], go(i, j-1) + piles[j])
            
        return go(0, N-1) > 0