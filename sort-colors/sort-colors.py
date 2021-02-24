class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # push all twos to the end
        # push all zeroes to the start
        
        N = len(nums)
        zeroes = 0
        ones = 0
        twos = 0
        
        for i in range(N):
            if nums[i] == 0:
                zeroes += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1
                
        nums[:zeroes] = [0]*zeroes
        nums[zeroes:zeroes+ones] = [1]*ones
        nums[zeroes+ones:zeroes+ones+twos] = [2]*twos
        
        
        
                