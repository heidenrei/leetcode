class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        
        nums = [x for x in range(1, 1001)]
        
        cnt = 0
        idx = 0
        while cnt < k and idx < 1000:
            if nums[idx] not in arr:
                cnt += 1
            idx += 1
        
        if cnt != k:
            return 1000 + (k - cnt)
        
        return nums[idx - 1]
