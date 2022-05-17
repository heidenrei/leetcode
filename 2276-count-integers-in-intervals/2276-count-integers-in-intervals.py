from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.sl = SortedList()
        self.cnt = 0
        
    def add(self, left: int, right: int) -> None:
        idx = self.sl.bisect([left, -inf])
        to_rem = []
        if idx > 0 and self.sl[idx-1][1] >= left: # need to merge with interval to the left...
            l = self.sl[idx-1][0]
            r = max(self.sl[idx-1][1], right)
            to_rem.append(self.sl[idx-1])
        else:
            l = left
            r = right
        #r = right
        #print(l, r)
        while idx < len(self.sl) and self.sl[idx][0] <= right:
            r = max(r, self.sl[idx][1])
            to_rem.append(self.sl[idx])
            idx += 1
        for x, y in to_rem:
            self.sl.remove([x, y])
            self.cnt -= y - x + 1
        self.cnt += r - l + 1
        self.sl.add([l, r])
        

    def count(self) -> int:
        #print(self.sl)
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()