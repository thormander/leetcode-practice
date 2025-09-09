class TimeMap:

    def __init__(self):
        self.my_dict = {} # key: key | value: [value,timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = []

        self.my_dict[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # is key even in there
        if key not in self.my_dict:
            return ""

        # do the binary search
        left = 0
        right = len(self.my_dict[key]) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            if self.my_dict[key][mid][1] <= timestamp:
                left = mid + 1
                result = self.my_dict[key][mid][0]
            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)  
