class Solution:
    def findMaxForm(self, nums: List[str], m: int, n: int) -> int:
        N = len(nums)
        nums = [[x for x in nums[i]] for i in range(N)]
        @cache
        def go(i, m, n):
            if i == N:
                return 0
            cnt0, cnt1 = nums[i].count('0'), nums[i].count('1')
            if m - cnt0 >= 0 and n - cnt1 >= 0:
                pick = go(i+1, m - cnt0, n - cnt1) + 1
            else:
                pick = -inf
            pss = go(i+1, m, n)
            
            return max(pick, pss)
        
        return go(0, m, n)