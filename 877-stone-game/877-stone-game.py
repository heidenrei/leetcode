class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        @cache
        def go(i, j, t): #[)
            if i == j:
                return 0
            if t:
                return max(go(i+1, j, 1-t) + piles[i], go(i, j-1, 1-t) + piles[j])
            else:
                return min(go(i+1, j, 1-t) - piles[i], go(i, j-1, 1-t) - piles[j])
            
        return go(0, N-1, 1) > 0