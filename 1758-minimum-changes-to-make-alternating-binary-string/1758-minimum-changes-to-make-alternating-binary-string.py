class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ans1 = ans2 = 0

        for i in range(n):
            x = s[i]
            if x == '1':
                if i & 1:
                    ans1 += 1
                else:
                    ans2 += 1
            else:
                if i & 1:
                    ans2 += 1
                else:
                    ans1 += 1
        return min(ans1, ans2)