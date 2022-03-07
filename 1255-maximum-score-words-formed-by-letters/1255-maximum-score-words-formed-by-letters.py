class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        N = len(words)
        M = len(letters)
        
        def get_score(i):
            ans = 0
            for ch in words[i]:
                ans += score[ord(ch) - ord('a')]
                
            return ans
        
        
        @cache
        def go(wbm, lbm):
            ans = 0
            d = defaultdict(list)
            for j in range(M):
                if not lbm & (1<<j):
                    d[letters[j]].append(j)
            for i in range(N):
                if not wbm & (1<<i):
                    c = Counter(words[i])
                    good = True
                    for k, v in c.items():
                        if v > len(d[k]):
                            good = False
                            break
                    if good:
                        tmpbm = lbm
                        for k, v in c.items():
                            for dv in range(v):
                                tmpbm |= 1<<d[k][dv]
                        tmp = go(wbm | (1<<i), tmpbm) + get_score(i)
                        if tmp > ans:
                            ans = tmp
                            
            return ans
        
        return go(0, 0)