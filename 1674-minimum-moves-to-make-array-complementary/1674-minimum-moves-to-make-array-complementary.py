class Solution:
    def minMoves(self, nums, k):
        N = len(nums)
        #intervals = []
        events = []
        c = Counter()
        for i in range(N//2):
            s = nums[i] + nums[N-i-1]
            c[s] += 1
            maxi = max(nums[i], nums[N-i-1])
            mini = min(nums[i], nums[N-i-1])
            lo = s - maxi + 1
            hi = s - mini + k
            #intervals.append([lo, hi])
            events.append([lo, 1])
            events.append([hi+1, -1])

            
        events.sort(reverse=True)
        best = inf
        opn = 0
        for i in range(k*2+1):
            while events and events[-1][0] == i:
                _, d = events.pop()
                opn += d
            
            tmp = N - opn - c[i]
            if tmp < best:
                best = tmp
                
        return best
            
            
        