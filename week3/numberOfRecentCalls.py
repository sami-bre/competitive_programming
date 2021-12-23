class RecentCounter:

    def __init__(self):
        self.queue = []
        self.size = 0
        

    def ping(self, t: int) -> int:
        self.lately = t
        self.queue.append(t)
        self.size += 1
        while(t-self.queue[0] > 3000):
            self.queue.pop(0)
            self.size -= 1
            
        return self.size
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)