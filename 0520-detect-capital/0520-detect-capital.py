class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all(x.isupper() for x in word) or all (x.islower() for x in word[1:])