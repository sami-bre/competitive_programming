# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
        
        if(n==1 and len(nodes)>1):
            nodes[-2].next = None
        elif(n==1):
            return None
        elif(n==len(nodes)):
            nodes[0].next = None
            return nodes[1]
        else:
            nodes[-(n+1)].next = nodes[-(n-1)]
        return nodes[0]
        