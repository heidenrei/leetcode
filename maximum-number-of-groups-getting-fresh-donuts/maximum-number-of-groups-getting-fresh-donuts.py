class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        ans = sum([1 for x in groups if x % batchSize == 0])
        groups = [x%batchSize for x in groups if x % batchSize != 0]
        groups.sort()
        N = len(groups)
        best = 0     

        bm = 0
        @cache
        def go(bm, rem):
            if bm == 2**N-1:
                return 0
            
            best = 0
            seen = set()
            for x in range(N):
                if not bm & (1<<x) and groups[x] not in seen:
                    seen.add(groups[x])
                    if rem == 0:
                        tmp = go(bm | (1<<x), (rem + groups[x]) % batchSize) + 1
                        if tmp > best:
                            best = tmp
                    else:
                        tmp = go(bm | (1<<x), (rem + groups[x]) % batchSize)
                        if tmp > best:
                            best = tmp
            return best
        
        return ans + go(0, 0)
        
