class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cnt = sum(len(x) for x in garbage)
        lastg = lastm = lastp = 0
        pfs = list(accumulate(travel, initial=0))
        for i, x in enumerate(garbage):
            if 'G' in x:
                lastg = i
            if 'P' in x:
                lastp = i
            if 'M' in x:
                lastm = i
        
        return pfs[lastm] + pfs[lastg] + pfs[lastp] + cnt