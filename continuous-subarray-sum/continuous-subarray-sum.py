class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        seen = set()
        curr = 0
        step = 0
        for x in nums:
            curr = (curr+x) % k
            if curr in seen:
                return True
            seen.add(step)
            step = curr
            
        return False
        