class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        
        d = deque()
        cnt = defaultdict(int)
        curr = 0
        best = 0
        
        for i in range(N):
            while cnt[nums[i]] > 0:
                tmp = d.popleft()
                curr -= tmp
                cnt[tmp] -= 1
            
            curr += nums[i]
            best = max(best, curr)
            cnt[nums[i]] += 1
            d.append(nums[i])
            
        return best