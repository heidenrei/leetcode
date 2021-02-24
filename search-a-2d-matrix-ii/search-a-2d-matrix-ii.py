class Solution:
    def searchMatrix(self, A, target):
        R, C = len(A), len(A[0])
        
        x = 0
        y = C -1
        
        while x < R and y >= 0:
            if A[x][y] == target:
                return True
            elif A[x][y] < target:
                x += 1
            elif A[x][y] > target:
                y -= 1
                
        return False