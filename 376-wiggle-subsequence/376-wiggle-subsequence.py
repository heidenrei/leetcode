class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        nums = [x for i, x in enumerate(nums) if (i == 0 or nums[i-1] != x)]
        N = len(nums)
        #print(nums)
        if N == 1:
            return 1
        peaks = 0
        valleys = 0
        
        for i in range(1, N-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                peaks += 1
                
            if nums[i-1] > nums[i] < nums[i+1]:
                valleys += 1
                
        peaks += nums[0] > nums[1]
        peaks += nums[-1] > nums[-2]
        
        valleys += nums[0] < nums[1]
        valleys += nums[-1] < nums[-2]
        
        return peaks + valleys if peaks + valleys else 1