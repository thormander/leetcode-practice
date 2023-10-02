class Solution:
    def numDecodings(self, s: str) -> int:
        hashmap = {len(s):1}

        def DFS(index):
            # base cases
            if index in hashmap:
                return hashmap[index]
            elif s[index] == "0":
                return 0 # because ex. "06" is not valid
            
            result = DFS(index+1) # moving i

            # checking for double digit values
            if (index+1 < len(s)) and (s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456")):
                result += DFS(index+2)
            
            hashmap[index] = result

            return result
        
        return DFS(0)


            
