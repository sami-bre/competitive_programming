# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
            
        if len(nodes) == 0:
            return None
        
        nodes.sort(key=lambda x:x.val)
                    
        for i in range(len(nodes)):
            if i == len(nodes)-1:
                nodes[i].next = None
                continue
            nodes[i].next = nodes[i+1]
            
        return nodes[0]