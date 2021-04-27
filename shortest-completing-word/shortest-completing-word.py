class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter([x.lower() for x in licensePlate if x.isalpha()])
        ans = []
        for word in words:
            word_c = Counter(word)
            ok = True
            for k, v in c.items():
                if word_c[k] < v:
                    ok = False
                    
            if ok:
                ans.append(word)
                    
        print(ans)  
        return sorted(ans, key=len)[0] if ans else ""
        
        