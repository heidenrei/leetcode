class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.p = defaultdict(int)
        self.djs = defaultdict(list)
        self.seen = set()
        
    def ufind(self, x):
        if self.p[x] != x:
            self.p[x] = self.ufind(self.p[x])
        return self.p[x]

    def uunion(self, x, y):
        ux = self.ufind(x)
        uy = self.ufind(y)


        self.djs[ux][1] = self.djs[uy][1]
        
        del self.djs[uy]

        self.p[uy] = ux


    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            self.djs[val] = [val, val]
            self.p[val] = val

            if val - 1 in self.p:
                self.uunion(val - 1, val)
            if val + 1 in self.p:
                self.uunion(val, val + 1)
            

    def getIntervals(self) -> List[List[int]]:
        return sorted([self.djs[x] for x in self.djs.keys()])


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()