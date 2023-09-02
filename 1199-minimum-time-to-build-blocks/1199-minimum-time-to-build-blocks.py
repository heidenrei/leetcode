class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # try all powers of 2?
        N = len(blocks)
        blocks.sort(reverse=True)
        @cache
        def go(i, x):
            if i == N:
                return 0
            if x == 0:
                return inf
            ans = go(i+1, x-1)
            if blocks[i] > ans:
                ans = blocks[i]
            #ans = max(go(i+1, x-1), blocks[i])
            nx = x*2
            cnt = 1
            while nx <= N-i:
                tmp = go(i, nx) + split*cnt
                cnt += 1
                nx *= 2
                if tmp < ans:
                    ans = tmp
            return ans
            
        ans = go(0, 1)
        go.cache_clear()
        return ans
        
        