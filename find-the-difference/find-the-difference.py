class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        for k, v in ct.items():
            if ct[k] - cs[k] > 0:
                return k