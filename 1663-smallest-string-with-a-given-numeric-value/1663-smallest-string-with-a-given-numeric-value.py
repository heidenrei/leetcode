class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == k:
            return 'a'*n
        ans = ''
        while k-1 < (n-len(ans)-1)*26:
            ans += 'a'
            k -= 1
        neededzs = n - len(ans) - 1
        k -= neededzs * 26
        ans += chr(ord('a') + k - 1)
        ans += 'z'*neededzs
        return ans
        