class Solution:
    def toLowerCase(self, s: str) -> str:
        tmp = [x.lower() for x in s]
        
        return ''.join(tmp)