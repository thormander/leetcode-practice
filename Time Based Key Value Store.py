class TimeMap():

    #initialize
    def __init__(self):
        self.map = {}

    def set(self,key:str,value:str,timestamp:int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append([value,timestamp])
        

    def get(self,key:str,timestamp:int) -> str:
        # check if key actually exists
        if key not in self.map:
            return ""

        left = 0
        right = len(self.map[key]) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            # when to search right
            if self.map[key][mid][1] <= timestamp:
                left = mid + 1
                result = self.map[key][mid][0]
            else:
                right = mid - 1
            
        return result




            

'''
map key values
key       value
abc       [[val,1],[val,2],[val,3]]

time stamps are sorted essentially --> binary search
use the timestamps to determine whether we search left or right.
'''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
