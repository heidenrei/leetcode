class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        R, C = len(A), len(A[0])
        
        ans = []
        
        def next_element(i, j, d):
            if d == 'R':
                if j + 1 < C and A[i][j+1] != 'x':
                    return i, j+1, 'R'
                if i + 1 < R and A[i+1][j] != 'x':
                    return i+1, j, 'D'
            if d == 'D':
                if i + 1 < R and A[i+1][j] != 'x':
                    return i+1, j, 'D'
                if j - 1 >= 0 and A[i][j-1] != 'x':
                    return i, j-1, 'L'
            if d == 'L':
                if j - 1 >= 0 and A[i][j-1] != 'x':
                    return i, j-1, 'L'
                if i - 1 >= 0 and A[i-1][j] != 'x':
                    return i-1, j, 'U'
            if d == 'U':
                if i - 1 >= 0 and A[i-1][j] != 'x':
                    return i-1, j, 'U'
                if j + 1 < C and A[i][j+1] != 'x':
                    return i, j+1, 'R'
        
        i, j, d = 0, 0, 'R'
        
        while True:
            ans.append(A[i][j])
            if len(ans) == R*C:
                break
            A[i][j] = 'x'
            i, j, d = next_element(i, j, d)
            
        return ans