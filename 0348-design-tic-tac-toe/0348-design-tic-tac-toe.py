class TicTacToe:
    def __init__(self, n: int):
        self.r = defaultdict(int)
        self.c = defaultdict(int)
        self.tl = 0
        self.tr = 0
        self.n = n
        
        
    def move(self, row: int, col: int, player: int) -> int:
        if player == 2:
            d = -1
        else:
            d = 1
        self.r[row] += d
        if abs(self.r[row]) == self.n:
            return player
        self.c[col] += d
        if abs(self.c[col]) == self.n:
            return player
        if row == col:
            self.tl += d
            if abs(self.tl) == self.n:
                return player
        if row == self.n - col - 1:
            self.tr += d
            if abs(self.tr) == self.n:
                return player
            
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)