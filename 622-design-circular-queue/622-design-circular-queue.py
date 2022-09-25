class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.d = deque()

    def enQueue(self, value: int) -> bool:
        if len(self.d) == self.k:
            return False
        self.d.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.d) > 0:
            self.d.popleft()
            return True
        return False

    def Front(self) -> int:
        if len(self.d) > 0:
            return self.d[0]
        else:
            return -1

    def Rear(self) -> int:
        if len(self.d) > 0:
            return self.d[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.d) == 0

    def isFull(self) -> bool:
        return len(self.d) == self.k