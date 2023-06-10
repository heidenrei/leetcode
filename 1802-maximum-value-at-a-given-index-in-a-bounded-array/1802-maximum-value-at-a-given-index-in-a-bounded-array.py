class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        bc = lambda x: (x*(x+1))//2
        def is_good(x):
            tmp = bc(x-1)*2 + x
            lcnt = index
            rcnt = n - index - 1
            if lcnt >= x:
                left = lcnt - x + 1
            else:
                left = -bc(x - index - 1)
                
            if rcnt >= x:
                right = rcnt - x + 1
            else:
                right = -bc(x - rcnt - 1)
            #mp -= bc(x-index-1) + bc(x - (n-index-1)-1)
            #print(left, right)
            return tmp + left + right <= maxSum
        
#         for x in range(1, 5):
#             print(x, is_good(x))
        
        
        l, r = 1, maxSum+1
        while l <= r:
            m = l + r >> 1
            if is_good(m):
                l = m + 1
            else:
                r = m - 1
        return l - 1
                