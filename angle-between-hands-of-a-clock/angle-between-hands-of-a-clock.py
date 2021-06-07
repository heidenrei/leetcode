class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        
        minute_hand = minutes/60*360
        hour_hand = hour/12*360 + minutes/60*30
                
        x = abs(hour_hand + (360 - minute_hand))
        y = abs(minute_hand + (360 - hour_hand))
        z = abs(minute_hand - hour_hand)
        return min([x, y, z])