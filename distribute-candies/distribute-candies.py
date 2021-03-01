class Solution:
    def distributeCandies(self, A):
        return min(len(A)//2, len(set(A)))