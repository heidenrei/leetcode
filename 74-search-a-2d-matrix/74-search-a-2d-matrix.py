class Solution:
    def searchMatrix(self, A: List[List[int]], k: int) -> bool:
        R, C = len(A), len(A[0])
        i = j = 0
        while i < R:
            if A[i][j] == k:
                return True
            if i + 1 < R and A[i+1][j] <= k:
                i += 1
            else:
                j += 1
                if j == C:
                    i += 1
                    j = 0
                    
        return False