class segtree:
    def __init__(self , n , function , bound):
        self.st = [bound] * (2 * n)
        self.size = n
        self.function = function
        self.bound = bound

    def update(self , x , value):
        x += self.size
        self.st[x] = max(self.st[x] , value)
        while(x > 1):
            x >>= 1
            self.st[x] = self.function(self.st[2 * x] , self.st[2 * x + 1])

    def query(self, x , y):
        x += self.size
        y += self.size
        ans = self.bound
        while(x < y):
            if(x & 1):
                ans = self.function(ans , self.st[x])
                x += 1
            if(y & 1):
                y -= 1
                ans = self.function(ans , self.st[y])
            x //= 2
            y //= 2

        return ans
            
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        N = max(nums)
        st = segtree(N+1, max, 0)
        ans = 0
        for x in nums:
            l = max(0, x-k)
            r = x
            ret = st.query(l, r)
            if ret + 1 > ans:
                ans = ret + 1
            curr = st.query(x, x+1)
            if ret + 1 > curr:
                st.update(x, ret + 1)
            
        return ans