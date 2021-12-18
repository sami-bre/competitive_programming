class MyQueue:

    def __init__(self):
        self.main = []
        self.back = [] # the reversed version of the queue (a stack by itself)
        
        
    def push(self, x: int) -> None:
#         # copy the reverse of the main stack 
#         for i in range(len(self.main)):
#             self.back.append(self.main.pop())
            
#         self.back.append(x)
        
#         for i in range(len(self.back)):
#             self.main.append(self.back.pop())
        self.main.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.main)):
            self.back.append(self.main.pop())
            
        temp = self.back.pop()
        
        for i in range(len(self.back)):
            self.main.append(self.back.pop())
            
        return temp
        
        
    def peek(self) -> int:
        for i in range(len(self.main)):
            self.back.append(self.main.pop())
            
        temp = self.back[-1]
        
        for i in range(len(self.back)):
            self.main.append(self.back.pop())
            
        return temp
        
        

    def empty(self) -> bool:
        if(len(self.main) == 0):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()