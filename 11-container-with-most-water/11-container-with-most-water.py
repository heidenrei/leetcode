class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        best = 0
        i, j = 0, N-1
        while i < j:
            tmp = (j-i)*min(height[i], height[j])
            if tmp > best:
                best = tmp
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
        return best