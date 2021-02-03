class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        nums.sort()
        
        def get_pro(i, j, k):
            return nums[i] * nums[j] * nums[k]
        
        zero = get_pro(N-1, N-2, N-3)
        
        two = get_pro(0,1, N-1)
        
                # need the highest neg number and lowest two pos numbers
        if zero < 0 and two < 0 and 0 in nums:
            return 0
        
        if nums[-1] < 0:
            return nums[-1] * nums[-2] * nums[-3]
        
        
        maxi = 0
        mini = N-1
        for i in range(N):
            if nums[maxi] < nums[i] < 0:
                maxi = i
            
            if 0 < nums[i] < nums[mini]:
                mini = i
        
        one = get_pro(maxi-1, maxi, mini)
        
        print(zero, one, two)
        
        return max(zero, one, two)