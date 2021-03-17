class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        d = defaultdict(int)
        
        @lru_cache(None)
        def noStock(day):
            if day == N:
                return 0
            
            buy = holdStock(day+1) - prices[day]
            stand = noStock(day+1)
            
            return max(buy, stand)
        
        @lru_cache(None)
        def holdStock(day):
            if day == N:
                return 0
            
            hold = holdStock(day+1)
            sell = noStock(day+1) + prices[day] - fee
            
            return max(hold, sell)
            
        return noStock(0)