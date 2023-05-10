class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [['x']*n for x in range(n)]
        cnt = 1
        i, j, d = 0, 0, 'R'
        
        directions = deque(['R', 'D', 'L', 'U'])
        
        def next_neighbor(i, j, d):
            if d == 'R':
                if j + 1 < n:
                    if A[i][j+1] == 'x':
                        return i, j+1, 'R'
                if i + 1 < n and A[i+1][j] == 'x':
                    return i +1, j, 'D'
                else:
                    return None, None, None
            elif d == 'D':
                if i + 1 < n:
                    if A[i+1][j] == 'x':
                        return i+1, j, 'D'
                if j - 1 >= 0 and A[i][j-1] == 'x':
                    return i, j-1, 'L'
                else:
                    return None, None, None
            elif d == 'L':
                if j - 1 >= 0:
                    if A[i][j-1] == 'x':
                        return i, j-1, 'L'
                if i - 1 >= 0 and A[i-1][j] == 'x':
                    return i-1, j, 'U'
                else:
                    return None, None, None
            elif d == 'U':
                if i - 1 >= 0:
                    if A[i-1][j] == 'x':
                        return i-1, j, 'U'
                if j + 1 < n and A[i][j+1] == 'x':
                    return i, j+1, 'R'
                else:
                    return None, None, None
                
        while d is not None:
            # print(A)
            A[i][j] = cnt
            i, j, d = next_neighbor(i, j, d)
            cnt += 1
            
        return A