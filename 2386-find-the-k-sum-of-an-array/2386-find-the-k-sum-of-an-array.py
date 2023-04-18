from sortedcontainers import SortedList

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = sum([x for x in nums if x > 0])
        cnt = 1
        av = sorted([abs(x) for x in nums])
        sl = SortedList([[ans - av[0], 0]])
        while cnt < k:
            ans, i = sl.pop()
            cnt += 1
            if i+1 < N:
                sl.add([ans + av[i] - av[i+1], i+1])
                sl.add([ans - av[i+1], i+1])
        #print(ans)
        return ans