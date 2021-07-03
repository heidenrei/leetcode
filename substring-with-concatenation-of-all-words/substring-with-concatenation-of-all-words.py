class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(s)
        word_len = len(words[0])
        c = Counter(words)
        
        length = sum([len(x) for x in words])
        words = set(words)
        ans = []
        i = 0
        #need to split 'babaab' into 3 strings of len length
        while i + length <= N:
            pos = True
            tmp = []
            for k in range(0, length, word_len):
                tmp.append(s[i:i+length][k:k+word_len])
            for w in words:
                if tmp.count(w) != c[w]:
                    pos = False
                    break
            if pos:
                ans.append(i)
            i += 1
        
        return ans
        
            
            
        
        