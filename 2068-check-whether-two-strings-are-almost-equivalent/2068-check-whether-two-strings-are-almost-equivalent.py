class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter([x for x in word1])
        c2 = Counter([x for x in word2])
        for x in 'qwertyuiopasdfghjklzxcvbnm':
            if abs(c1[x] - c2[x]) > 3:
                return False
        return True