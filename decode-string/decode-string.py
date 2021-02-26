class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        ans = ''
        idx = 0
        while idx < N:
            if s[idx].isalpha():
                ans += s[idx]
                idx += 1
            else:
                # need to find where the closing bracket is
                num = ''
                while s[idx].isnumeric():
                    num += s[idx]
                    idx += 1
                stack = 1
                tmp_idx = idx + 1
                tmp_string = ''
                while stack >= 1:
                    if s[tmp_idx] == '[':
                        stack += 1
                        tmp_string += '['
                        tmp_idx += 1
                    elif s[tmp_idx] == ']':
                        stack -= 1
                        if stack == 0:
                            break
                        else:
                            tmp_string += ']'
                        tmp_idx += 1
                    else:
                        tmp_string += s[tmp_idx]
                        tmp_idx += 1
                            
                
                ans += int(num)*self.decodeString(tmp_string)
                idx = tmp_idx+1
        
        return ans