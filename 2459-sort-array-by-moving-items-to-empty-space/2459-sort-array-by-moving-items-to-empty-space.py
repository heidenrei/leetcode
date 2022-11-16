class Solution:
    def sortArray(self, nums: List[int]) -> int:
        N = len(nums)
        def get_ans(nums, t):
            def go(x):
                if nums[x] != x and nums[x] not in tmp:
                    tmp.add(nums[x])
                    go(nums[x])

            cycles = []
            seen = set()
            for i in range(N):
                if i not in seen:
                    tmp = set([i, nums[i]])
                    go(nums[i])
                    cycles.append(tmp)
                    seen |= tmp

            ans = 0
            for c in cycles:
                if len(c) > 1:
                    if t == 0:
                        if 0 in c:
                            ans += len(c) - 1
                        else:
                            ans += len(c) + 1
                    else:
                        if N-1 in c:
                            ans += len(c) - 1
                        else:
                            ans += len(c) + 1
                    
            return ans
        zero = get_ans(nums, 0)
        tmp_nums = []
        for x in nums:
            if x:
                tmp_nums.append(x-1)
            else:
                tmp_nums.append(N-1)
        one = get_ans(tmp_nums, 1)
        return min(one, zero)