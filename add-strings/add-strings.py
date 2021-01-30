class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = 0
        for i in range(len(num1)):
            ans += 10 ** (len(num1)-i-1) * int(num1[i])
            
        for i in range(len(num2)):
            ans += 10 ** (len(num2)-i-1) * int(num2[i])
            
        return str(ans)