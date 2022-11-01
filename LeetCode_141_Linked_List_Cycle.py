# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        #if there is a loop then the fast and slow pointer will meet again
        while fast and fast.next: #if fast.next is None then there is no loop
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False