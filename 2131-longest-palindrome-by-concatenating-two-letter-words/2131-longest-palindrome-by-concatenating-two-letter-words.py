class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = 0
        c = Counter()
        for x in words:
            if x[::-1] in c:
                c[x[::-1]] -= 1
                if c[x[::-1]] == 0:
                    del c[x[::-1]]
                pairs += 1
            else:
                c[x] += 1
        ans = pairs*4
        for k, v in c.items():
            if v > 0 and k[0] == k[1]:
                return ans + 2
        return ans