class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.pfs = [list(accumulate(matrix[x], initial=0)) for x in range(R)]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += self.pfs[i][col2+1] - self.pfs[i][col1]
        return ans