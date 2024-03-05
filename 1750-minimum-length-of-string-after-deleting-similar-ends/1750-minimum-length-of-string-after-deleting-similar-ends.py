class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 2 and s[0] == s[-1]:
            curr_ch = s[0]
            curr_len = len(s)
            head_idx = 0
            tail_idx = curr_len - 1
            
            while head_idx < curr_len and s[head_idx] == curr_ch:
                head_idx += 1
            head_idx -= 1
            
            while tail_idx >= 0 and s[tail_idx] == curr_ch:
                tail_idx -= 1
            tail_idx += 1
            
            if not tail_idx > head_idx:
                return 0
            
            s = s[head_idx+1:tail_idx]
        
        if len(s) > 1 and len(set(s)) == 1:
            return 0
        
        return len(s)