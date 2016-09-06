# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        # copy the node and paste them right next to the original code
        ptr = head
        while ptr is not None:
            newNode = RandomListNode(ptr.label)
            newNode.next = ptr.next
            ptr.next = newNode
            ptr = ptr.next.next
        
        # assgin the corresponding random nodes to the new nodes
        ptr = head
        while ptr is not None:
            if ptr.random is not None:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        
        #split the original list with the new list
        pseudohead = RandomListNode(0)
        ptr1, ptr2 = head, pseudohead
        while ptr1 is not None:
            ptr2.next = ptr1.next
            ptr1.next = ptr1.next.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return pseudohead.next