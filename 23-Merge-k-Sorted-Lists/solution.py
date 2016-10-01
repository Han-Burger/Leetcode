# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0:
            return None
        elif k == 1: 
            return lists[0]
        elif k == 2:
            return self.merge2Lists(lists[0], lists[1])
        else:
            return self.merge2Lists(self.mergeKLists(lists[: k / 2]), self.mergeKLists(lists[k / 2:]))
        
        
    def merge2Lists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        tmpHead = ListNode(0)
        curr = tmpHead
        curr1 = l1
        curr2 = l2
        while curr1 != None or curr2 != None:
            if curr1 == None:
                curr.next = curr2
                break
            if curr2 == None:
                curr.next = curr1
                break
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
            curr.next = None
        return tmpHead.next
        
        
            