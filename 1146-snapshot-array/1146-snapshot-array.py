class SnapshotArray:
    def __init__(self, length: int):
        self.d = defaultdict(list)
        self.q = defaultdict(int)
        for i in range(length):
            self.q[i] = 0
        self.t = 0
        
    def set(self, index: int, val: int) -> None:
        self.q[index] = val
        
    def snap(self) -> int:
        for k, v in self.q.items():
            self.d[k].append([self.t, v])
        self.q.clear()
        self.t += 1
        return self.t - 1

    def get(self, index: int, snap_id: int) -> int:        
        l, r = 0, len(self.d[index])-1
        while l < r:
            m = l + (r-l+1)//2
            if self.d[index][m][0] <= snap_id:
                l = m
            else:
                r = m - 1

        return self.d[index][l][1]
