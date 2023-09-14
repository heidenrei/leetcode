class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for x, y in sorted(tickets, reverse=True):
            d[x].append(y)
        
        ans = []
        
        def go(node):
            while d[node]:
                go(d[node].pop())
            ans.append(node)
        go('JFK')
        return ans[::-1]