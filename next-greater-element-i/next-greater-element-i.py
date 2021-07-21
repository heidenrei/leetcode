class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums1)
        ans = [-1]*N
        for i in range(N):
            to_right = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    to_right = True
                if to_right and nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans