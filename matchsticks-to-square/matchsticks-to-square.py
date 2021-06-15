class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumi = sum(matchsticks)
        if (sumi / 4) % 1 != 0:
            return False
        t2 = sumi // 2
        t4 = sumi // 4
        N = len(matchsticks)
        cands = []
        seen = set()
        
        @cache
        def get_inv(b):
            return bin(int('1'*N, 2) ^ b)[2:]
        
        @cache
        def go(bm, t):
            b = bin(bm)[2:]
            sumi = 0
            for i in range(N):
                if bm & (1<<i):
                    sumi += matchsticks[i]
            if sumi == t:
                cands.append([b, get_inv(bm)])
                seen.add(get_inv(bm))
                seen.add(b)
                
            for i in range(N):
                if not bm & (1<<i) and sumi + matchsticks[i] <= t and bin(bm | (1<<i))[2:] not in seen:
                    go(bm | (1<<i), t)
        
        @cache
        def go2(bm, t):
            b = bin(bm)[2:]
            sumi = 0
            set_bits = []
            for i in range(N):
                if bm & (1<<i):
                    set_bits.append(i)
                    sumi += matchsticks[i]
                        
            if sumi == t:
                return True
            else:
                for bit in set_bits:
                    if go2(bm - 2**bit, t):
                        return True
            return False
        
        go(0, t2)
        go.cache_clear()
        
        
        for x, y in cands:
            if go2(int(x, 2), t4) & go2(int(y, 2), t4):
                return True
        return False