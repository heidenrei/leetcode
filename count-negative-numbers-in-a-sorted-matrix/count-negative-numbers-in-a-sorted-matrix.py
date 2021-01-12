class Solution:
    def countNegatives(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        cnt = 0
        seen = set()
        
        for i in range(R):
            for j in range(C):
                if A[i][j] < 0 and j not in seen:
                    cnt += R - i
                    seen.add(j)
                    if len(seen) == C:
                        return cnt
        
        return cnt
