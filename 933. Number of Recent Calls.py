class RecentCounter:

    def __init__(self):
        self.recent = deque() # store pings within 3000 ms


    def ping(self, t: int) -> int:
        self.recent.append(t)

        # make sure everythin in recent is within 3000 of just added ping
        while self.recent[0] < (t-3000):
            self.recent.popleft()
        
        return len(self.recent)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
