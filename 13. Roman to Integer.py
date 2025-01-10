class Solution:
    def romanToInt(self, s: str) -> int:
        # fill map
        # key: symbol | value: value
        conversion_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        lag = "I" # initially set to smallest numeral
        result = 0
        for i in range(len(s)-1,-1,-1):
        
            if conversion_map[lag] > conversion_map[s[i]]:
                # case where we subtract
                result -= conversion_map[s[i]]
            else:
                # case where we add
                result += conversion_map[s[i]]
            
            lag = s[i]
        
        return result






'''
running result wehere we keep appending to it

hashmap to store conversion table

if we go in reverse:
running lag, where we track previous numeral:
    if that numeral is less than current

"MCMXCIV"
       |

result = 5
lag = V

since I < V, subtract
result = 4

lag = I
result = 104

lag = C
result = 94

lag = X
result = 1094

lag = M
result = 994

1994

'''
