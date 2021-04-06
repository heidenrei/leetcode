class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        d = defaultdict(list)
        ans = set()
        for i in range(N):
            if nums[i] in d:
                for k, j, oi in d[nums[i]]:
                    ans.add(tuple([nums[k], nums[j], nums[oi], nums[i]]))

            for j in range(i):
                for k in range(j):
                    d[target - nums[i] - nums[j] - nums[k]].append([k, j, i])
        
        ans = [list(x) for x in ans]
        ans = list(set([tuple(sorted(x)) for x in ans]))
        return ans