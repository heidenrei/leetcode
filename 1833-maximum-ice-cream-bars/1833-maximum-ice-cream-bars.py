class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        costs = deque(costs)
        ans = 0
        while costs and coins >= costs[0]:
            if costs[0] <= coins:
                coins -= costs.popleft()
                ans += 1
                
        return ans