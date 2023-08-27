class Solution:
    def canCross(self, stones: List[int]) -> bool:
        k = stones[-1]
        stones = set(stones)
        if 1 not in stones:
            return False
        @cache
        def go(x, jump):
            #print(x, jump)
            if x == k:
                return True
            if x > k:
                return False
            ans = False
            if x + jump in stones and go(x+jump, jump):
                ans = True
            if x + jump + 1 in stones and go(x+jump+1, jump+1):
                ans = True
            if jump - 1 > 0 and x + jump - 1 in stones and go(x+jump-1, jump-1):
                ans = True
            return ans
        
        return go(1, 1)