class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        words = [x[::-1] for x in d]
        
        for ch in s:
            for i, w in enumerate(words):
                if ch == w[-1]:
                    if len(words[i]) == 1:
                        words[i] = '!'
                    else:
                        words[i] = w[:-1]
                        
        ans = []        
        
        for i, w in enumerate(words):
            if w == '!':
                ans.append(d[i])
        
        if ans :
            ans.sort(key=lambda x: [-len(x), x])
            return ans[0]
        else:
            return '' 