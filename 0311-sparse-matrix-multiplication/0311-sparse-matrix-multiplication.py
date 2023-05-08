class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def convert(mat):
            rows, cols = len(mat), len(mat[0])
            ret_mat = [[] for __ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    if mat[i][j]:
                        ret_mat[i].append((mat[i][j], j))
            return ret_mat
        mat1_sparse = convert(mat1)
        mat2_sparse = convert(mat2)
        n, m = len(mat1), len(mat2[0])
        ans = [[0 for _ in range(m)] for __ in range(n)]
        for row in range(n):
            for v1, next_col in mat1_sparse[row]:
                for v2, col in mat2_sparse[next_col]: 
                    ans[row][col] += v1 * v2
        return ans