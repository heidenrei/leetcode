class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        ans = 1
        N = len(s)
        #s = [ord(x) - ord('a') for x in s if x.islower() else ord(x) - ord('A') + 26]

        dp = [defaultdict(int) for _ in range(N+1)]
        dp[0][s[0]] += 1
        for i in range(1, N+1):
            for j in dp[i-1].keys():
                dp[i][j] = dp[i-1][j]
            dp[i][s[i-1]] += 1
        
        def is_good(i, m):
            cnt = 0
            for j in dp[m].keys():
                cnt += (dp[m][j] > dp[i-1][j])
                if cnt > k:
                    return False
            return True
        #print(is_good(1, 2))
        for i in range(1, N):
            l, r = i, N
            while l < r:
                m = l + (r-l+1)//2
                if is_good(i, m):
                    l = m
                else: 
                    r = m - 1
            tmp = l - i + 1
            if tmp > ans:
                ans = tmp
        return ans
            
            
                