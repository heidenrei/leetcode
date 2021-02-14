class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] == 0:
                nums[i] = -1        
        
        A = list(accumulate(nums, initial=0))
        
        best = 0
        seen = {}
        
        for i in range(N+1):
            if A[i] in seen:
                if i - seen[A[i]] > best:
                    best = i - seen[A[i]]
            if A[i] not in seen:
                seen[A[i]] = i
        return best