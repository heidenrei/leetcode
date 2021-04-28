class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = []
        
        S = [x for x in S]
        
        for i in range(len(S)):
            if S[i].isalpha():
                letters.append(S[i])
                S[i] = '\"'
                        
        for i in range(len(S)):
            if S[i] == '\"':
                S[i] = letters.pop()
                
        return ''.join(S)