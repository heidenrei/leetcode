class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = 0
        s = 0
        for x in nums:
            s += x
            ans |= x
            ans |= s
            
        return ans
            