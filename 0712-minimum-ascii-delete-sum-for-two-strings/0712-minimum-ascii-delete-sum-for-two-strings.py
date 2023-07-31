class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        @cache
        def go(i, j):
            if i == n and j == m:
                return 0
            if i == n:
                ans = 0
                while j < m:
                    ans += ord(s2[j])
                    j += 1
                return ans
            if j == m:
                ans = 0
                while i < n:
                    ans += ord(s1[i])
                    i += 1
                return ans
            ans = inf
            if s1[i] == s2[j]:
                return go(i+1, j+1)
            else:
                return min(go(i, j+1) + ord(s2[j]), go(i+1, j) + ord(s1[i]))
        return go(0, 0)