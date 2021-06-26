from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        nums.reverse()
        sl = SortedList()
        
        for i in range(N):
            ans.append(sl.bisect_left(nums[i]))
            sl.add(nums[i])
            
        return ans[::-1]