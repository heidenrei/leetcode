from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = list(permutations(range(1, n+1)))
        
        p.sort()
        return ''.join([str(x) for x in p[k-1]])