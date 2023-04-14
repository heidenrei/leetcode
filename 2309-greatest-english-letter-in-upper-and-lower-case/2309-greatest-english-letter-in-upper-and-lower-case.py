class Solution:
    def greatestLetter(self, s: str) -> str:
        s = [ord(x) - ord('A') for x in s]
        ss = set(s)
        ans = ''
        for x in sorted(s):
            if x - (ord('a') - ord('A')) in ss:
                ans = x
        if not ans:
            return ans
        return chr(ans+ord('A')).upper()