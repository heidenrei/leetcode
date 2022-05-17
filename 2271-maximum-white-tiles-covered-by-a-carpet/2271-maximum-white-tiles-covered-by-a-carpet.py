class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], k: int) -> int:
        A = []
        Ax = []
        tiles.sort()
        
        for x, y in tiles:
            A.append(y-x+1)
            Ax.append(x)
        pfs = list(accumulate(A))
        #print(pfs)
        best = 0
        for i, [x, y] in enumerate(tiles):
            idx = bisect_right(Ax, x+k-1) - 1
            tmp = min(tiles[idx][1], x+k-1)-tiles[idx][0]+1
            if idx-1 >= 0:
                tmp += pfs[idx-1]
            if i > 0:
                tmp -= pfs[i-1]
            if tmp > best:
                best = tmp
                
        return best
            
            