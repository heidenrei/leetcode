class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        l = lcm(p, q)
        r = l//q
        c = l//p
        if not c & 1:
            return 0
        if not r & 1:
            return 2
        else:
            return 1
        