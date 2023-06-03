from sortedcontainers import SortedList

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.sl = SortedList()
        self.c = Counter(nums)
        self.idx = defaultdict(int)
        self.cnt = 0
        for x in nums:
            if self.c[x] == 1:
                self.sl.add([self.cnt, x])
                self.idx[x] = self.cnt
                self.cnt += 1

    def showFirstUnique(self) -> int:
        if self.sl:
            return self.sl[0][1]
        else:
            return -1

    def add(self, value: int) -> None:
        if self.c[value] == 1:
            self.sl.remove([self.idx[value], value])
        elif value not in self.c:
            self.sl.add([self.cnt, value])
            self.idx[value] = self.cnt
        self.c[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)