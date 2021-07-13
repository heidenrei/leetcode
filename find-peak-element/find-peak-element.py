class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        
        l = 0
        r = N - 1
        
        while l <= r:
            m = l + r >> 1
            greater_than_left = False
            greater_than_right = False
            if m == 0 or nums[m] > nums[m-1]:
                greater_than_left = True
                
            if m == N-1 or nums[m] > nums[m+1]:
                greater_than_right = True
                
            if greater_than_left & greater_than_right:
                return m
            
            elif greater_than_left and not greater_than_right:
                l = m + 1
            else:
                r = m  