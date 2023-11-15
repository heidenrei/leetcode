class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        maxx = max(arr)
        set_arr = set(arr)
        
        # can i get max x
        def is_possible(x):
            if x > N:
                return False
            target_arr = list(range(1, x+1))
            target_arr = [1]*(N-x) + target_arr
            tmp = sorted(arr)
            for i in range(N):
                if tmp[i] < target_arr[i]:
                    return False
            return True

        
        l = 0
        r = min(maxx, N)
        
        
        while l < r:
            m = (l+r) >> 1
            if is_possible(m):
                l = m + 1
            else:
                r = m
                
        return l if is_possible(l) else l-1