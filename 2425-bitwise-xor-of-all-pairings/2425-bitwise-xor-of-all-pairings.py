class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for x in nums1:
            if len(nums2) & 1:
                ans ^= x
        for x in nums2:
            if len(nums1) & 1:
                ans ^= x
        return ans