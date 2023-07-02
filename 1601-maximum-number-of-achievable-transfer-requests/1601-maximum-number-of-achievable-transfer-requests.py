class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        nums = [0]*n
        for x, y in requests:
            nums[x] += 1
        tbm = int('1010110', 2)
        for bm in range(2**len(requests)):
            tmp = [x for x in nums]
            for i in range(len(requests)):
                if bm & (1<<i):
                    tmp[requests[i][0]] -= 1
                    tmp[requests[i][1]] += 1
            if tmp == nums and bm.bit_count() > ans:
                ans = bm.bit_count()
        return ans