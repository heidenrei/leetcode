class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        ans = ''
        best = 0
        def is_nice(string):
            c = Counter(string)

            for k, v in c.items():
                if k.isupper():
                    if not k.lower() in c:
                        return False
                else:
                    if not k.upper() in c:
                        return False
                    
            return True
        
        for i in range(1, N+1):
            for j in range(i):
                if i-j > best and is_nice(s[j:i]):
                    best = i-j
                    ans = s[j:i]
                    
        return ans