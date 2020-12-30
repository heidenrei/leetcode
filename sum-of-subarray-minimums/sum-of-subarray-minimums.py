class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = 10**9+7
        ans = []
        stack = []
        
        # stack[i] = [index, val]
        # mono increasing
        
        for i in range(N):
            while stack and stack[-1][1] >= arr[i]:
                stack.pop()
            if stack:
                j = stack[-1][0]
                ans.append(ans[j]+arr[i]*(i-j))
            else:
                ans.append(arr[i]*(i+1))
            stack.append([i, arr[i]])
        
        return sum(ans) % MOD
