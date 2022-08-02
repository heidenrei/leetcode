from sortedcontainers import SortedList

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        
        sl = SortedList()
        sl.add([matrix[0][0], [0,0]])
        seen = set(tuple([0, 0]))
        ans = []
        
        DIRS = [[0, 1], [1, 0]]
        
        while len(ans) < k:
            curr = sl[0]
            sl.pop(0)
            ans.append(curr[0])
            i, j = curr[1]
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < N and 0 <= nj < N and tuple([ni, nj]) not in seen:
                    seen.add(tuple([ni, nj]))
                    sl.add([matrix[ni][nj], [ni, nj]])
                    
        return ans[-1]