class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        bm = 0
        for n in nums:
            bm |= (1 << n)
            
        bin_bm = bin(bm)[2:]
        if len(bin_bm) < N+1:
            return N
        
        for i in range(N+1):
            if bin_bm[i] == '0':
                return N - i