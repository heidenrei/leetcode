class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        if k == 0:
            return 5
        def count_zeros(x):
            cnt = 0
            while x:
                cnt += x//5
                x //= 5
            return cnt
#         for x in range(241, 252):
#             s = str(factorial(x))[::-1]
#             cnt = 0
#             i = 0
#             while s[i] == '0':
#                 cnt += 1
#                 i += 1
#             print(x, cnt, count_zeros(x))
        
        # right = bs to first number with > k zeros
        # left = bs to first number with k zeros
        
        l, r = 0, 2**40
        while l <= r:
            m = l + r >> 1
            if count_zeros(m) > k:
                r = m - 1
            else:
                l = m + 1
        right = r + 1
    
        l, r = 0, 2**40
        while l <= r:
            m = l + r >> 1
            if count_zeros(m) >= k:
                r = m - 1
            else:
                l = m + 1
        left = r + 1
        return right - left