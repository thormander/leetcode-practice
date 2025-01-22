class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # minute hand
        degree_minhand = 6 * minutes
        # hour hand
        degree_hourhand = 30 * hour + (minutes / 60) * 30

        difference = degree_hourhand - degree_minhand

        return min(abs(difference),360-abs(difference))


'''
could be float values

use 12 as starting point

hour = 12, minutes = 30

minute hand degrees
    - 360 / 60 = 6 degrees per min --> 6 * minutes or 6 * 30 = 180

hour hand (we want to normalize it to minutes to hour)
    - 360 / 12 = 30 degrees per hour -->  30min/60min = 1/2 an hour * 30 degrees per hour 

min(360 - | degree from hour hand - degrees from minute |, | degree from hour hand - degrees from minute |)

'''
