class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last1 = -inf
        last2 = -inf
        best = inf
        if word1 == word2:
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    tmp = i - last1
                    if tmp < best:
                        best = tmp
                    last1 = i
        else:
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    tmp = i - last2
                    if tmp < best:
                        best = tmp
                    last1 = i
                if wordsDict[i] == word2:
                    tmp = i - last1
                    if tmp < best:
                        best = tmp
                    last2 = i
        return best