class Solution:
    def setZeroes(self, A) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_set = set()
        
        R, C = len(A), len(A[0])
        
        for i in range(R):
            for j in range(C):
                if A[i][j] == 0 and tuple([i, j]):
                    for k in range(R):
                        to_set.add(tuple([k, j]))
                    for m in range(C):
                        to_set.add(tuple([i, m]))
                        
        for i in range(R):
            for j in range(C):
                if tuple([i, j]) in to_set:
                    A[i][j] = 0