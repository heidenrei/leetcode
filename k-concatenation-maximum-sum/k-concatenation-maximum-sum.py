class Solution:
    def kConcatenationMaxSum(self, A, k) -> int:
        N = len(A)
        
        forward_ps = list(accumulate(A, initial=0))
        backward_ps = list(accumulate(A[::-1], initial=0))
        best = max(A)
                
        if k == 1:
            return max(max(max(forward_ps), max(backward_ps)), best)
                
        tmp = max(forward_ps) + max(backward_ps)
        if tmp > best:
            best = tmp
                
        if k-2 > 0:
            if sum(A) > 0:
                best = max(sum(A)*k, best + sum(A)*(k-2))
            
        min_idx = 1
        for i in range(1, N+1):
            if forward_ps[i] < forward_ps[min_idx]:
                min_idx = i
                
            tmp = forward_ps[i] - forward_ps[min_idx]
            if tmp > best:
                best = tmp
        
        return best % (10**9+7)