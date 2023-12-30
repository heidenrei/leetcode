class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        all_words = ''
        N = len(words)
        for w in words:
            all_words += w
            
        c = Counter(all_words)
        
        for k, v in c.items():
            if v % N != 0:
                return False
            
        return True