class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        nums1, nums2 = set(nums1), set(nums2)
        both = nums1 & nums2
        one = nums1 ^ both
        two = nums2 ^ both
        from_one = min(N//2, len(one))
        from_two = min(N//2, len(two))
        return min(from_one + from_two + len(both), N)