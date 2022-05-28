class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
            
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = 0
        # s1 < s2
        seen = set()
        seen.add((s1, s2))
        while s1 < s2:
            for x in range(1, 6): # never increase 6...
                if c1[x]:
                    c1[x] -= 1
                    s1 += 6-x
                    ans += 1
                    break
                elif c2[7-x]:
                    c2[7-x] -= 1
                    s2 -= 7-x-1
                    ans += 1
                    break
            if (s1, s2) in seen:
                return -1
            else:
                seen.add((s1, s2))
        #print(s1, s2)
        return ans
                    
        