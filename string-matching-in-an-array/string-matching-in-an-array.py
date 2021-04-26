class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        words.sort(key=len)
        N = len(words)
        for i in range(N):
            for j in range(i):
                if words[j] in words[i]:
                    ans.add(words[j])
                    
        return list(ans)