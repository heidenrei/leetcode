class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 1:
            return n
        
        ans = 0
        n = str(n)
        N = len(n)
        # 13
        for i in range(len(n)):
            if i != 0:
                if n[i] == '1':
                    ans += int(n[:i]) * 10**(N-i-1) + 1
                    if n[i+1:]:
                        ans += int(n[i+1:])
                elif n[i] == '0':
                    ans += int(n[:i]) * 10**(N-i-1)
                else:
                     ans += int(n[:i]) * 10**(N-i-1) + 10**(N-i-1)
            else:
                if n[i] == '1':
                    ans += 1 + int(n[i+1:])
                else:
                     ans += 10**(N-i-1)
        return ans
        
        
                
                
