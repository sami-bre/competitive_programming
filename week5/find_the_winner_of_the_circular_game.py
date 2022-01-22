class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        if n==1:
            return 1
        
        nl = [Node(val=x) for x in range(1,n+1)]
        nl[0].prev = nl[-1]
        nl[0].next = nl[1]
        nl[-1].prev = nl[-2]
        nl[-1].next = nl[0]
        for i in range(1,len(nl)-1):
            nl[i].prev = nl[i-1]
            nl[i].next = nl[i+1]
            
        current = nl[0]
        
        # print(nl)
        
        while current.next != current:
            for i in range(k-1):
                current = current.next
            
            current.prev.next = current.next
            current.next.prev = current.prev
            temp = current.next
            current.next = None
            current.prev = None
            current = temp
                
        return current.val
            
        
        

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
        
        