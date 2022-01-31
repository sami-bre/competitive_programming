# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        size=0
        h = head
        while h:
            size += 1
            h = h.next
            
        stack = []
        counter = 0
        maxSum = 0
        
        while head:
            counter += 1
            if counter <= size/2:
                stack.append(head.val)
            else:
                temp = head.val + stack.pop()
                if temp > maxSum:
                    maxSum = temp
                    
            head = head.next
        
        return maxSum
        
        