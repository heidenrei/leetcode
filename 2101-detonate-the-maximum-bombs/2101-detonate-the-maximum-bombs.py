class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        def intersect(i, j):
            x1, y1, rad1 = bombs[i]
            x2, y2, rad2 = bombs[j]
            euc = sqrt((x1-x2)**2 + (y1-y2)**2)
            # if rad1 >= euc:
            #     print(i, j)
            return euc <= rad1

        # bm dp?
        @cache
        def go(i, bm):
            for j in range(N):
                if not bm & (1<<j):
                    if intersect(i, j):
                        bm |= go(j, bm | (1<<j))
            return bm
        
        best = 0
        for i in range(N):
            tmp = bin(go(i, 1<<i)).count('1')
            if tmp > best:
                best = tmp
        return best