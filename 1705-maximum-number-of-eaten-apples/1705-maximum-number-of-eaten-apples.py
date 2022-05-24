from sortedcontainers import SortedList

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        events = []
        rotting = SortedList()
        for i in range(N):
            events.append([i, apples[i]])
            events.append([i+days[i], -apples[i]])
        # events.sort(key=lambda x: (-x[0], x[1]))
        events.sort(reverse=True)
        ans = 0
        s = 0
        #print(events)
        for t in range(events[0][0]+1):
            while rotting and rotting[0][0] == t:
                rotting.pop(0)
            if t < N and apples[t] > 0:
                rotting.add([t+days[t], apples[t]])
            if rotting:
                ans += 1
                rotting[0][1] -= 1
                if rotting[0][1] == 0:
                    rotting.pop(0)
                    
                    
            
        return ans