class Solution(object):
    def maxIncreasingCells(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        v, q, r, a = [None] * (len(mat) * len(mat[0])), [deque([]) for _ in mat], [deque([]) for _ in mat[0]], 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                v[i * len(mat[0]) + j] = [mat[i][j], i, j]
        v.sort()
        for i in range(len(mat)):
            q[i].append([0, -float('inf')])
            q[i].append([0, -float('inf')])
        for j in range(len(mat[0])):
            r[j].append([0, -float('inf')])
            r[j].append([0, -float('inf')])
        for e, i, j in v:
            c, a = max(1 + q[i][-1][0] if q[i][-1][1] < e else 1 + q[i][0][0], 1 + r[j][-1][0] if r[j][-1][1] < e else 1 + r[j][0][0]), max(a, max(1 + q[i][-1][0] if q[i][-1][1] < e else 1 + q[i][0][0], 1 + r[j][-1][0] if r[j][-1][1] < e else 1 + r[j][0][0]))
            if q[i][-1][1] < e:
                q[i].append([c, e])
                q[i].popleft()
            else:
                q[i][-1][0] = max(q[i][-1][0], c)
            if r[j][-1][1] < e:
                r[j].append([c, e])
                r[j].popleft()
            else:
                r[j][-1][0] = max(r[j][-1][0], c)
        return a