class MyStack:

    def __init__(self):
        self.Qr = []
        

    def push(self, x: int) -> None:
        self.Qr.append(x)
        for i in range(len(self.Qr) - 1):
            self.Qr.append(self.Qr.pop(0))
        

    def pop(self) -> int:
        return self.Qr.pop(0)

    def top(self) -> int:
        return self.Qr[0]
        

    def empty(self) -> bool:
        if(len(self.Qr) == 0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()