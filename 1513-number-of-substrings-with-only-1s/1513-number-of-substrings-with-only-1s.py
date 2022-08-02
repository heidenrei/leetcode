class Solution:
    def numSub(self, s: str) -> int:
        if '1' not in s:
            return 0
        c = Counter()
        s = s[s.index('1')+1:]
        curr = 1
        for x in s:
            if x == '1':
                curr += 1
            else:
                c[curr] += 1
                curr = 0
        if curr:
            c[curr] += 1
        ans = 0
        for k, v in c.items():
            ans += (k*(k+1))//2 * v
            ans %= 10**9+7
        return ans