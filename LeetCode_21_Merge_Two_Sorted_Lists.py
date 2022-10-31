# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() #initiating a dummy node
        ll = dummy
        
        while list2 and list1:
            if list1.val < list2.val:
                ll.next = list1
                list1 = list1.next
            else:
                ll.next = list2
                list2= list2.next
            ll = ll.next
        if list1:
            ll.next = list1
        elif list2:
            ll.next = list2
        
        return dummy.next