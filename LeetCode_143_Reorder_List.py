# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow.next
        prev=slow.next=None
        
        while curr:
            temp=curr.next
            curr.next = prev
            prev=curr
            curr = temp
            
        first,last = head,prev
            
        while last:
            temp1,temp2 = first.next, last.next
            first.next=last
            last.next=temp1
            first, last = temp1, temp2
        
            