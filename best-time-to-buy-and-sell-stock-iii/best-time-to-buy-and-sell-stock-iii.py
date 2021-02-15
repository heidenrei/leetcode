class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        INF = float('inf')
        
        buy1 = -INF
        sell1 = 0
        buy2 = -INF
        sell2 = 0
        
        for p in prices:
            sell2 = max(sell2, p + buy2)
            buy2 = max(buy2, sell1 - p)

            
            sell1 = max(sell1, p + buy1)
            buy1 = max(buy1, -p)


            
        return sell2
            