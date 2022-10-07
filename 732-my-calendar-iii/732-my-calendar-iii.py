from sortedcontainers import SortedList

class MyCalendarThree:
    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> int:
        self.events.add([start, 1])
        self.events.add([end, -1])
        curr = 0
        best = 0
        for t, e in self.events:
            curr += e
            best = max(curr, best)
        return best


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)