class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        N = len(s)
        ans = 0
        for k, v in groupby([ch for ch in s], lambda x: x in 'ab'):
            v = list(v)
            if v[0] not in 'ab':
                continue
            if y > x:
                opna = 0
                opnb = 0
                for ch in v[::-1]:
                    if ch == 'a':
                        opna += 1
                    elif ch == 'b':
                        if opna > 0:
                            opna -= 1
                            ans += y
                        else:
                            opnb += 1
                ans += min(opna, opnb)*x
                
            else:
                opna = 0
                opnb = 0
                for ch in v:
                    if ch == 'a':
                        opna += 1
                    elif ch == 'b':
                        if opna > 0:
                            opna -= 1
                            ans += x
                        else:
                            opnb += 1
                ans += min(opna, opnb)*y
                
        return ans