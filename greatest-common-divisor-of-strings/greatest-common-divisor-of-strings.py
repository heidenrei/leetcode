class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        strs = sorted([str1, str2], key=len)
        min_len = len(strs[0])
        
        for i in range(1, min_len+1)[::-1]:
            string = strs[0][:i]
            if strs[0].count(string) * i == len(strs[0]) and strs[1].count(string) * i == len(strs[1]):
                return string
        return ''