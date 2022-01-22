# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
        
        for j in range(0,len(nodes)//2):
            i = 2*j
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
            
        for i in range(len(nodes)):
            if i == len(nodes)-1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
                
        return nodes[0]
            
        