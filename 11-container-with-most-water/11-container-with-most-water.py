from sortedcontainers import SortedList

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def f(height):
            nums = []
            best = 0
            for i, x in enumerate(height):
                nums.append([i, x])
            nums.sort(key=lambda x: (-x[1], x[0]))
            #print(nums)
            # what's the earliest height >= x
            # add them to sl by height (decreasing) and then by idx (increasing)
            sl = SortedList()
            for i, x in nums:
                #print(x)
                idx = sl.bisect_right(i)
                if idx > 0:
                    tmp = (i - sl[0])*x
                    if tmp > best:
                        best = tmp

                sl.add(i)

            return best
        
        return max(f(height), f(height[::-1]))