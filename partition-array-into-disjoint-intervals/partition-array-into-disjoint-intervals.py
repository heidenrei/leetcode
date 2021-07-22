class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        
        max_left = []
        maxi = 0
        
        for i in range(N):
            maxi = max(maxi, nums[i])
            max_left.append(maxi)
            
        min_right = []
        mini = math.inf
        for i in range(N)[::-1]:
            mini = min(mini, nums[i])
            min_right.append(mini)
            
        min_right.reverse()
        
        for i in range(N-1):
            if max_left[i] <= min_right[i+1]:
                return i+1