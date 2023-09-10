class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key:int) -> int:
        # if key exists return value, else -1
        if key in self.cache:
            # move accessed key to back (for ordering) where front is least used
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key:int, value:int) -> None:
        if key in self.cache:
            self.cache[key] = value # update if key exists
            self.cache.move_to_end(key)
        elif len(self.cache) < self.capacity:
            # add to cache
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # cache full
            self.cache.popitem(last = False) # pop at front of cache
            # add to cache
            self.cache[key] = value
            self.cache.move_to_end(key)


            
# USED --> basically anytime it is touched or created        
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
