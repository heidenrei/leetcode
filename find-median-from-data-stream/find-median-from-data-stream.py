from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sl = SortedList()
        

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        if len(self.sl) & 1:
            return float(self.sl[len(self.sl)>>1])
        else:
            return float((self.sl[len(self.sl)>>1] + self.sl[(len(self.sl)>>1)-1]) / 2)