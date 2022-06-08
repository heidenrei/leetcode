class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        #print(nums1)
        for i in range(n+m):
            ti = i
            while ti > 0 and nums1[ti] < nums1[ti-1]:
                nums1[ti], nums1[ti-1] = nums1[ti-1], nums1[ti]
                ti -= 1
                
        