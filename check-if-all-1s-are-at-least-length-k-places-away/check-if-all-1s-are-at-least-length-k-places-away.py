class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        cnt = 0
        
        if 1 not in nums:
            return True
        
        for i in range(nums.index(1)+1, N):
            if nums[i] == 1:
                if cnt >= k:
                    cnt = 0
                else:
                    return False
            else:
                cnt += 1
                
        return True
