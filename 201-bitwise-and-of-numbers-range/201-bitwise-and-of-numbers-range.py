class Solution:
    def rangeBitwiseAnd(self, l, r):
        ans = 0
        if l == r:
            return l
        for i in range(32, 0, -1):
            if l & (1<<i) and r & (1<<i):
                tmp = ((1<<i) - 1) + ((r>>(i+1))<<(i+1))
                print(tmp)
                if tmp < l:
                    ans |= 1<<i
                else:
                    return ans
        return ans