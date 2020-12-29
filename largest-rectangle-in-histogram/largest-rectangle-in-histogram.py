class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # n <= 2*10**4
        
        if not heights:
            return 0
        
        heights.append(0)
        heights = [0] + heights
        N = len(heights)
        best = max(heights)
        
        stack = [[heights[0], 0]]
        for i in range(1, N):
            if heights[i] < stack[-1][0]:
                h = stack[-1][0]
                w = i-stack[-1][1]
                best = max(best, w*h)
                
                while stack and heights[i] < stack[-1][0]:
                        h = stack[-1][0]
                        w = i-stack[-1][1]
                        best = max(best, w*h)
                        tmp = stack.pop()
                
                if stack:
                    if stack[-1][0] != heights[i]:
                        stack.append([heights[i], tmp[1]])
                else:
                    stack.append([heights[i], i])
                
            
            elif heights[i] > stack[-1][0]:
                stack.append([heights[i], i])
                
        return best
