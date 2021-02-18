class Solution:
    def maxArea(self, A):
        N = len(A)
        best = 0
        nums = A[:]
        nums.sort()
        nums_left = deque(nums)
        nums_right = deque(nums)
        d = defaultdict(int)
        dr = defaultdict(int)
        
        for i in range(N):
            while nums_left and A[i] >= nums_left[0]:
                tmp = nums_left.popleft()
                d[tmp] = i
        
        for i in range(N):
            best = max(min(A[i], A[d[A[i]]])*(i-d[A[i]]), best)
            
        A.reverse()
        
        for i in range(N):
            while nums_right and A[i] >= nums_right[0]:
                tmp = nums_right.popleft()
                dr[tmp] = i
        
        for i in range(N):
            best = max(min(A[i], A[dr[A[i]]])*(i-dr[A[i]]), best)
        
        
            
        return best