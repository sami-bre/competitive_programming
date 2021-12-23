class MyCircularDeque:
    

    def __init__(self, k: int):
        self.f = []
        self.b = []
        self.size = 0
        self.max_size = k
    
    # two utility functions
    def f_give_rear(self, pop):
        for i in range(len(self.f)-1):
            self.f.append(self.f.pop(0))
        temp = self.f.pop(0)
        if(pop):
            return temp
        else:
            self.f.append(temp)
            return temp
        
    def b_give_rear(self, pop):
        r = self.b
        for i in range(len(self.b)-1):
            self.b.append(self.b.pop(0))
        temp = self.b.pop(0)
        if(pop):
            return temp
        else:
            self.b.append(temp)
            return temp
        
    ##############################################
    def insertFront(self, value: int) -> bool:
        if(self.size < self.max_size):
            self.f.append(value)
            self.size += 1
            return True
        else:
            return False
        
        
        

    def insertLast(self, value: int) -> bool:
        if(self.size < self.max_size):
            self.b.append(value)
            self.size += 1
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if(self.f):
            self.f_give_rear(True)
            self.size -= 1
            return True
        elif(self.b):
            self.b.pop(0)
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if(self.b):
            self.b_give_rear(True)
            self.size -= 1
            return True
        elif(self.f):
            self.f.pop(0)
            self.size -= 1
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if(self.f):
            return self.f_give_rear(False)
        elif(self.b):
            return self.b[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if(self.b):
            return self.b_give_rear(False)
        elif(self.f):
            return self.f[0]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if(self.size == 0):
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if(self.size == self.max_size):
            return True
        else:
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