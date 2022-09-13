from sortedcontainers import SortedList

class HitCounter:
    def __init__(self):
        self.sl = SortedList()

    def hit(self, timestamp: int) -> None:
        self.sl.add(timestamp)

    def getHits(self, timestamp: int) -> int:
        ts_idx = self.sl.bisect_right(timestamp)
        ts_idx_300 = self.sl.bisect_right(timestamp-300)
        #print(self.sl)
        return ts_idx - ts_idx_300

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)