class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        stack = deque()
        
        for idx, x in enumerate(nums):
            if idx >= k:
                if stack[0] is nums[idx - k]:
                    stack.popleft()
                    
            while stack and stack[-1] < x:
                stack.pop()
                
            stack.append(x)
            
            if idx >= k - 1:
                ans.append(stack[0])
                
        return ans