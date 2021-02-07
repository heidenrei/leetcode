class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        c = Counter(nums)
        ans = ['x']*2
        for i in range(1, N+1):
            if not c[i]:
                ans[1] = i
            elif c[i] == 2:
                ans[0] = i
                
        return ans