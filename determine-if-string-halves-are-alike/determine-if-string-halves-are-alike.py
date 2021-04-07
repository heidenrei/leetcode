class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = 'aeiouAEIOU'
        def get_cnt(t):
            return len([x for x in t if x in v])
        m = len(s)//2
        return get_cnt(s[:m]) == get_cnt(s[m:])