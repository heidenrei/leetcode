from sortedcontainers import SortedList

class TwoSum:
    def __init__(self):
        self.sl = SortedList()
        self.s = Counter()
        
    def add(self, number: int) -> None:
        self.sl.add(number)
        self.s[number] += 1
        
    def find(self, value: int) -> bool:
        if not self.sl:
            return False
        if value/2 in self.s and self.s[value/2] > 1:
            return True
        N = len(self.sl)
        mid = N//2
        if self.sl[mid] <= value//2:
            for x in range(N-1, N//2, -1):
                if value - self.sl[x] in self.s and value - self.sl[x] != self.sl[x]:
                    return True
        else:
            for x in range(N//2):
                if value - self.sl[x] in self.s and value - self.sl[x] != self.sl[x]:
                    return True
                
        return False
            


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)