class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        words = set(words)
        N = len(text)
        ans = []
        for i in range(1, N+1):
            for j in range(i):
                if text[j:i] in words:
                    ans.append([j, i-1])
        return sorted(ans)