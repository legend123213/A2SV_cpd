class RecentCounter:

    def __init__(self):
        self.ls = []
        self.ptr = 0
        
        

    def ping(self, t: int) -> int:
        self.ls.append(t)
        ptr = self.ptr
        for i in range(ptr,len(self.ls)):
            if self.ls[-1] - self.ls[i]>3000:
                self.ptr=i+1
        return len(self.ls[self.ptr::])    


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)