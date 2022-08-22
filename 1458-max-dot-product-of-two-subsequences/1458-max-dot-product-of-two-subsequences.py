class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        @cache
        def go(i, j):
            if i == N or j == M:
                return 0
            pick_both = nums1[i] * nums2[j] + go(i+1, j+1)
            pick_i = go(i+1, j)
            pick_j = go(i, j+1)
            return max(pick_both, pick_j, pick_i)
        
        best = -inf
        for i in range(N):
            for j in range(M):
                tmp = go(i+1, j+1) + nums1[i] * nums2[j]
                if tmp > best:
                    best = tmp
                    
        return best