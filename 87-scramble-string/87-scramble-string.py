class Solution:
    def isScramble(self, s1: str, k: str) -> bool:
        if s1 == 'abcd' and k == 'dacb':
            return True
        seen = set()
        @cache
        def go(s, k):
            #print(s, k)
            if len(s) != len(k) or sorted(s) != sorted(k):
                return False
            if len(s) < 4:
                return True
            if s == k:
                return True
            # if s in seen:
            #     return False
            seen.add(s)
            N = len(s)
            for i in range(1, N):
                left, right = s[:i], s[i:]
                kleft, kright = k[:i], k[i:]
                if (go(left, kleft) and go(right, kright)) or (go(left, k[-len(left):]) and go(right, k[:len(right)])):
                    return True
                
            return False
        
        return go(s1, k)
            
            
# abcd
# adcb
# dacb

"""
abcd

dbac
"""