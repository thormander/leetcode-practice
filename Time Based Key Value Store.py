class TimeMap():

    def __init__(self):
        self.myDict = {}
    
    def set(self,key:str,value:str,timestamp:int) -> None:
        if key not in self.myDict:
            self.myDict[key] = []
        
        self.myDict[key].append([value,timestamp])
    
    def get(self,key:str,timestamp:int) -> str:

        if key not in self.myDict:
            return ""

        left = 0
        right = len(self.myDict[key]) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            # move right
            if self.myDict[key][mid][1] <= timestamp:
                left = mid + 1
                result = self.myDict[key][mid][0]
            else:
                # move left
                right = mid - 1
        
        return result
            
            
        


'''
[(a,1),(a,2),(b,3)]
'''




        
