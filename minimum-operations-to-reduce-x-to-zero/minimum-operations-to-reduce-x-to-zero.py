class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        A = list(accumulate(nums, initial=0))
        total = sum(nums)
        target = total - x
        
        best = -1
        seen = set([0])
        idx_lookup = {0: 0}
        for i, x in enumerate(A):
            curr = x - target
            if curr in seen:
                best = max(best, i - idx_lookup[curr])
            idx_lookup[x] = i
            seen.add(x)
        
        return N - best if best != -1 else -1
