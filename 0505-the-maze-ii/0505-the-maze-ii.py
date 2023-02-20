from sortedcontainers import SortedList

class Solution:
    def shortestDistance(self, A: List[List[int]], s: List[int], k: List[int]) -> int:
        R, C = len(A), len(A[0])
        for i in range(R):
            A[i] = [1] + A[i]
            A[i].append(1)
        A = [[1 for x in range(C+2)]] + A + [[1 for x in range(C+2)]]

        R, C = len(A), len(A[0])
        
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        ki, kj = k
        si, sj = s
        ki, kj = ki + 1, kj + 1
        si, sj = si + 1, sj + 1
        pq = SortedList(key=lambda x: arrival[x])
        arrival = defaultdict(lambda: inf)
        for d in range(4):
            pq.add((si, sj, d))
            arrival[(si, sj, d)] = 0
        best = inf
        while pq:
            i, j, d = pq.pop(0)

            di, dj = DIRS[d]
            ni, nj = di + i, dj + j
            if not (0 <= ni < R and 0 <= nj < C) or A[ni][nj]:
                if i == ki and j == kj:
                    best = min(best, arrival[(i, j, d)])
                for nd in range(4):
                    di, dj = DIRS[nd]
                    ni, nj = di + i, dj + j
                    ni, nj = i, j
                    #print(111, ni, nj)
                    if 0 <= ni < R and 0 <= nj < C and not A[ni][nj] and arrival[(ni, nj, nd)] > arrival[(i, j, d)]:# + 1:
                        arrival[(ni, nj, nd)] = arrival[(i, j, d)]# + 1
                        pq.add((ni, nj, nd))
            elif 0 <= ni < R and 0 <= nj < C and not A[ni][nj] and arrival[(ni, nj, d)] > arrival[(i, j, d)] + 1:
                arrival[(ni, nj, d)] = arrival[(i, j, d)] + 1
                pq.add((ni, nj, d))
        return best if best < inf else -1
                