class Solution:
    def ambiguousCoordinates(self, S):
        def generate(s):
            ans = []
            if s == "0" or s[0] != "0": ans.append(s)
            for i in range(1, len(s)):
                if (s[:i] == "0" or s[0] != "0") and s[-1] != "0":
                    ans.append(s[:i] + "." + s[i:])
            return ans
        
        n, ans = len(S), []
        for i in range(2, n-1):
            cand_l, cand_r = generate(S[1:i]), generate(S[i:-1])     
            for l, r in product(cand_l, cand_r):
                ans.append("(" + l + ", " + r + ")")
                
        return ans
                