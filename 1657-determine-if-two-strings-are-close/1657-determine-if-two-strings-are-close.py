class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2)