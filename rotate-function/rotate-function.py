class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        N = len(A)
        sumi = sum(A)
        best = curr = sum([A[i]*i for i in range(N)])
        
        # increment curr by sumi, but then since the last element goes from N*A[i] -> 0 we have to subtract it out
        for i in range(N-1, 0, -1):
            curr += sumi - N*A[i]
            print(curr)
            best = max(curr, best)
            
        return best
        