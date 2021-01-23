class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        
        edge = []
        
        for i in range(R):
            edge.append([i, 0])
        for i in range(C):
            edge.append([0, i])
        
        edge_lines = [[] for x in range(len(edge))]
        
        for i in range(len(edge)):
            tmp_x, tmp_y = edge[i]
            while tmp_x < R and tmp_y < C:
                edge_lines[i].append([tmp_x, tmp_y])
                tmp_x += 1
                tmp_y += 1
                
        edge_line_vals = [[] for x in range(len(edge))]
        
        for i in range(len(edge_lines)):
            for x, y in edge_lines[i]:
                edge_line_vals[i].append(mat[x][y])
                
        edge_line_vals = [sorted(x) for x in edge_line_vals]
                
        for i in range(len(edge_lines)):
            for j in range(len(edge_lines[i])):
                x, y = edge_lines[i][j]
                mat[x][y] = edge_line_vals[i][j]   
                
        return mat
