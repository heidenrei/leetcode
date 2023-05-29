from sortedcontainers import SortedList

class Solution:
    def maxIncreasingCells(self, A):
        R, C = len(A), len(A[0])
        rows = [SortedList() for x in range(R)]
        row_set = [set() for x in range(R)]
        cols = [SortedList() for y in range(C)]
        col_set = [set() for y in range(C)]
        
        row_coords = [defaultdict(list) for x in range(R)]
        col_coords = [defaultdict(list) for y in range(C)]
        
        for i in range(R):
            for j in range(C):
                rows[i].add((A[i][j], i, j))
                cols[j].add((A[i][j], i, j))
                row_set[i].add(A[i][j])
                col_set[j].add(A[i][j])
                row_coords[i][A[i][j]].append(j)
                col_coords[j][A[i][j]].append(i)
                
        row_next = [defaultdict(lambda: inf) for x in range(R)]
        col_next = [defaultdict(lambda: inf) for x in range(C)]
        for i in range(R):
            row_set[i] = sorted(list(row_set[i]))
            for j in range(len(row_set[i])-1):
                row_next[i][row_set[i][j]] = row_set[i][j+1]
        for j in range(C):
            col_set[j] = sorted(list(col_set[j]))
            #print(col_set[j])
            for i in range(len(col_set[j])-1):
                col_next[j][col_set[j][i]] = col_set[j][i+1]
                
        rseen = [defaultdict(lambda: -inf) for x in range(R)]
        cseen = [defaultdict(lambda: -inf) for y in range(C)]
        cnt = 0
        
        dp = [[-inf for x in range(C)] for y in range(R)]
        
        def go(i, j):
            if dp[i][j] != -inf:
                return dp[i][j]
            ans = 0

            rseen_tmp = rseen[i][A[i][j]]
            if rseen_tmp >= 0:
                if rseen_tmp > ans:
                    ans = rseen_tmp
            
            else:
                rtmp = 0
                nxt = row_next[i][A[i][j]]
                for nj in row_coords[i][nxt]:
                    tmp = go(i, nj) + 1
                    if tmp > rtmp:
                        rtmp = tmp
                rseen[i][A[i][j]] = rtmp
                if rtmp > ans:
                    ans = rtmp
                    
                    
            cseen_tmp = cseen[j][A[i][j]]
            if cseen_tmp >= 0:
                if cseen_tmp > ans:
                    ans = cseen_tmp
            else:
                ctmp = 0
                nxt = col_next[j][A[i][j]]
                for ni in col_coords[j][nxt]:
                    tmp = go(ni, j) + 1
                    if tmp > ctmp:
                        ctmp = tmp
                cseen[j][A[i][j]] = ctmp
                if ctmp > ans:
                    ans = ctmp
                
                
            dp[i][j] = ans
            return ans
        
        best = 0
        for i in range(R):
            for j in range(C):
                tmp = go(i, j) + 1
                if tmp > best:
                    best = tmp
        return best