class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict() # maintains insertion order
        self.max = capacity # make it accessible
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # need to move it to the front (as we jsut used it)
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1



    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            # update (doesn't need an eviction)
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # may need an eviction
            if len(self.cache) >= self.max:
                # pop from the front
                self.cache.popitem(last=False)
                
            self.cache[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
