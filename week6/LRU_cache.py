class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.D = {}
        self.head = Node("HEAD","HEAD")
        self.tail = Node("TAIL","TAIL")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.D:
            return -1
        node = self.D[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.D:
            node = self.D[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(key, value)
            self.D[key] = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        if len(self.D) > self.capacity:
            #the node to be deleted
            node = self.tail.prev
            node.prev.next = self.tail
            node.next.prev = node.prev
            node.next, node.prev = None, None
            self.D.pop(node.key)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
