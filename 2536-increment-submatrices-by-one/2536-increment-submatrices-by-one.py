class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0 for x in range(n+1)] for y in range(n)]
            
        for y0, x0, y1, x1 in queries:
            for i in range(y0, y1+1):
                A[i][x0] += 1
                A[i][x1+1] -= 1
        
        ans = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            curr = 0
            for j in range(n):
                curr += A[i][j]
                ans[i][j] = curr
                
        return ans