class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        # get our header list
        header = ["Table"]

        for order in orders:
            for j in range(2,len(order)):
                # skip name and table number
                if order[j] not in header:
                    header.append(order[j])
        
        header[1:] = sorted(header[1:]) # sort everything except first index

        # fill our hashmap key is table; value is counts (IN ORDER)
        hashmap = {}

        for order in orders:
            tableNum = order[1]
            food = order[2]
            foodIndex = header.index(food) - 1 # -1 to account for the table in there

            if tableNum not in hashmap:
                hashmap[tableNum] = [0] * (len(header) - 1) # populate with 0s

            hashmap[tableNum][foodIndex] += 1
        
        # build our output
        result = [header] # first index is header

        for key in sorted(hashmap.keys(), key=int):
            row = [key] + list(map(str,hashmap[key]))
            result.append(row)

        return result






'''
reorganize the input
 - we ignore first index of nested list (we dont need customer name)

output:
row 1: headers [table,food1,food2,...]
row 2..n: actual data

hashmap --> key: table number | value: [counts of the food item]
 -> first initilize with empty list [0,0,0,0]
 -> based on header we need to increment depending on position
'''
