class LFUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.size = 0
        self.start = HeadNode('START', None)
        self.end = HeadNode('END', None)
        self.start.next, self.end.prev = self.end, self.start
        self.dataNodeDict = {}
        self.headNodeDict = {}
        

    def get(self, key: int) -> int:
        if not (key in self.dataNodeDict):
            return -1
        
        node = self.dataNodeDict[key]
        self.moveNodeToNextFreqBranch(node)
        return node.val
        
        

    def put(self, key: int, value: int) -> None:
        if self.limit == 0:
            return None
        
        if key in self.dataNodeDict:
            node = self.dataNodeDict[key]
            node.val = value
            self.moveNodeToNextFreqBranch(node)
            return None
        
        node = DataNode(key, value, 1)
        self.dataNodeDict[key] = node
        
        # if size already equals limit, remove the last data-node from the last branch
        if self.size == self.limit:
            # tail = self.headNodeDict[1][1]
            tail = self.headNodeDict[self.end.prev.freq][1]
            deadNode = tail.up
            top = deadNode.up
            top.down = tail
            tail.up = top
            deadNode.up, deadNode.down = None, None

            k = deadNode.key
            self.dataNodeDict.pop(k)
            
            self.size -= 1
        
        # if no freq-1-branch head, create it.
        if not (1 in self.headNodeDict):
            head = HeadNode('HEAD', 1)
            tail = TailNode('TAIL')
            head.down, tail.up = tail, head
            right = self.end
            left = right.prev
            left.next = head
            right.prev = head
            head.next = right
            head.prev = left
            
            self.headNodeDict[1] = (head, tail)
            
        # link the node to the freq-1-head
        top = self.headNodeDict[1][0]
        bottom = top.down
        top.down = node
        bottom.up = node
        node.up = top
        node.down = bottom
        
        self.size += 1
        
        
    def moveNodeToNextFreqBranch(self, node):
        branchHead = self.headNodeDict[node.freq][0]
        freq = node.freq
        nextFreq = freq+1
        
        # make sure a head with the next freq exists
        if not (nextFreq in self.headNodeDict):
            newHead = HeadNode('HEAD', nextFreq)
            left = branchHead.prev
            right = branchHead
            right.prev = newHead
            left.next = newHead
            newHead.next = right
            newHead.prev = left
            newHead.down = TailNode('TAIL')
            newHead.down.up = newHead
            
            self.headNodeDict[nextFreq] = (newHead, newHead.down)
        
        #break previous links of the node
        top = node.up
        bottom = node.down
        top.down = bottom
        bottom.up = top
        
        #if the branch is empity, remove the branch
        if top.val == 'HEAD' and bottom.val == 'TAIL':
            left = top.prev
            right = top.next
            left.next = right
            right.prev = left
            top.next = None
            top.prev = None
            self.headNodeDict.pop(top.freq)
            
        #link the node to the next-freq-head
        nfh = self.headNodeDict[nextFreq][0]
        node.freq += 1
        bottom = nfh.down
        nfh.down = node
        bottom.up = node
        node.up = nfh
        node.down = bottom
        
        
        
    def reveal(self):
        head = self.start.next
        while head.val != 'END':
            print(f'freq-{head.freq} branch: ', end='')
            dnode = head.down
            while dnode.val != 'TAIL':
                print(f'{dnode.val} ', end='')
                dnode = dnode.down
            head = head.next
            print()
        print(f'------------- size: {self.size}')
            
            
        
        
        
        
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, val):
        self.val = val
        
class HeadNode(Node):
    def __init__(self, val, freq):
        super().__init__(val)
        self.next = None
        self.prev = None
        self.down = None
        self.freq = freq
        
class TailNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.up = None

class DataNode(Node):
    def __init__(self, key, val, freq):
        super().__init__(val)
        self.key = key
        self.freq = freq
        self.up = None
        self.down = None