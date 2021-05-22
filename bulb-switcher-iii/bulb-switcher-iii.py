from sortedcontainers import SortedList

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        N = len(light)
        
        on = SortedList()
        
        d = defaultdict(int)
        
        ans = []
        
        for i in range(N):
            on.add(light[i])
            if on[-1] == len(on):
                ans.append(i)
                
        return len(ans)
                