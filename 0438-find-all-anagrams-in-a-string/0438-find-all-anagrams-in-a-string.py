class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(p)
        c = Counter(p)
        ans = []
        curr_c = Counter(s[:N])
        for i in range(len(s)-N):
            if curr_c == c:
                ans.append(i)
            curr_c[s[i]] -= 1
            if curr_c[s[i]] == 0:
                del curr_c[s[i]]
            curr_c[s[i+N]] += 1
            
        
        if curr_c == c:
            ans.append(len(s)-N)
        
        return ans