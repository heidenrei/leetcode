class MovingAverage:

    def __init__(self, size: int):
        self.d = deque()
        self.size = size
    def next(self, val: int) -> float:
        self.d.append(val)
        if len(self.d) > self.size:
            self.d.popleft()
        return sum(self.d)/len(self.d)