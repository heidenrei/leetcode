class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        p = 0
        for i in range(N - 1):
            p += max(0, prices[i+1] - prices[i])
            
        return p