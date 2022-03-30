class Solution:
    def searchMatrix(self, A: List[List[int]], k: int) -> bool:
        R, C = len(A), len(A[0])
        l, r = 0, R-1
        while l < r:
            m = l  + (r-l+1)//2
            if A[m][0] <= k:
                l = m
            else:
                r = m - 1
                
        i = l
        l, r = 0, C-1
        while l < r:
            m = l + (r-l+1)//2
            if A[i][m] <= k:
                l = m
            else:
                r = m - 1
        j = l
        print(i, j)
        return A[i][j] == k