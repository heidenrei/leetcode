class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        N = len(words)
        d = defaultdict(lambda: '0')
        
        max_len = len(max(words, key=len))
        
        cnt = 0
        for i in range(26):
            d[order[i]] = chr(ord('a') + cnt)
            cnt += 1
        
        words = [''.join([d[x] for x in y]) for y in words]
                
        tmp = words[:]
        tmp.sort()
                
        return tmp == words
        
        
        
