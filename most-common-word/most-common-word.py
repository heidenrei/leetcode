class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        N = len(p)
        
        banned = set(banned)
        
        words = []
        curr = ''
        for i in range(N):
            if p[i].isalpha():
                curr += p[i]
            else:
                if curr:
                    words.append(curr.lower())
                curr = ''
        
        if curr:
            words.append(curr.lower())
        
        c = Counter(words)
        
        print(c)
        
        ans = []
        
        for k, v in c.items():
            ans.append([v, k])
            
        ans.sort(reverse=True)
        
        idx = 0
        while idx < len(ans):
            if ans[idx][1] not in banned:
                return ans[idx][1]
            idx += 1
            
        return ''
        
        