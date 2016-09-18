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
        When the first i rows are prefectly connected with their right node
        We only need to know the head of i'th row to populate next point for the i+1'th row
        """
        
        if root == None: return
        prevHead = root
        while prevHead != None:
            if prevHead.left == None:
                break
            node = prevHead
            while node != None:
                node.left.next = node.right
                if node.next != None:
                    node.right.next = node.next.left
                node = node.next
            prevHead = prevHead.left
            