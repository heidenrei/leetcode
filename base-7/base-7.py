class Solution:
    def convertToBase7(self, num: int) -> str:
        is_neg = num < 0
        num = abs(num)
        ans = ''
        
        power = 1
        while 7**power <= num:
            power += 1
            
        power -= 1
        
        while power:
            print(num, power)
            tmp = num // 7**power
            ans += str(tmp)
            num -= (7**power*tmp)
            power -= 1
        
        ans += str(num)
        
        return ans if not is_neg else str(-1*int(ans))