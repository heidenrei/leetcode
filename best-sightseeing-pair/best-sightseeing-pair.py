class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        best = 0
        ans = 0
        for i in range(N):
            ans = max(ans, values[i] + best)
            if values[i] - 1 > best - 1:
                best = values[i] - 1
            else:
                best -= 1
                
        return ans
                
                
        