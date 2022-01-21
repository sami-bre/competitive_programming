# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
            
        nodes2 = nodes.copy()
        nodes2.reverse()
        print(nodes2)
        if nodes == nodes2:
            return True
        else:
            return False