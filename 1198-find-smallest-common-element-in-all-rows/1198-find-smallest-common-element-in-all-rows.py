class Solution:
    def smallestCommonElement(self, A):
        c = Counter()
        R, C = len(A), len(A[0])
        for i in range(R):
            for j in range(C):
                c[A[i][j]] += 1
                
        maxi = max(c.values())
        ans = inf
        for k, v in c.items():
            if v == R:
                ans = min(ans, k)
        return ans if ans < inf else -1
        