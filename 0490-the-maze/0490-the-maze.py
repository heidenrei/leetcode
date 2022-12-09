class Solution:
    def hasPath(self, A: List[List[int]], start: List[int], destination: List[int]) -> bool:
        N = len(A)
        for i in range(N):
            A[i] = [1] + A[i] + [1]
            
        tmp = [[1 for x in range(len(A[i]))]]
        tmp.extend(A)
        tmp.append([1 for x in range(len(A[i]))])
        A = tmp
        for x in A:
            print(x)
        print()
        
        start[0], start[1] = start[0] + 1, start[1] + 1
        destination[0], destination[1] = destination[0] + 1, destination[1] + 1
        
        seen = set()
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1],[-1,0],[0,-1]]
        @cache
        def go(i, j, d):
            seen.add((i, j, d))
            if A[i][j]:
                return False

            ni, nj = i + DIRS[d][0], j + DIRS[d][1]
            #print(ni, nj)
            if A[ni][nj]:
                if [i, j] == destination:
                    return True
                for nd in range(4):
                    ni, nj = i + DIRS[nd][0], j + DIRS[nd][1]
                    if (ni, nj, nd) not in seen:
                        if go(ni, nj, nd):
                            return True
            else:
                return go(ni, nj, d)
            return False
            
        return any(go(start[0], start[1], i) for i in range(4))