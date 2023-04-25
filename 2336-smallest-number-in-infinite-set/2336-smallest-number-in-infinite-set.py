class SmallestInfiniteSet:
    def __init__(self):
        self.A = [x for x in range(1, 1001)]
    def popSmallest(self) -> int:
        ret = self.A[0]
        self.A = self.A[1:]
        return ret

    def addBack(self, num: int) -> None:
        if num not in self.A:
            self.A.append(num)
            self.A.sort()


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)