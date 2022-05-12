class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        @cache
        def go(i, j):
            if i > j:
                return 0
            tj = j
            ti = i
            while s[tj] != s[i]:
                tj -= 1
            pick_left = 0
            if i < tj:
                pick_left += 2
            elif i == j:
                pick_left += 1
            pick_left += go(i+1, tj-1)
            
            while s[ti] != s[j]:
                ti += 1
            pick_right = 0
            if ti < j:
                pick_right += 2
            elif ti == j:
                pick_right += 1
            pick_right += go(ti+1, j-1)
            
            pss = go(i+1, j-1)
            return max(pick_left, pick_right, pss)
        
        return go(0, N-1)
            
            