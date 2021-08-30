class Solution:
    def dayOfYear(self, date: str) -> int:
        d = [0, 31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
        
        for i in range(1, 12):
            d[i] = d[i-1] + d[i]
        
        date = date.split('-')
        
        is_leap_year = int(date[0]) % 4 == 0# and int(date[0]) % 400 != 0
        
        is_leap_year &= int(date[1]) > 2 | (int(date[1]) == 2 & int(date[2]) == 29)
        
        
        return d[int(date[1])-1] + int(date[2]) + is_leap_year
        
        
        