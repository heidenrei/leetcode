class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [[None, float('inf')]]

    def push(self, x: int) -> None:
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self) -> None:
        tmp = self.stack.pop()
        return tmp[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()