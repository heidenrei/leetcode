class Solution:
    def countSegments(self, s: str) -> int:
        prev = None
        tmp = None
        cnt = 0
        for i in range(len(s)):
            
            if s[i] == ' ':
                if tmp:
                    cnt += 1
                tmp = None
            else:
                tmp = s[i]
        return cnt + 1 if tmp else cnt
                