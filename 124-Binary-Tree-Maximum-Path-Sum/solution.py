# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
        
    def dfs(self, node):
        if node == None: return float('-inf')
        leftRes = self.dfs(node.left)
        rightRes = self.dfs(node.right)
        leftVal = max(0, 0 if node.left == None else node.left.val)
        rightVal = max(0, 0 if node.right == None else node.right.val)
        res = leftVal + rightVal + node.val
        node.val += max([0, leftVal, rightVal])
        return max(leftRes, rightRes, res)
                         
        