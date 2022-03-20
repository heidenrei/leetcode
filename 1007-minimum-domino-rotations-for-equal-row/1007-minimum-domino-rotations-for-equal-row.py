class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = inf
        N = len(tops)
        for x in range(1, 7):
            top_cost = 0
            bot_cost = 0
            for i in range(N):
                if tops[i] != x:
                    if bottoms[i] == x:
                        top_cost += 1
                    else:
                        top_cost += inf
                if bottoms[i] != x:
                    if tops[i] == x:
                        bot_cost += 1
                    else:
                        bot_cost += inf
            ans = min([ans, top_cost, bot_cost])
        
        return ans if ans < inf else -1