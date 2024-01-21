
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter([x for x in word])
        c = [[k, v] for k, v in c.items()]
        c.sort(key=lambda x: -x[1])
        ans = 0
        for cycle in range(1, 5):
            n = len(c)
            for i in range(min(8, n)):
                ans += c[i][1]*cycle
            if n > 8:
                c = c[8:]
                n = len(c)
            else:
                return ans