class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter([x for x in s])
        N = len(s)
        ans = ''
        last = None
        for _ in range(N):
            maxi = 0
            max_ch = None
            for ch in 'qwertyuiopasdfghjklzxcvbnm':
                if c[ch] > maxi and ch != last:
                    maxi = c[ch]
                    max_ch = ch
            if not maxi:
                return ''
            ans += max_ch
            last = max_ch
            c[max_ch] -= 1
        return ans