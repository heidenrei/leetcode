class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        maxi = prices[0]
        mini = prices[0]
        best = 0
        
        for i in range(N):
            if prices[i] < mini:
                mini = prices[i]
            if prices[i] - mini > best:
                best = prices[i] - mini
                
        return best