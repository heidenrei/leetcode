class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [x for x in s]
        t = [x for x in t]
        
        return sorted(s) == sorted(t)