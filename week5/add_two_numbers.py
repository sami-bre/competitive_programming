# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sl1=0
        sl2=0
        
        L1 = l1
        L2 = l2
        while(l1):
            l1 = l1.next
            sl1 += 1
            
        while(l2):
            l2 = l2.next
            sl2 += 1
            
        if(sl1>=sl2):
            longerH = L1
            shorterH = L2
        else:
            longerH = L2
            shorterH = L1
            
        answer = longerH
            
        while(longerH):
            if shorterH:
                temp = longerH.val + shorterH.val
            else:
                temp = longerH.val
                
            if temp>9:
                longerH.val = temp-10
                if longerH.next:
                    longerH.next.val += 1
                else:
                    longerH.next = ListNode(val=1)
            else:
                longerH.val = temp
            
            if shorterH:
                shorterH = shorterH.next
            longerH = longerH.next
            
        return answer            