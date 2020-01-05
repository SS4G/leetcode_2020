class RecentCounter:

    def __init__(self):
        self.buffer = []      
        self.earlyIdx = 0
        self.latestIdx = 0
    
    def ping(self, t: int) -> int:
        self.buffer.append(t)
        self.latestIdx += 1
        #self.latestIdx %= 10000
        while self.buffer[self.earlyIdx] < t - 3000:
            self.earlyIdx += 1
        return self.latestIdx - self.earlyIdx



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)