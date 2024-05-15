class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        N = len(target)
        for i in range(1, N):
            ans += max(0, target[i] - target[i-1])
        return ans + target[0]