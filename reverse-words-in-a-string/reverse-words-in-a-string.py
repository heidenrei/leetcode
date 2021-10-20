class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x.strip().lstrip() for x in s.strip().lstrip().split(' ') if x != ''][::-1])