class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        chars = ['M', 'CM', 'D','CD', 'C','XC', 'L','XL', 'X','IX', 'V','IV','I']
        nums = [1000, 900, 500,400, 100,90, 50,40, 10,9, 5,4, 1]

        idx = 0
        while num > 0:
            while num - nums[idx] >= 0:
                num -= nums[idx]
                ans += chars[idx]
                
            idx += 1
            
        return ans