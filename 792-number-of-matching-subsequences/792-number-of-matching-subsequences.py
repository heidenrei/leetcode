class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        ss = set([x for x in s])
        c = Counter(words)
        words = set(words)
        for w in words:
            if not set([x for x in w]).issubset(ss):
                continue
            si = 0
            wi = 0
            while si < len(s) and wi < len(w):
                if s[si] == w[wi]:
                    si += 1
                    wi += 1
                    if wi == len(w):
                        ans += c[w]
                else:
                    si += 1
                    
        return ans
            