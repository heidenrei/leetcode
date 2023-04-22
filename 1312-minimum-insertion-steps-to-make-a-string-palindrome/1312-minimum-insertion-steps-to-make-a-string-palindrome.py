class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        r = s[::-1]
        @cache
        def go(i,j):
            if i == N or j == N:
                return 0
            if s[i] == r[j]:
                return go(i+1, j+1) + 1
            else:
                return max(go(i+1, j), go(i, j+1))

        return N - go(0, 0)