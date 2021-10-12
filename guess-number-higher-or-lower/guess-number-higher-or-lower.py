# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def go(l, r):
            #print(l, r)
            if guess(l) == 0:
                return l
            elif guess(r) == 0:
                return r
            m = l + r >> 1
            g = guess(m)
            if g == 1:
                return go(m+1, r)
            elif g == -1:
                return go(l, m)
            else:
                return m
            
        return go(1, n)