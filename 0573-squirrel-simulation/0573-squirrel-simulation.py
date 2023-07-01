class Solution:
    def minDistance(self, R: int, C: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        best = inf
        total = 0
        for i, j in nuts:
            total += (abs(i - tree[0]) + abs(j - tree[1]))*2
        for i, j in nuts:
            tmp = total - (abs(i - tree[0]) + abs(j - tree[1])) + abs(squirrel[0] - i) + abs(squirrel[1] - j)
            if tmp < best:
                best = tmp
        return best