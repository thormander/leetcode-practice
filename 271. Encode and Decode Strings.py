class Solution:

    def encode(self, strs: List[str]) -> str:
        # length + #
        encodedString = ""

        for string in strs:
            encodedString += str(len(string)) + "#" + string

        return encodedString


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0

        while i < len(s):
            if s[i] != "#":
                i += 1
                continue
            
            # we should be on the '#'
            length = int(s[j:i])
            j = i + length + 1

            # string split to grab individual string
            result.append(s[i+1:j])
            
            # update pointer past string we extracted
            i = j            

        return result
            
        

'''
list of strings -> string -> list of strings

encode:
    can easily just join the list and we will get the encoded

decode:
    where to split the strings?


["abc","bc"]

store length of string + some seperator 

3#abc2#bc
    |

string[i+1,i+3+1] = abc --> add this to a list

3#abc2#bc
     |
     |
'''
