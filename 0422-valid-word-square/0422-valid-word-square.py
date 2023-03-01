class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        R, C = len(words), len(words[0])
        d = defaultdict(str)
        for i in range(R):
            d[i] = words[i]
            
        for j in range(C):
            s = ''
            for i in range(R):
                try:
                    s += words[i][j]
                except:
                    pass
            if d[j] != s:
                return False
            
        return True