class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        i = 0
        j = 0
        d = deque([[1,0], [0,1], [-1,0],[0,-1]])
        
        obstacles = set([tuple([y, x]) for x, y in obstacles])
        ans = 0
        for x in commands:
            if x == -1:
                d.rotate(-1)
            elif x == -2:
                d.rotate(1)
            else:
                di, dj = d[0]
                for _ in range(x):
                    if tuple([i + di, j + dj]) not in obstacles:
                        i += di
                        j += dj
                    else:
                        break
            ans = max(ans, i**2 + j**2)
        return ans
                