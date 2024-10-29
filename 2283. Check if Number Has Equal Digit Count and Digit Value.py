class Solution:
    def digitCount(self, num: str) -> bool:
        hashmap = {} # key: index | value: counts/occurances

        # get counts
        # note - char is type str
        for char in num:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        # loop through num again
        for i,v in enumerate(num):
            # case where a index/digit is 0 so we skip
            if str(i) not in hashmap and v == '0':
                continue

            if v != str(hashmap.get(str(i),0)):
                return False
        
        return True


    


'''
We want:
    true --> if every index i in num; digit i occurs num[i] times

i must occur num[i] times (think of value is the occurance we want)

loop through and..
make a hashmap:
    - key = digit/index
    - value = occurances in num

loop through once more, and check if the value == occurance we found in our hashmap
    - if we get through it reutrn true
    - otherwise just reutrn false
'''
        
