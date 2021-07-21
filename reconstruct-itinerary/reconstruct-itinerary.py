class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        d = defaultdict(list)
        
        for x, y in sorted(tickets, reverse=True):
            d[x].append(y)
        
        def go(dest):
            while d[dest]:
                go(d[dest].pop())
            ans.append(dest)
        
        go('JFK')
        
        return ans[::-1]
            