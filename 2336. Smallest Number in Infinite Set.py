class SmallestInfiniteSet:

    def __init__(self):
        self.my_set = []
        self.check_inside = set()
        for i in range(1,1001):
            self.my_set.append(i)
            self.check_inside.add(i)
        heapq.heapify(self.my_set)
        

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.my_set)
        self.check_inside.remove(smallest)
        return smallest

        

    def addBack(self, num: int) -> None:
        if num not in self.check_inside:
            heapq.heappush(self.my_set,num)
            self.check_inside.add(num)
        

        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
