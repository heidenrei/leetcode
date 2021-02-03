import bisect

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        ans = []
        
        for k, v in c.items():
            ans.append([k, v])
            
        ans.sort()
        
        best = 0
        
        for i in range(1, len(ans)):
            if ans[i][0] == ans[i-1][0] + 1:
                best = max(best, ans[i][1] + ans[i-1][1])
                
        return best