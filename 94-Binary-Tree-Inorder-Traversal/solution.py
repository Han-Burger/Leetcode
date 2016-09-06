# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iteratively(root)
        
    def iteratively(self, root):
        l = []
        m = set()
        s = []
        s.append(root)
        round = 0
        while len(s) > 0:
            round += 1
            node = s.pop()
            if node != None:
                if node not in m:
                    s.append(node.right)
                    s.append(node)
                    s.append(node.left)
                    m.add(node)
                else:
                    l.append(node.val)
        return l
                
    def recursively(self, root):
        if root is None: return []
        return self.recursively(root.left) + [root.val] + self.recursively(root.right)