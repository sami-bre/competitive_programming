class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.max_size = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if(self.size < self.max_size):
            self.deque.insert(0, value)
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if(self.size < self.max_size):
            self.deque.append(value)
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if(self.size > 0):
            self.deque.pop(0)
            self.size -= 1
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if(self.size > 0):
            self.deque.pop()
            self.size -= 1
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if(self.size > 0):
            return self.deque[0]
        return -1
        

    def getRear(self) -> int:
        if(self.size > 0):
            return self.deque[-1]
        else:
            return -1
            
        

    def isEmpty(self) -> bool:
        if(self.size == 0):
            return True
        return False
        

    def isFull(self) -> bool:
        if(self.size == self.max_size):
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()