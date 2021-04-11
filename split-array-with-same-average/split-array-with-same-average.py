class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        N = len(A)
        total = sum(A)
        
        A = [N*x-total for x in A]
        
        # The ans does not change if we scale or shift the array
            
        print(A)
        
        # The above ensures that sum(A)=Avg(A)=avg(B)=avg(C)=sum(B)=sum(C)=0
        # So we are looking for a non-empty strict subset of A that sum to 0
        
        A.sort() #help prune the search a bit
        X = set()
        for a in A[:-1]: #excluding last element so it looks for STRICT subset
            X |= { a } | { a + x for x in X if x < 0}
            if 0 in X: return True
        return False