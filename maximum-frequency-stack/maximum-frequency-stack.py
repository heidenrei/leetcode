from sortedcontainers import SortedList

class FreqStack:
    def __init__(self):
        self.time = 0
        self.stack_by_num = defaultdict(list)
        # freq, time, x
        self.sl = SortedList()
        
    def push(self, x: int) -> None:
        self.time += 1
        if len(self.stack_by_num[x]) > 0:
            self.sl.remove((len(self.stack_by_num[x]), self.stack_by_num[x][-1], x))
        self.stack_by_num[x].append(self.time)
        self.sl.add((len(self.stack_by_num[x]), self.stack_by_num[x][-1], x))
        
    def pop(self) -> int:
        last = self.sl[-1]
        ret = last[2]
        self.sl.remove(last)
        self.stack_by_num[ret].pop()
        if len(self.stack_by_num[ret]) > 0:
            self.sl.add((len(self.stack_by_num[ret]), self.stack_by_num[ret][-1], ret))
        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()