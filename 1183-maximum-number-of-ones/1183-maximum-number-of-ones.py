from sortedcontainers import SortedList

class Solution:
    def maximumNumberOfOnes(self, w, h, k, m):
        sl = SortedList()
        for i in range(k):
            for j in range(k):
                sl.add(((w - i - 1) // k + 1) * ((h - j - 1) // k + 1))
                if len(sl) > m:
                    sl.pop(0)
        ans = 0
        while sl:
            ans += sl[0]
            sl.pop(0)
        return ans