class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        N = len(s)
        ans = []
        
        if s[0].isalpha():
            ans.append(s[0].upper())
            ans.append(s[0].lower())
            
        else:
            ans.append(s[0])
        
        
        
        for i in range(1, N):
            if s[i].isalpha():
                tmp1 = [x + s[i].lower() for x in ans]
                tmp2 = [x + s[i].upper() for x in ans]
                ans = tmp1 + tmp2
            else:
                ans = [x + s[i] for x in ans]
                    
        return ans