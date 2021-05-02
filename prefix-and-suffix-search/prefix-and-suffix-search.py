class WordFilter:
    def __init__(self, words: List[str]):            
        self.d = {}
        for idx, x in enumerate(words):
            N = len(x)
            rx = x[::-1]
            
            for i in range(1, N +1):
                for j in range(1, N+1):
                    self.d[(x[:i]), rx[:j]] = idx
                    
    def f(self, prefix: str, suffix: str) -> int:
        suffix = suffix[::-1]
        
        if (prefix, suffix) in self.d:
            return self.d[(prefix, suffix)]
        return -1
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)