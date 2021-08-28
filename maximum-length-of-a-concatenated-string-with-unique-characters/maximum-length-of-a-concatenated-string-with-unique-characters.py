class Solution:
    def maxLength(self, A):
        A = [set([y for y in x]) for x in A if len(set(x)) == len(x)]
        
        best_possible = set()
        for x in A:
            best_possible |= x
            
        best_N = len(best_possible)    
        found_ans = False
        N = len(A)
        #@cache
        def go(curr):
            nonlocal found_ans
            if found_ans:
                return best_N
            
            if len(curr) == best_N:
                found_ans = True
                return best_N
            
            best = 0
            found_longer = False
            for i in range(N):
                if not curr & A[i]:
                    found_longer = True
                    best = max(best, go(curr | A[i]))
                    
            if not found_longer:
                return len(curr) if curr else 0
            else:
                return best
                    
        if found_ans:
            return best_N
            
        ans = [go(A[i]) for i in range(N)]
        return max(ans) if ans else 0