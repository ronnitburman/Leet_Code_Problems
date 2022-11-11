# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        ll = temp = l1
        
        while l1 and l2:
            temp=l1
            temp.val=l1.val+l2.val+carry
            carry = temp.val//10
            temp.val = temp.val%10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            temp=l1
            temp.val=l1.val + carry
            carry = temp.val//10
            temp.val = temp.val%10
            l1=l1.next
        
        while l2:
            temp.next=l2
            temp=temp.next
            temp.val=l2.val + carry
            carry = temp.val//10
            temp.val = temp.val%10
            l2=l2.next
            
        if carry == 1:
            temp.next=ListNode()
            temp.next.val = 1
        return ll
           