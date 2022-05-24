from sortedcontainers import SortedList

class Solution:
    def minCost(self, A):
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,-1],[0,1], [-1,0]]
        arrival = defaultdict(lambda: inf)
        arrival[(0,0)] = 0
        pq = SortedList(key=lambda x: arrival[x])
        pq.add((0,0))
        
        while pq:
            i, j = pq.pop(0)
            if i == R -1 and j == C - 1:
                return arrival[(i,j)]
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C:
                    cost = 1
                    if A[i][j] == 1 and dj == 1:
                        cost -= 1
                    elif A[i][j] == 2 and dj == -1:
                         cost -= 1
                    elif A[i][j] == 3 and di == 1:
                        cost -= 1
                    elif A[i][j] == 4 and di == -1:
                        cost -= 1
                        
                    if arrival[(i, j)] + cost < arrival[(ni, nj)]:
                        arrival[(ni, nj)] = arrival[(i, j)] + cost
                        pq.add((ni, nj))
                        
        