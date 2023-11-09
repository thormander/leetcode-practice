class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        result = []
        hashmap = {} # char : index of last occurance

        # first pass -> fill map
        for i in range(len(s)):
            hashmap[s[i]] = i

        # second pass -> paritions
        end = 0
        p_size = 0
        for i in range(len(s)):
            p_size += 1
            end = max(end,hashmap[s[i]]) # update end to last occurance of current letter
            
            # case of partition found
            if i == end:
                result.append(p_size)
                p_size = 0
        
        return result


        '''
        map of char to last occurance

        iterate through again and record size. if at any point our size passes last occurance, we can add that to output
        '''  
