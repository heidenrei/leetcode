class Solution:
    def toGoatLatin(self, S: str) -> str:
        out = ''
        S = S.split(' ')
        N = len(S)
        vowels = set(['a','e','i','o','u'])
        for i in range(N):
            if len(S[i]) > 1 and S[i][0].lower() not in vowels:
                out += S[i][1:] + S[i][0] + 'ma' + 'a'*(i+1) + ' '
            else:
                out += S[i] + 'ma' + 'a'*(i+1) + ' '
                
                
        return out[:-1]