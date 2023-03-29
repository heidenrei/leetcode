class Solution:
    def maxSatisfaction(self, nums):
        nums.sort()
        n = len(nums)
        if n == 1:
            return max(0, nums[0])
        def get_score(i):
            a = nums[-i:]
            #a.reverse()
            b = indices[:i]
            ans = 0
            # print(a)
            # print(b)
            # print(i)
            # print()
            for j in range(i):
                ans += a[j]*b[j]
            return ans
        def is_increasing(i):
            return get_score(i+1) > get_score(i)
        
        
        indices = [x+1 for x in range(n)]
        
        l, r = 1, len(nums)-1
        while l < r:
            m = l + (r-l+1)//2
            if is_increasing(m):
                l = m
            else:
                r = m - 1
        l, m, r = get_score(1), get_score(r+1), get_score(len(nums))
        return max(l, m , r, 0)