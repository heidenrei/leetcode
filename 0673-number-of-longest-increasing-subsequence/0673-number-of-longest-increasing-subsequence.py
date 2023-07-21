class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1]*N
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        lis = []
        maxi = max(dp)
        for i in range(N):
            if dp[i] == maxi:
                lis.append(i)
        #print(dp)
        dp2 = [1]*N
        for i in range(1, N):
            c = Counter()
            c[1] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    c[dp[j] + 1] += dp2[j]
            dp2[i] = c[max(c.keys())]
        #print(dp2)
                    
        ans = 0
        for i in lis:
            ans += dp2[i]
        return ans