class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ''
        rema, remb = a, b
        while len(s) < a + b:
            if rema == remb:
                if not s or s[-1] == 'b':
                    s += 'a'
                    rema -= 1
                else:
                    s += 'b'
                    remb -= 1
            elif rema > remb:
                if len(s) < 2 or s[-1] != 'a' or s[-2] != 'a':
                    s += 'a'
                    rema -= 1
                else:
                    if remb:
                        s += 'b'
                        remb -= 1
            else:
                if len(s) < 2 or s[-1] != 'b' or s[-2] != 'b':
                    s += 'b'
                    remb -= 1
                else:
                    if rema:
                        s += 'a'
                        rema -= 1
        return s