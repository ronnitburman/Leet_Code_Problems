# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # num = 0
        # temp = head
        # while temp:
        #     temp=temp.next
        #     num+=1
        
        # idx=num-n-1
        # num=0
        # res=ListNode()
        # root = res
        # while num<=idx:
        #     res.next=head
        #     res=res.next
        #     head = head.next
        #     num+=1
        # if head:
        #     res.next = head.next
        # return root.next

        dummy = ListNode(0,head)
        left=dummy
        right = head
        while n>0 and right:
            right = right.next
            n-=1
        
        while right:
            right=right.next
            left=left.next
        
        left.next = left.next.next
        
        return dummy.next