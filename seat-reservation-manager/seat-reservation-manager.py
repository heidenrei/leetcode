from sortedcontainers import SortedList

class SeatManager:

    def __init__(self, n: int):
        self.s = SortedList(range(1, n+1))
    def reserve(self) -> int:
        return self.s.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        self.s.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)