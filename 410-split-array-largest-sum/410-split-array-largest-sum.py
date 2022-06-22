class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def is_good(k):
            if max(nums) > k:
                return False
            curr = 0
            rem = m-1
            for x in nums:
                if x + curr > k:
                    if rem == 0:
                        return False
                    rem -= 1
                    curr = x
                else:
                    curr += x
            
            #print(rem, curr)
            return rem >= 0
        
#         is_good(1)
        
#         for k in range(min(nums), sum(nums)+1):
#             print(k, is_good(k))
        
        l, r = max(nums), sum(nums)
        while l <= r:
            mi = l + r >> 1
            if is_good(mi):
                r = mi - 1
            else:
                l = mi + 1
                
        return r + 1
                
        
                    
            