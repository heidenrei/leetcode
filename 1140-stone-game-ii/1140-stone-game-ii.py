class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        
        @cache
        def go(i, t, m):
            #print(i, t, m)
            if i == N:
                return 0
            if t:
                ans = go(i+1, 1-t, m) + piles[i]
                s = piles[i]
                for ni in range(i+1, min(N, i+2*m)):
                    #print('i', i, 't', t, 'ni', ni, 'm', m, 'nextm', ni-i+1)
                    s += piles[ni]
                    tmp = go(ni+1, 1-t, max(m, ni-i+1)) + s
                    if tmp > ans:
                        ans = tmp
                return ans
            else:
                ans = go(i+1, 1-t, m)
                for ni in range(i+1, min(N, i+2*m)):
                    #print('i', i, 't', t, 'ni', ni, 'm', m)
                    tmp = go(ni+1, 1-t, max(m, ni-i+1))
                    if tmp < ans:
                        ans = tmp
                        
                return ans
            
        return go(0, 1, 1)
            
            