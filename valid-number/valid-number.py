class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True if 'inf' not in s.lower() else False
        except:
            return False