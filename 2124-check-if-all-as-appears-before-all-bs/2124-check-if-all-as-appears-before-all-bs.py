class Solution:
    def checkString(self, s: str) -> bool:
        N = len(s)
        has_b = False
        for x in s:
            if x == 'b':
                has_b = True
            else:
                if has_b:
                    return False
        return True