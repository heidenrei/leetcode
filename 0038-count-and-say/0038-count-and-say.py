class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n-1):
            prev = result
            result = ''
            j = 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j += 1
                while j < len(prev) and prev[j] == cur:
                    cnt += 1
                    j += 1
                result += str(cnt) + str(cur)
        return result