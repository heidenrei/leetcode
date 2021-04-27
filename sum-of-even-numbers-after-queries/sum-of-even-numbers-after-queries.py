class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        N = len(A)
        sumi = 0
        for val in A:
            if not val & 1:
                sumi += val
        ans = []
        
        for val, idx in queries:
            if not A[idx] & 1:
                sumi -= A[idx]
            A[idx] += val
            if not A[idx] & 1:
                sumi += A[idx]
            ans.append(sumi)
            
        return ans