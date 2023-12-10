class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        N = len(A)
        
        for i in range(len(A[0])):
            res.append([row[i] for row in A])
            
        return res