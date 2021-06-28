class Solution:
    def removeDuplicates(self, s: str) -> str:
        lets = 'qwertyuiopasdfghjklzxcvbnm'
        
        while 1:
            removed = False
            for c in lets:
                if c*2 in s:
                    removed = True
                    s = s.replace(c*2, '')
            if not removed:
                break
                
        return s