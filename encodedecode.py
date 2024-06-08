class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "_" + string

        return encoded
        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0 # initial index on length

        while i < len(s):
            j = i 
            while s[j] != "_":
                j += 1 # find our delimmiter

            length = int(s[i:j])
            output.append(s[j+1:j+1+length])

            i = j+1+length
        
        return output




'''
encode:
    know the count of how long the actual string is
    know the delimitter we are on is real

    Input: ["neet","code","love","you"]
    "123_neet4_code"
     i  j

decode:
    use that 'metadata' to decode, use of indexes

'''
