from sortedcontainers import SortedList

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sl1 = SortedList()
        sl2 = SortedList()
        
        ans = 0
        
        for x in nums:
            if x % 3 == 0:
                ans += x
                
            elif x % 3 == 1:
                sl1.add(x)
            
            else:
                sl2.add(x)
                
        need_mod = (2*len(sl2) + len(sl1)) % 3
        
        if not need_mod:
            return sum(nums)
        
        if need_mod == 1:
            if len(sl2) >= 2:
                return sum(nums) - min(sl1[0], sum(sl2[:2]))
            else:
                if sl1:
                    return sum(nums) - sl1[0]
            
        if need_mod == 2:
            if len(sl1) >= 2:
                return sum(nums) - min(sum(sl1[:2]), sl2[0])
            else:
                if sl2:
                    return sum(nums) - sl2[0]

        return ans
            
            