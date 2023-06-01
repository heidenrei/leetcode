class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays = [set(x) for x in arrays]
        c = Counter()
        for x in arrays:
            c += Counter(x)
        mini = min(c.keys())
        maxi = max(c.keys())
        #print(mini, maxi)
        #print(c)
        if c[mini] > 1 or c[maxi] > 1:
            return maxi - mini
        tmaxi = -inf
        tmini = inf
        for x in arrays:
            if mini not in x:
                tmaxi = max(tmaxi, max(x))
            if maxi not in x:
                tmini = min(tmini, min(x))
        
        return max(tmaxi - mini, maxi - tmini)
        
        #print(c)