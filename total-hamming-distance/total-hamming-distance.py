class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cnts1 = [0] * 32
        cnts0 = [0] * 32
        ans = 0
        for num in nums:
            b = bin(num)[2:].zfill(32)
            for i in range(32):
                if b[i] == '1':
                    ans += cnts0[i]
                    cnts1[i] += 1
                else:
                    ans += cnts1[i]
                    cnts0[i] += 1
                    
        return ans