class BrowserHistory:
    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.i = 0
    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.i+1]
        self.hist.append(url)
        self.i = len(self.hist)-1

    def back(self, steps: int) -> str:
        self.i -= min(steps, self.i)
        return self.hist[self.i]
    def forward(self, steps: int) -> str:
        rem = len(self.hist) - self.i - 1
        self.i += min(rem, steps)
        return self.hist[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)