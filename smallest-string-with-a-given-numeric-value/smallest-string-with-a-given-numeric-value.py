class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        d = defaultdict(int)
        
        for i in range(26):
            d[chr(ord('a')+i)] = i + 1
        
        ans = ''
        remaining_chars = n
        remaining_value = k
        
        while remaining_value < 26*remaining_chars:
            if (len(ans) + 1) + 26*(remaining_chars-1) < k:
                ans += chr(ord('a') + (k - 26*(remaining_chars-1) - len(ans))-1)
                ans += 'z' * (n - len(ans))
                return ans
            else:
                ans += 'a'
            remaining_value -= 1
            remaining_chars -= 1
            
        return ans + 'z'*(n-len(ans))