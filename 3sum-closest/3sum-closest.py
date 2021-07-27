from sortedcontainers import SortedList

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        best = math.inf
        best_sum = -1
        
        sl = SortedList(nums[1:])
        
        for i in range(1, N):
            sl.remove(nums[i])
            for j in range(i):
                idx = sl.bisect(target - nums[i] - nums[j])
                if idx > 0:
                    if abs(target - (sl[idx-1] + nums[i] + nums[j])) < best:
                        best = abs(target - (sl[idx-1] + nums[i] + nums[j]))
                        best_sum = sl[idx-1] + nums[i] + nums[j]
                
                if idx < len(sl) - 1:
                    if abs(target - (sl[idx+1] + nums[i] + nums[j])) < best:
                        best = abs(target - (sl[idx+1] + nums[i] + nums[j]))
                        best_sum = sl[idx+1] + nums[i] + nums[j]
                
                if idx < len(sl) and abs(target - (sl[idx] + nums[i] + nums[j])) < best:
                    best = abs(target - (sl[idx] + nums[i] + nums[j]))
                    best_sum = sl[idx] + nums[i] + nums[j]
                    
        return best_sum