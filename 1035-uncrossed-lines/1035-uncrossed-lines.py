class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        @cache
        def go(i, j):
            if i == N or j == M:
                return 0
            if nums1[i] == nums2[j]:
                ans = go(i+1, j+1) + 1
            else:
                ans = go(i+1, j+1)
            return max(ans, go(i+1, j), go(i, j+1))
        return go(0, 0)