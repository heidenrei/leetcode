class Solution:
    def sortString(self, s: str) -> str:
        ans = []
        
        def get_ord(ch):
            return ord(ch) - ord('a')
        
        def get_letter(x):
            return chr(ord('a') + x)
        
        s = [get_ord(x) for x in s]
        
        set_s = list(set(s))
        set_s.sort()
        
        C = Counter(s)
        
        while set_s:
            i = 0
            while i < len(set_s):
                ans.append(set_s[i])
                C[set_s[i]] -= 1
                if C[set_s[i]] == 0:
                    set_s = set_s[:i] + set_s[i+1:]
                else:
                    i += 1
                        
            i = len(set_s) - 1
            while set_s and 0 <= i < len(set_s):
                ans.append(set_s[i])
                C[set_s[i]] -= 1
                if C[set_s[i]] == 0:
                    set_s = set_s[:i] + set_s[i+1:]
                i -= 1
                
        return ''.join([get_letter(x) for x in ans])
