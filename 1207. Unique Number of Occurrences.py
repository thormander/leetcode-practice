class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {} # key: number | value: occurance

        # get counts
        for num in arr:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # scan occurances, if we have a same value return false
        hashset = set()
        for occ in hashmap.values():
            if occ in hashset:
                return False
            hashset.add(occ)
        
        return True



'''
the occurances must be different
 - we need to keep track of counts

hashmap = {number : occurance}

scan through the values of hashmap, and make sure none are same
    - use a set for that

'''
