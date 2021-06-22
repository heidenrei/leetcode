class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        A = [0 for x in range(5001)]
        
        for x in nums:
            A[x] += 1
            
        A = [[i, x] for i, x in enumerate(A) if x != 0]
        
        nn = []
        
        for x, y in A:
            nn.extend([x]*y)
        
        if len(nn) & 1:
            m = len(nn)//2+1
        else:
            m = len(nn)//2
        
        lows = nn[:m]
        his = nn[m:]
        
        for k in range(len(nums)):
            if k & 1:
                nums[k] = his.pop()
            else:
                nums[k] = lows.pop()
                
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         nums[:m], nums[m:] = nums[m:], nums[:m]
        #         break
                