class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spotions = sorted(potions)
        N = len(potions)
        ans = []
        for x in spells:
            l, r = 0, N-1
            while l <= r:
                m = l + r >> 1
                if x*spotions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
            ans.append(N-r-1)
        return ans