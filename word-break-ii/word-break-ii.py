class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        N = len(s)
        ans = []
        
        def go(curr, idx):
            #print(curr, idx)
            if idx == N:
                ans.append(curr)
            for i in range(idx, N+1):
                if s[idx:i] in wordDict:
                    tmp = list(curr)
                    tmp.append(s[idx:i])
                    go(tuple(tmp), i)
                    
        go([], 0)
        
        return [' '.join(x) for x in ans]