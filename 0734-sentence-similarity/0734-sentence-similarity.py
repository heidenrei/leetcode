class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        d = defaultdict(set)
        for x, y in similarPairs:
            d[x].add(y)
            d[y].add(x)
            d[x].add(x)
            d[y].add(y)
            
        N = len(sentence1)
        M = len(sentence2)
        if N != M:
            return False
        for i in range(N):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence2[i] not in d[sentence1[i]]:
                return False
        return True