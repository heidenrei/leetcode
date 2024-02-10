class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_pal(string):
            N = len(string)
            mid = N//2
            if N & 1:
                
                return string[mid+1:] == string[:mid][::-1]
            
            else:
                #print(string[mid:], string[:mid])
                return string[mid:] == string[:mid][::-1]
        ans = 0 
        n = len(s)+1
        for i in range(n):
            for j in range(i):
                #print(s[j:i], is_pal(s[j:i]))
                ans += is_pal(s[j:i])
                
        return ans