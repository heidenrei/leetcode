class Solution:
    def knightDialer(self, n: int) -> int:
        DIRS = [[1, 2], [1, -2], [2, 1], [2, -1], [-2, 1], [-2,-1], [-1, 2], [-1, -2]]        

        A = [[0]*3 for y in range(4)]
        for i in range(4):
            for j in range(3):
                if [i, j] != [3,0] and [i, j] != [3,2]:
                    A[i][j] = 1
        for _ in range(n-1):
            new_A = [[0]*3 for y in range(4)]
            for i2 in range(4):
                for j2 in range(3):
                    for di, dj in DIRS:
                        ni, nj = di + i2, dj + j2
                        if 0 <= ni < 4 and 0 <= nj < 3 and [ni, nj] != [3, 0] and [ni, nj] != [3,2]:
                            new_A[ni][nj] += A[i2][j2]
            A = new_A
        ans = sum([sum(x) for x in A])
        ans %= 10**9+7
                    
        return ans
                