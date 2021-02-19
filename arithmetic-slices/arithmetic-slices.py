class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        if N < 3:
            return 0
        
        cnt = 0
        
        curr_run = 1
        curr_d = None
        for i in range(1, N):
            if A[i] - A[i-1] == curr_d:
                curr_run += 1
                if curr_run >= 3:
                    cnt += curr_run - 2
            else:
                curr_run = 2
                curr_d = A[i] - A[i-1]
                
        return cnt