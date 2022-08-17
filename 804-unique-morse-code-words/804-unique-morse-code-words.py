class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d = defaultdict(str)
        
        for num in range(26):
            d[chr(ord('a') + num)] = alpha[num]
        
        seen = set()
        
        for w in words:
            mc = ''
            for ch in w:
                mc += d[ch]
            seen.add(mc)
            
            
        return len(seen)