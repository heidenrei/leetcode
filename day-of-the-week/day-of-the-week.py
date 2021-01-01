class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # jan 1, 1971 was friday
        day_dict = {0: 'Friday', 1: 'Saturday', 2: 'Sunday', 3: 'Monday', 4: 'Tuesday', 5: 'Wednesday', 6: 'Thursday'}
        
        dt = (year-1968) // 4
        if (year - 1968) % 4 == 0 and (month == 1 or month == 2):
            dt -= 1
            
        if year == 2100:
            if month != 1 and month != 2:
                dt -= 1
        
        dt += (year - 1971)*365
        
        d = dict()
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        cnt = 0
        for i in range(13):
            cnt += months[i]
            d[i] = cnt
        
        dt += d[month-1]
        dt += day
        
        return day_dict[((dt-1) % 7)]
        
        
        
        
