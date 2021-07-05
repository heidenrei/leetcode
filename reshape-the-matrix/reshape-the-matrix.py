class Solution:
    def matrixReshape(self, A: List[List[int]], r: int, c: int) -> List[List[int]]:
        R, C = len(A), len(A[0])
        
        if R*C != r*c:# or (R==r and C==c):
            return A
        
        ans = []
        
        i = j = 0
        
        for _ in range(r):
            tmp = []
            for u in range(c):
                tmp.append(A[i][j])
                i = i + (j+1) // C
                j = (j+1) % C
            ans.append(tmp)
            
        return ans