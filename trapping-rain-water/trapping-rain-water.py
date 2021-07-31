class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right = [], []
        curr = 0
        ans = 0
        
        for x in height:
            curr = max(curr, x)
            left.append(curr)
        
        curr = 0
        for x in height[::-1]:
            curr = max(curr, x)
            right.append(curr)
            
        right.reverse()
        
        for i in range(N):
            tmp = min(left[i], right[i]) - height[i]
            if tmp > 0:
                ans += tmp
                
        return ans