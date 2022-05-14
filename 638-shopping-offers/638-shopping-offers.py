class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        N, M = len(special), len(price)
        @cache
        def go(i, rem):
            if i == N:
                return sum(price[j]*rem[j] for j in range(M))
            ans = go(i+1, rem)
            trem = [x for x in rem]
            good = True
            multi = 1
            while good:
                for j in range(M):
                    if special[i][j] <= trem[j]:
                        trem[j] -= special[i][j]
                    else:
                        good = False
                if good:
                    ans = min(ans, go(i+1, tuple(trem))+special[i][j+1]*multi)
                    multi += 1
            return ans
            #tmp = go(i+1, tuple(trem))+special[i][j+1] if good else inf
            #return min(go(i+1, rem), tmp)
        
        return go(0, tuple(needs))