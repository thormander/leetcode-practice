class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + ":" + s

        return encoded_string

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []

        p1 = 0
        p2 = 0

        while p2 < len(s):
            if s[p2] == ":":
                # get length
                length = int(s[p1:p2])

                # add to result
                result.append(s[p2+1 : p2+1+length])

                # fix pointer positions
                p1 = p2+1+length
                p2 = p1
            
            p2 += 1
        
        print(result)
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

'''
special character --> out since it covers all valid ascii characters

encode:
    get the length of each string and store it so we know where the string ends

    say given ["Hello","World"]

    we return "5:Hello5:World"

decode:
    look for a number + :
    we know where to start counting

    "5:Hello5:World":
p1          |
p2           |
    
    if p2 == :
        get the length of the word
        add to our result --> string[p2+1 : p2+1+length]
        move pointers accordingly
            p1 = p2+1+length
            p2 = p1
    if it isnt, just keep increment p2
'''
