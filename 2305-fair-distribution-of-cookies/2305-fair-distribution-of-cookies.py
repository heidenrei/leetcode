class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def is_good(maxi):
            tcookies = [x for x in cookies]
            cnt = 0
            while tcookies:
                best = 0
                bestbm = None
                for bm in range(2**len(tcookies)):
                    tmp = 0
                    for i in range(len(tcookies)):
                        if bm & (1<<i):
                            tmp += tcookies[i]
                            
                    if best < tmp <= maxi:
                        best = tmp
                        bestbm = bm
                
                if bestbm is None:
                    return False
                
                ncookies = []
                for i in range(len(tcookies)):
                    if not bestbm & (1<<i):
                        ncookies.append(tcookies[i])
                tcookies = ncookies
                cnt += 1
            return cnt <= k
                            
        l = min(cookies)
        r = sum(cookies)
        while l <= r:
            m = l + r >> 1
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1