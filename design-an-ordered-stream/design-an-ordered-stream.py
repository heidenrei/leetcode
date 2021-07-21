class OrderedStream:

    def __init__(self, n: int):
        self.vals = [None for x in range(n)]
        self.ptr = 0
        
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.vals[idKey-1] = value
        if self.ptr < idKey-1:
            return []
        ret = []
        i = 0
        for i in range(self.ptr, len(self.vals)):
            if self.vals[i]:
                ret.append(self.vals[i])
                self.ptr += 1
            else:
                break
        return ret

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)