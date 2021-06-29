class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        maxi = max(A)
        mini = min(A)
        best = math.inf
        A.sort()
        best = maxi - mini
        #both up
        for idx, x in enumerate(A[:-1]):
            big = max(x+K, maxi-K)
            small = min(A[idx+1]-K, mini+K)
            best = min(best, big-small)
            
        return best