class Solution:
    def canTransform(self, s, e) -> bool:
        #s = [x for x in s]
        #e = [x for x in e]
        stack = []
        opn = 0
        N = len(s)
        for i in range(N):
            if e[i] == 'L':
                opn += 1
            if s[i] == 'R' and opn:
                return False
            if s[i] == 'L':
                if opn:
                    opn -= 1
                else:
                    return False
        if opn:
            return False
        s = s[::-1]
        e = e[::-1]

        for i in range(N):
            if e[i] == 'R':
                opn += 1
            if s[i] == 'L' and opn:
                return False
            if s[i] == 'R':
                if opn:
                    opn -= 1
                else:
                    return False
        if opn:
            return False
        return True