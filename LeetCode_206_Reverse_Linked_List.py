#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #intializing two pointers curr and head
        curr = head
        prev = None
        while curr: #looping until curr becomes None
            temp = curr.next #temporarily storing the link to the next node before breaking it
            curr.next = prev#reversing the direction
            #updating pointers for next iteration
            prev = curr 
            curr = temp
        return prev 
#returning prev since it'll be the last node of the linked list which becomes first node of the reversed linked list  
