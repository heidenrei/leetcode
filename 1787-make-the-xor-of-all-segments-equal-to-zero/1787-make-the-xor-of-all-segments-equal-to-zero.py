class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if k == 1:
            return N - nums.count(0)
        maxi = max(nums)
        #d = [[0 for x in range(maxi+1)] for x in range(k)]
        d = [defaultdict(int) for x in range(k)]
        for i in range(N):
            d[i%k][nums[i]] += 1
                
#         @cache
#         def go(i, b):
#             if i == k:
#                 return 0 if b == 0 else inf
#             ans = inf
#             for j in range(maxi+1):
#                 tmp = go(i+1, b^j) + (N//k) - d[i][j] + (N%k>i)
#                 if tmp < ans:
#                     ans = tmp
                
#             return ans
        #return go(0, 0)
        n = 2**10
        dp = [0] + [-inf]*(n-1)
        for i in range(k):
            mx = max(dp)
            tmp = [mx]*n
            for x, c in enumerate(dp):
                # for j in range(maxi+1):
                #     if d[i][j]:
                for xx, cc in d[i].items():
                        # cc = d[i][j]
                        # xx = j
                        #tmp[x^xx] = max(tmp[x^xx], c + cc, mx)
                        if tmp[x^xx] < c + cc:# > mx:
                            tmp[x^xx] = c + cc
                        # elif tmp[x^xx] < mx > c + cc:
                        #     tmp[x^xx] = mx
            dp = tmp
                
        return len(nums) - dp[0]
        