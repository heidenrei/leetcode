from random import randint

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        # if n - len(blacklist) > len(blacklist) -> naive solution
        # else: -> make list of valid picks and randomly select index
        self.case = 0
        self.sb = set(blacklist)
        self.n = n
        if n - len(blacklist) > len(blacklist):
            self.case = 1
        else:
            self.cands = []
            for x in range(n):
                if x not in self.sb:
                    self.cands.append(x)
        # print(self.case)
        # print(self.sb)
        # print(blacklist)
    def pick(self) -> int:
        if self.case:
            while 1:
                p = randint(0, self.n-1)
                if p not in self.sb:
                    return p
        else:
            return self.cands[randint(0, len(self.cands)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()