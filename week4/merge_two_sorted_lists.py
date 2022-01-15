# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = []
        ll2 = []
        combined = []
        
        while(list1):
            ll1.append(list1)
            list1 = list1.next
            
        while(list2):
            ll2.append(list2)
            list2 = list2.next
            
        # merge sort
        while(len(ll1) and len(ll2)):
            if(ll1[0].val <= ll2[0].val):
                combined.append(ll1.pop(0))
            else:
                combined.append(ll2.pop(0))
        
        if(len(ll1)):
            for item in ll1:
                combined.append(item)
        
        if(len(ll2)):
            for item in ll2:
                combined.append(item)
                
        for i in range(len(combined)):
            if(i == len(combined)-1):   # the last node case
                combined[i].next = None
                break
            combined[i].next = combined[i+1]
            
        if(combined):
            return combined[0]
        return None
            
                
            
        