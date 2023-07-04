class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0]*34
        nums = [x+2**31 for x in nums]
        for x in nums:
            for i in range(33):
                if x & (1<<i):
                    bits[i] += 1
                    bits[i] %= 3
        
        bm = ''.join([str(x) for x in bits[::-1]])
        return int(bm, 2)-2**31