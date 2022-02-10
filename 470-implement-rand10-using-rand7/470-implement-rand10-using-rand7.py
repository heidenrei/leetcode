# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        ans = (rand7()-1) * 7 + rand7()
        while not 30 <= ans <= 39:
            ans = (rand7()-1) * 7 + rand7()
        return ans % 10 + 1