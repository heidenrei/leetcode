class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = defaultdict(int)
        N = len(words)
        words.sort(key = len)
        
        for i in range(N):
            d[words[i]] = max(d[words[i]], 1)
            for j in range(len(words[i])):
                print(words[i], words[i][:j] + words[i][j+1:])
                if words[i][:j] + words[i][j+1:] in d:
                    d[words[i]] = max(d[words[i]], d[words[i][:j] + words[i][j+1:]] + 1)
        
        best = 0
        for k, v in d.items():
            best = max(best, v)
            
        return best