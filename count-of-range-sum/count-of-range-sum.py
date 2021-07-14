from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        sl.add(0)
        curr = 0
        ans = 0
        for x in nums:
            curr += x

            plus = sl.bisect_right(curr-lower)
            minus = sl.bisect_left(curr-upper)
            ans += plus
            ans -= minus
            sl.add(curr)

            
        return ans

        