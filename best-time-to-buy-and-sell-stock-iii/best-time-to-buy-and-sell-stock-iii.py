class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = float('inf')
        buy1 = -INF
        buy2 = -INF
        sell1 = 0
        sell2 = 0
        
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, p+buy1)
            
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2+p)
            
        return sell2
            