class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = set()
        seen = set()
        
        @lru_cache(None)
        def go(curr, idx):
            curr = tuple(sorted(curr))
            if curr not in seen:
                ans.add(curr)
                seen.add(curr)
            for i in range(idx, N):
                curr = list(curr)
                curr.append(nums[i])
                go(tuple(curr), i+1)
                curr.pop()
                
        go(tuple(), 0)

        return ans