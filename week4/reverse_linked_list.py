# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
            
        if len(nodes) == 0:
            return None
            
        nodes[0].next = None
        for i in range(1, len(nodes)):
            nodes[i].next = nodes[i-1]
            
        return nodes[-1]
            
        