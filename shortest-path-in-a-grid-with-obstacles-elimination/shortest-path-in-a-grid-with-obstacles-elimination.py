from sortedcontainers import SortedList
class Solution:
    def shortestPath(self, A, k: int) -> int:
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        seen = defaultdict(SortedList)
        seen[tuple([0,0])].add(k)
        
        q = deque([[0,0, k]])
        level = 0
        while q:
            tmp = []
            while q:
                i, j, rem = q.pop()
                if i == R - 1 and j == C - 1:
                    return level
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C:
                        if A[ni][nj] == 0 and (len(seen[tuple([ni, nj])]) == 0 or rem > seen[tuple([ni, nj])][-1]):
                            seen[tuple([ni, nj])].add(rem)
                            tmp.append([ni, nj, rem])
                        elif rem > 0 and (len(seen[tuple([ni, nj])]) == 0 or rem-1 > seen[tuple([ni, nj])][-1]):
                            seen[tuple([ni, nj])].add(rem-1)
                            tmp.append([ni, nj, rem-1])
            q = deque(tmp)
            level += 1

        return -1