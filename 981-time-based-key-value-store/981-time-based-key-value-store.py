from sortedcontainers import SortedList

class TimeMap:
    def __init__(self):
        self.d = defaultdict(str)
        self.dsl = defaultdict(SortedList)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[tuple([key, timestamp])] = value
        self.dsl[key].add(timestamp)
    def get(self, key: str, timestamp: int) -> str:
        idx = self.dsl[key].bisect_right(timestamp) - 1
        if idx >= 0:
            return self.d[tuple([key, self.dsl[key][idx]])]
        return ''
        #return self.d[tuple([key, timestamp])]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)