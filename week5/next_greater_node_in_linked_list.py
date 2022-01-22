# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[listNode]) -> list[int]:
        vals = []
        stack = []
        while(head):
            vals.append(head.val)
            head = head.next
            
        print(vals)
        
        answer = [0 for i in range(len(vals))]
        
        for i in range(len(vals)):
            if i==0:
                stack.append((vals[i], i))
                continue
                
            if vals[i] <= stack[-1][0]:
                stack.append((vals[i], i))
            else:
                while(len(stack)>0 and vals[i]>stack[-1][0]):
                    temp = stack.pop()
                    answer[temp[1]] = vals[i]
                stack.append((vals[i], i))
                    
        return answer
        