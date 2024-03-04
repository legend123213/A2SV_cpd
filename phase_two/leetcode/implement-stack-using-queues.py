from collections import deque
class MyStack:

    def __init__(self):
        self.de = deque()
    def push(self, x: int) -> None:
        self.de.append(x)
    def pop(self) -> int:
        return self.de.pop()
    def top(self) -> int:
        return self.de[-1]
    def empty(self) -> bool:
        return not bool(len(self.de))
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()