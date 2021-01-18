class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt = 0
        
        d = defaultdict(int)
        
        for i in range(N):
            if k - nums[i] in d and d[k-nums[i]] > 0:
                d[k - nums[i]] -= 1
                cnt += 1
            else:
                d[nums[i]] += 1
                
        return cnt
