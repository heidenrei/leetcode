class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        maxi = 1
        for c in coins:
            if c <= maxi:
                maxi += c
                
        return maxi
        