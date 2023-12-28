from collections import Counter, defaultdict
class FrequencyTracker:

    def __init__(self):
        self.f = Counter()
        self.g = Counter()
        

    def add(self, number: int) -> None:
        self.f[number] += 1
        self.g[self.f[number]] += 1
        self.g[self.f[number] - 1] -= 1
        

    def deleteOne(self, number: int) -> None:
        if self.f[number]:
            self.f[number] -= 1
            if self.f[number] == 0: 
                del self.f[number]
            self.g[self.f[number]] += 1
            self.g[self.f[number] + 1] -= 1 
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.g[frequency] > 0
                
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)