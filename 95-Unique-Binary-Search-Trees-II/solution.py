# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return [] if n == 0 else self.sub(1, n)
        
    def sub(self, start, end):
        if start > end: return [None]
        if start == end: return [TreeNode(start)]
        
        lst = []
        for mid in xrange(start, end + 1):
            leftLst = self.sub(start, mid - 1)
            rightLst = self.sub(mid + 1, end)
            for leftTree in leftLst:
                for rightTree in rightLst:
                    midNode = TreeNode(mid)
                    midNode.left = leftTree
                    midNode.right = rightTree
                    lst.append(midNode)
        return lst
                    