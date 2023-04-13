from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        sl = SortedList(nums[:k])
        ans = []
        if k & 1:
            ans.append(sl[k//2])
        else:
            ans.append((sl[k//2]+sl[k//2-1])/2)
        for i in range(k, len(nums)):
            sl.remove(nums[i-k])
            sl.add(nums[i])
            if k & 1:
                ans.append(sl[k//2])
            else:
                ans.append((sl[k//2]+sl[k//2-1])/2)
        return ans