class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        s = [x for x in s]
        ans = 0
        curr = s[0]
        curr_cnt = 1
        prev_cnt = 0
        for i in range(1, N):
            if s[i] == curr:
                curr_cnt += 1
                if curr_cnt <= prev_cnt:
                    ans += 1
            else:
                prev_cnt = curr_cnt
                curr_cnt = 1
                curr = s[i]
                if curr_cnt <= prev_cnt:
                    ans += 1
                    
        return ans
