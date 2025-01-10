class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_hand = minutes * 6.0
        hour_hand = (hour + minutes/60)  * 30.0

        diff = minute_hand - hour_hand
        return min(abs(diff),360-abs(diff))

'''
360 degrees
each hour = 360/12 = 30 degrees per hour
each min = 360/60 = 6 degrees per min

for hour, need to normalize the minute hand --> hours
    - divide minutes to conver to hours and add that to our current hour
'''
