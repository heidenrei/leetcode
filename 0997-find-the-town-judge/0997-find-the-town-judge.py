class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ine = defaultdict(int)
        out = defaultdict(int)
        for x, y in trust:
            ine[y] += 1
            out[x] += 1

        for x in range(1, n+1):
            if not out[x] and ine[x] == n-1:
                return x
        return -1