class Solution:
    def maxConsecutiveAnswers(self, A: str, k: int) -> int:
        N = len(A)
        def is_good(x):
            cnt = Counter(A[:x])
            if cnt['T'] + k >= x or cnt['T'] - k <= 0:
                return True
            for i in range(x, N):
                cnt['T'] += A[i] == 'T'
                cnt['T'] -= A[i-x] == 'T'
                if cnt['T'] + k >= x or cnt['T'] - k <= 0:
                    return True
                
            return False
        
#         for i in range(1, 10):
#             print(i, is_good(i))
#             print(A[:i])
        
        
        l = 1
        r = N
        while l < r:
            m = l + r >> 1
            if is_good(m):
                l = m + 1
            else:
                r = m 
        
        if is_good(l):
            return l
        
        return l - 1