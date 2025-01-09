class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.randomHelp = []
        
    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.randomHelp)
            self.randomHelp.append(val)
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        else:
            index_to_remove = self.hashmap[val]
            last_value = self.randomHelp[-1]

            self.randomHelp[index_to_remove] = last_value # reassign value
            self.randomHelp.pop() # pop end
            self.hashmap[last_value] = index_to_remove # fix index in map as we moved end value
            del self.hashmap[val]
            
            return True
        
    def getRandom(self) -> int:
        return random.choice(self.randomHelp)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
'''
instead of a set, use a map

key: value | value: index in our randomHelp list

[]

{1:0} -insert to map
[1]   -insert to list
'''
