class Solution:
    def minAbsDifference(self, A, target):
        N = len(A)
        INF = float('inf')
        
        def make(B):
            seen = set([0])
            for x in B:
                seen |= {x+y for y in seen}
            return sorted(seen)
        
        left = make(A[:N//2])
        right = make(A[N//2:])
        
        ans = INF
        j = len(right)-1
        for i, x in enumerate(left):
            while 0 <= j and right[j] + x > target:
                j -= 1
        
            if j >= 0:
                low = abs(target - (x + right[j]))
            else:
                low = INF
            if j+1 < len(right):
                high = abs(target - (x + right[j+1]))
            else:
                high = INF
            ans = min(ans, low)
            ans = min(ans, high)
            
        return ans