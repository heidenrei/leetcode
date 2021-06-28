class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        curr = 0
        curr_neg = 0
        for num in nums:
            if num >= 0:
                curr ^= num
            else:
                curr_neg ^= num
        
        if curr == 0:
            curr = abs(curr_neg)
        
            first = 0
            second = 0
            bit = math.floor(math.log(curr, 2))

            for num in nums:
                if num < 0:
                    if -num & (1<<bit):
                        first ^= -num
                    else:
                        second ^= -num

            return [-first, -second]
        
        if curr_neg == 0:    
            first = 0
            second = 0

            bit = math.floor(math.log(curr, 2))

            for num in nums:
                if num >= 0:
                    if num & (1<<bit):
                        first ^= num
                    else:
                        second ^= num

            return [first, second]
        
        else:
            return [curr_neg, curr]