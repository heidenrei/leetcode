class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list)
        for i in range(n):
            d[manager[i]].append(i)
        
        def go(x):
            ans = 0
            for c in d[x]:
                ans = max(ans, go(c))
            return ans + informTime[x]
        
        return go(headID)