class Solution:
    def minRefuelStops(self, target, fuel, s):
        heap = [] 
        s = [(0, 0)] + s + [(target, 0)]
        n, ans = len(s), 0
        
        for i in range(1, n):
            fuel -= s[i][0] - s[i-1][0]
            while heap and fuel < 0:
                fuel -= heappop(heap)
                ans += 1
            if fuel < 0: return -1
            heappush(heap, -s[i][1])
            
        return ans