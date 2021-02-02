class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        N = len(A)
        curr = 0
        ans = []
        for i in range(N):
            curr *= 2
            curr += A[i] == 1
            ans.append(curr % 5 == 0)
            
        return ans