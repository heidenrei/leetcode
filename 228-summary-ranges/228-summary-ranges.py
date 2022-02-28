class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        nums.sort()
        low = nums[0]
        curr = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != curr + 1:
                if low != curr:
                    ans.append(str(low) + '->' + str(curr))
                else:
                    ans.append(str(curr))
                low = nums[i]
            curr = nums[i]
        
        
        if low != curr:
            ans.append(str(low) + '->' + str(curr))
        else:
            ans.append(str(curr)) 
        return ans