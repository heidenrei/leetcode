class Solution:
    def romanToInt(self, s: str) -> int:
        N = len(s)
        d = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        
        total = 0
        idx = 0
        while idx < N:
            curr = d[s[idx]]
            if idx + 1 < N and d[s[idx+1]] > curr:
                curr = d[s[idx+1]]
                curr -= d[s[idx]]
                total += curr
                idx += 2
            elif idx + 1 < N and d[s[idx+1]] == curr:
                tmp_idx = 0
                tmp = curr
                while idx + tmp_idx + 1 < N and d[s[idx+tmp_idx+1]] == curr:
                    tmp += curr
                    tmp_idx += 1
                total += tmp
                idx += tmp_idx + 1
            else:
                total += d[s[idx]]
                idx += 1
                
        return total