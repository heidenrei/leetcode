class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        print(number)
        ans = ''
        while len(number) > 4:
            ans += number[:3] + '-'
            number = number[3:]
        
        
        
        if not number:
            return ans[:-1]
        if len(number) == 2 or len(number) == 3:
            ans += number
            
        if len(number) == 4:
            ans += number[:2] + '-' + number[2:]
            
        return ans
