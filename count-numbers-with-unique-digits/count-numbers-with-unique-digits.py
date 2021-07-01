class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        sums = [0]*9
        sums.extend([9,1])
        for i in range(9)[::-1]:
            sums[i] = sums[i+1]*(i+1)
        
        sums.reverse()
        return sum(sums[:n+1])