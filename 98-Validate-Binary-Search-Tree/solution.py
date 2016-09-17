# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)
        
    def isValid(self, root, lowerBound, upperBound):
        if root == None: return True
        if lowerBound is not None and root.val <= lowerBound: return False
        if upperBound is not None and root.val >= upperBound: return False
        
        return self.isValid(root.left, lowerBound, root.val) and self.isValid(root.right, root.val, upperBound)