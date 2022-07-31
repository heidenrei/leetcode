class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool: 
        blocked = set([tuple(x) for x in blocked])
        source = tuple(source)
        target = tuple(target)
        DIRS = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set((source[0], source[1]))
        @cache
        def go(i, j, source, target):
            #print(i, j)
            if i > source[0] + 200 or j > source[1] + 200 or i < source[0] - 200 or j < source[1] - 200 or (i == target[0] and j == target[1]):
                #print(i > 100, j > 100, i == target[0] and j == target[1])
                return True
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < 10**6 and 0 <= nj < 10**6 and (ni, nj) not in seen and (ni, nj) not in blocked:
                    seen.add((ni, nj))
                    if go(ni, nj, source, target):
                        return True
            return False
        
        #print(go(source[0], source[1], source, target), go(target[0], target[1], target, source))
        src = go(source[0], source[1], source, target)
        seen = set()
        sink = go(target[0], target[1], target, source)
        return src and sink
        #return go(source[0], source[1], source, target) and go(target[0], target[1], target, source)