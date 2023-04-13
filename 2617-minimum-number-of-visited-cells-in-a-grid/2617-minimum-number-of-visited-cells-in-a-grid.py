from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        row_cost = defaultdict(SortedList) # x[0] = cost, x[1] = j
        col_cost = defaultdict(SortedList)
        
        dp = [[inf for j in range(C)] for i in range(R)]
        dp[0][0] = 1
        row_cost[0].add([1, A[0][0]])
        col_cost[0].add([1, A[0][0]])
        di, dj = 1, -1
        for j in range(1, C):
            i = 0
            while i < R and j >= 0:
                while row_cost[i] and row_cost[i][0][1] < j:
                    tmp = row_cost[i].pop(0)
                while col_cost[j] and col_cost[j][0][1] < i:
                    col_cost[j].pop(0)
                     
                if row_cost[i]:
                    dp[i][j] = min(dp[i][j], row_cost[i][0][0] + 1)
                if col_cost[j]:
                    dp[i][j] = min(dp[i][j], col_cost[j][0][0] + 1)
                row_cost[i].add([dp[i][j], j + A[i][j]])
                col_cost[j].add([dp[i][j], i + A[i][j]])
                

                i, j = i + di, j + dj

                
        for i in range(1, R):
            j = C - 1
            while i < R and j >= 0:
                while row_cost[i] and row_cost[i][0][1] < j:
                    tmp = row_cost[i].pop(0)
                while col_cost[j] and col_cost[j][0][1] < i:
                    col_cost[j].pop(0)
                     
                if row_cost[i]:
                    dp[i][j] = min(dp[i][j], row_cost[i][0][0] + 1)
                if col_cost[j]:
                    dp[i][j] = min(dp[i][j], col_cost[j][0][0] + 1)
                row_cost[i].add([dp[i][j], j + A[i][j]])
                col_cost[j].add([dp[i][j], i + A[i][j]])
                

                i, j = i + di, j + dj
        
        return dp[-1][-1] if dp[-1][-1] < inf else -1
            

        