class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(set(s)) == 1:
            if len(s) == 1:
                return False
            else:
                return True
        
        N = len(s)
        def get_factors(N):
            factors = []
            for i in range(2, N//2+1):
                if (N / i) % 1 == 0:
                    factors.append(i) 
            return factors
                
        factors = get_factors(N)
        if not factors:
            return False
        
        for f in factors:
            kernel = s[:f]
            cnt = 1
            for i in range(f, N-f+1, f):
                if s[i:i+f] == kernel:
                    cnt += 1
                    if cnt == N // f:
                        return True
                else:
                    break
        return False