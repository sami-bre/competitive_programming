class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.ordered.append(val)
        self.ordered.sort()

    def pop(self) -> None:
        temp = self.stack.pop()
        self.ordered.remove(temp)
        return temp
    
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ordered[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()