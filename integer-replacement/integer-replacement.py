class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def go(num):
            if num == 1:
                return 0
            if num & 1:
                go_down = go(num-1) + 1
                go_up = go(num+1) + 1
                return min(go_up, go_down)
            else:
                return go(num>>1) + 1
            
        return go(n)
                