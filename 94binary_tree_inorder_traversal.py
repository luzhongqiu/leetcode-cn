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
        if not root:
            return []
        res = []
        if root.left is not None:
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if root.right is not None:
            res.extend(self.inorderTraversal(root.right))
        return res
        