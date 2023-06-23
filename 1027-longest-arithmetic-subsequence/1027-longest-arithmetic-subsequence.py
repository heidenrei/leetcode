class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N = len(nums)
        idx = defaultdict(list)
        for i in range(N):
            idx[nums[i]].append(i)
        @cache
        def go(i, d):
            #print(i, d)
            ans = 0
            for j in idx[nums[i] + d]:
                if j > i:
                    tmp = go(j, d) + 1
                    if tmp > ans:
                        ans = tmp
                    break
            return ans
        ans = 0
        for i in range(N):
            for j in range(i):
                tmp = go(j, nums[i] - nums[j]) + 1
                if tmp > ans:
                    ans = tmp
        return ans