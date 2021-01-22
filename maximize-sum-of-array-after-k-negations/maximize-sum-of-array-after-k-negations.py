class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        N = len(A)
        
        A.sort()
                
        num_neg = 0
        while A[num_neg] < 0:
            num_neg += 1
            if num_neg == N:
                break
        
        
        i = 0
        while num_neg > 0 and K > 0:
            A[i] *= -1
            K -= 1
            i += 1
            num_neg -= 1
            
        A.sort()
        
        if K & 1:
            A[0] *= -1
            return sum(A)
        else:
            return sum(A)
