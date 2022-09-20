class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [str(x) for x in nums1]
        nums2 = [str(x) for x in nums2]
        
        
        def is_good(length):
            hashes = []
            tmp = []
            for i in range(len(nums1)-length):
                tmp.append(' '.join(nums1[i:i+length+1]))
            hashes.append(tmp)
            tmp = []
            for i in range(len(nums2)-length):
                tmp.append(' '.join(nums2[i:i+length+1]))
            hashes.append(tmp)
            
            return set(hashes[0]) & set(hashes[1])
        
        l = 0
        r = len(min([nums2, nums1], key=len))
        
        while l < r:
            m = l + r >> 1
            if is_good(m):
                l = m + 1
            else:
                 r = m
                    
        return l