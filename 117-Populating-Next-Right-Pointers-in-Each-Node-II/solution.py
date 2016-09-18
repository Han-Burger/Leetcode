# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        """
        similar to 'Populating Next Right Pointers in Each Node I'
        Except that we cannot assume that the node exist.
        """
        
        if root == None: return
        prevHead = root
        while prevHead != None:
            prevNode = prevHead
            currHead = None
            curr = None
            while prevNode != None:
                for node in [prevNode.left, prevNode.right]:
                    if node != None:
                        if curr != None:
                            curr.next = node
                        else:
                            currHead = node
                        curr = node
                prevNode = prevNode.next
            prevHead = currHead