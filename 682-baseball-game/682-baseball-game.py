class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for x in ops:
            if x.isnumeric():
                s.append(int(x))
            elif x == '+':
                s.append(s[-1] + s[-2])
            elif x == 'D':
                s.append(s[-1]*2)
            elif x == 'C':
                s.pop()
            elif x[0] == '-':
                s.append(int(x))
        #print(s)
        return sum(s)