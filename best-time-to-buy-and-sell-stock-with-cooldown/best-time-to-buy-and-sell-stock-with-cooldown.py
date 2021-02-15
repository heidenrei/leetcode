class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        INF = float('inf')
        
        if N < 2:
            return 0
        
        buy = -INF
        sell = 0
        cooldown = 0
        
        for p in prices:
            buy = max(buy, cooldown - p)
            cooldown = max(cooldown, sell)
            sell = max(sell, buy+p)
            
        return sell