# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        if not head:
            return None
        while(head):
            nodes.append(head)
            head = head.next
        
        for node in nodes:
            node.next = None
            
        previous = nodes[0]
        for i in range(1, len(nodes)):
            if(nodes[i].val != previous.val):
                previous.next = nodes[i]
                previous = nodes[i]
                
        return nodes[0]
        