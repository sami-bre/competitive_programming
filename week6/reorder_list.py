# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        
        while(head):
            nodes.append(head)
            head = head.next
            
        for item in nodes:
            item.next = None
            
        odd = len(nodes)%2 != 0
        
        for i in range(1, len(nodes)//2 + 1):
            nodes[i-1].next = nodes[-i]
            if i!=len(nodes)//2 or odd:
                nodes[-i].next = nodes[i]