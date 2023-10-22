from sortedcontainers import SortedList

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        sl = SortedList()
        n = len(nums)
        tmp = [[x, i] for i, x in enumerate(nums)]
        tmp.sort()
        ans = 0
        while tmp:
            x, i = tmp.pop()
            idx = sl.bisect([i, i])
            tl, tr = i, i
            if idx > 0 and sl[idx-1][-1] == i - 1:
                tl, _ = sl.pop(idx-1)
            idx = sl.bisect([i, i])
            if idx < len(sl) and sl[idx][0] == i + 1:
                _, tr = sl.pop(idx)
            if (tr - tl + 1)*x > ans and tl <= k <= tr:
                ans = (tr - tl + 1)*x
                #print(x, tr, tl)
            sl.add([tl, tr])
            #print(x, sl)
        return ans