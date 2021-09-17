class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        c = c1 & c2
        
        ans = []
        
        for k, v in c.items():
            ans.extend([k]*v)
            
        return ans