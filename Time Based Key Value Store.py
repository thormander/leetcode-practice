class TimeMap:

    def __init__(self):
        self.map = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value,timestamp])

    def get(self, key:str, timestamp: int) -> str:

        pairs =  self.map.get(key,[]) # list   
        
        l = 0
        r = len(pairs) - 1
        val = ""
        
        while l <= r:
            mid = (l + r) // 2
            if pairs[mid][1] < timestamp:
                val = pairs[mid][0]
                l = mid + 1
            elif timestamp < pairs[mid][1]:
                r = mid - 1
            else:
                val = pairs[mid][0]
                break
        
        return val






    '''
    hashmap or dictionary --> key: 'key' | value: [value,timestamp]

    init:
        need to make the map
    set:
        if key is not there:
            need to make a new new item
        else:
            we just add on top of the existing key
    
    get:
        ascending order --> binary search
        do binary search on timestamp:
            no values == map[mid[1]]  // check if mid value = timestamp
             search left for closest value if
    '''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
