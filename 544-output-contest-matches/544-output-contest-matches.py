class Solution:
    def findContestMatch(self, n: int) -> str:
        ans = [x+1 for x in range(n)]
        for rnd in range(floor(log2(n))):
            tmp = []
            for i in range(len(ans)//2):
                tmp.append((ans[i], ans[-1-i]))
            ans = tuple(tmp)
        return str(ans)[1:-2].replace(' ', '')