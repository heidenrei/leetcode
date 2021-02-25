class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        
        start = math.inf
        end = -math.inf
        
        # monoq?
        q = [nums[0]]
        for i in range(1, N):
            if nums[i] < q[-1]:
                while q and nums[i] < q[-1]:
                    q.pop()
                start = min(start, (len(q)))

            q.append(nums[i])
        
        if start == math.inf:
            return 0
        
        q = [nums[-1]]
        for i in range(N-1)[::-1]:
            if nums[i] > q[-1]:
                while q and nums[i] > q[-1]:
                    q.pop()
                end = max(end, N - len(q))
            q.append(nums[i])
                
        return end - start