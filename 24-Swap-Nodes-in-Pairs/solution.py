# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        while head != None and head.next != None:
            pt1 = head
            pt2 = head.next
            head = head.next.next
            curr.next = pt2
            pt2.next = pt1
            pt1.next = None
            curr = pt1
        curr.next = head
        return dummy.next