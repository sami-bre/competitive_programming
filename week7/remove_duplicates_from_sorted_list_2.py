# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cap = ListNode(val="START", next=head)
        bp = cap
        fp = head
        
        if head and head.next and head.val == head.next.val:
            cap.next = None
        
        while(fp):
            if (not fp.next) or fp.val != fp.next.val:
                bp.next = fp
                bp = fp
                fp = fp.next
                bp.next = None
            else:
                v = fp.val
                while fp and v == fp.val:
                    prev = fp
                    fp = fp.next
                    prev.next = None
        return cap.next
                    
            
        