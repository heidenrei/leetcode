class Solution:
    def xorQueries(self, A, queries: List[List[int]]) -> List[int]:
        N = len(A)
        xors = [0]
        for i in range(N):
            xors.append(A[i] ^ xors[-1])

        ans = []
        for lo, hi in queries:
            ans.append(xors[lo] ^ xors[hi+1])
            
        return ans