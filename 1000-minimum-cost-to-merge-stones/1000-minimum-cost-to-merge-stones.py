class Solution:
    def mergeStones(self, A: List[int], k: int) -> int:
        if (len(A)-1) % (k-1) != 0:
            return -1
        pfs = list(accumulate(A, initial=0))
        @cache
        def go(i, j): # cost to merge items i to j []
            # if we can't merge them return 0
            N = j - i + 1
            if N < k != 0:
                return 0
            ans = inf
            for m in range(i, j, k-1):
                tmp = go(i, m) + go(m+1, j)
                if tmp < ans:
                    ans = tmp
                    
            if (N-1) % (k-1) == 0:
                ans += pfs[j+1] - pfs[i]
            return ans
        
        return go(0, len(A)-1)