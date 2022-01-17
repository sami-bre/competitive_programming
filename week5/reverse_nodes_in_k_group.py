# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes=[]
        while head:
            nodes.append(head)
            head = head.next
            
        l = len(nodes)     # length nodes list
        b = len(nodes)//k # number of bundles
        s=0 # the start
        
        for i in range(b):
            if i==0:
                nodes[s:s+k] = nodes[s+k-1::-1]
            else:
                nodes[s:s+k] = nodes[s+k-1:s-1:-1]
            s += k
            
        for i in range(l):
            if i == l-1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
        
        return nodes[0]