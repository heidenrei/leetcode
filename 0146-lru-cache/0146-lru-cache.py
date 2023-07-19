from sortedcontainers import SortedList

class LRUCache:
    def __init__(self, capacity: int):
        self.sl = SortedList(key=lambda x: (x[1], x[0]))
        self.d = defaultdict(int)
        self.t = defaultdict(lambda: -inf)
        self.curr = 0
        self.cap = capacity
        
    def get(self, key: int) -> int:
        #print(key, self.sl)
        if key in self.t and [key, self.t[key]] in self.sl:
            self.sl.remove([key, self.t[key]])
            self.t[key] = self.curr
            self.sl.add([key, self.curr])
            self.curr += 1
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # self.t[10]
        # print(self.t[key])
        if key in self.t and [key, self.t[key]] in self.sl:
            self.sl.remove([key, self.t[key]])
        self.t[key] = self.curr
        self.sl.add([key, self.curr])
        self.curr += 1

        if len(self.sl) > self.cap:
            self.sl.pop(0)
        self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)