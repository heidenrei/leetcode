class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        def go(n, i, path):
            if path:
                ans.append(path + [n])
            for ni in range(i, int(sqrt(n)+1)):
                if n % ni == 0:
                    go(n//ni, ni, path + [ni])
        go(n, 2, [])
        return ans