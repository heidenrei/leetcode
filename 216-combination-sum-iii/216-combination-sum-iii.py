class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = range(1, 10)
        ans = []
        for c in combinations(nums, k):
            if sum(c) == n:
                ans.append(c)
                    
        return ans