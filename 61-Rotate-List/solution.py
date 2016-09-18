# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        n = 0
        currNode = head
        tailNode = head
        while currNode:
            n += 1
            if not currNode.next: tailNode = currNode
            currNode = currNode.next
        
        k %= n
        if k == 0: return head
        
        newTail = head
        for i in xrange(n - k - 1):
            newTail = newTail.next
            
        newHead = newTail.next
        newTail.next = None
        tailNode.next = head
        return newHead
        
            