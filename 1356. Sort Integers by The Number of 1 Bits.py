class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:



        listPairs = [] # store pairs (integer : count)

        for num in arr:
            binary = bin(num) # returns string
            
            # get occurances of 1 in each binary    
            count = 0
            for char in binary:
                if char == '1':
                    count += 1
                else:
                    continue
            
            listPairs.append((num,count))

        listPairs = sorted(listPairs,key=lambda x: (x[1],x[0]))

        result = []
        for pair in listPairs:
            result.append(pair[0])
        return result


'''
convert to binary representation
bin() can convet int -> binary
int(_,2) convert binary -> int

1. sort based on bits

2. sort based on number (if same bits)

list of lists
combine after we are done

'''

