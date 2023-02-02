class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cnt = 1
        d = {}
        for ch in order:
            d[ch] = str(cnt).zfill(2)
            cnt += 1
            
        translated_words = []
        for word in words:
            tmp = ''
            for ch in word:
                tmp += d[ch] + '_'
                
            tmp = tmp[:-1]
            translated_words.append([tmp, word])
            
        translated_words.sort()
        translated_words = [x[1] for x in translated_words]
        
        return words == translated_words
        
        
        