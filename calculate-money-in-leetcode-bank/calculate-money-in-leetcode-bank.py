class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        curr = 1
        day = 1
        prev = 1
        for i in range(n):
            if day == 7:
                day = 1
                ans += curr
                curr = prev + 1
                prev = curr

            else:
                day += 1
                ans += curr
                curr += 1


                
        return ans