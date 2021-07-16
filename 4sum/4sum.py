class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        ans = []
        for i in range(N):
            for j in range(i):
                seen = set()
                for k in range(j):
                    if target - nums[i] - nums[j] - nums[k] in seen:
                        ans.append([target - nums[i] - nums[j] - nums[k], nums[k], nums[j], nums[i]])
                    seen.add(nums[k])
        
        ans = set([tuple(sorted(x)) for x in ans])
        return list(ans)