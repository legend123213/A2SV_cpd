class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.arr.append(val)
        self.index[val] = len(self.arr)-1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        i = self.index[val]
        self.index[self.arr[-1]] = i
        self.arr[i] = self.arr[-1]
        self.index.pop(val)
        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)