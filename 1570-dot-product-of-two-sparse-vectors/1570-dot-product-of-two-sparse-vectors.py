class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = defaultdict(int)
        for i, x in enumerate(nums):
            if x:
                self.d[i] = x

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for k in self.d:
            if vec.d[k]:
                ans += self.d[k]*vec.d[k]
            
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)