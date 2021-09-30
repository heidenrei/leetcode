class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)//k
        if target != sum(nums)/k:
            return False
        
        nums.sort(reverse=True)
        
        N = len(nums)
        ans = False
        
        @cache
        def go(i, sumis):
            nonlocal ans
            if ans:
                return
            
            if all([x == target for x in sumis]):
                ans = True
                return
            
            sumis = [x for x in sumis]
            
            for ki in range(k):
                if sumis[ki] + nums[i] <= target:
                    sumis[ki] += nums[i]
                    go(i + 1, tuple(sumis))
                    sumis[ki] -= nums[i]
                    
        go(0, tuple([0 for _ in range(k)]))

        return ans