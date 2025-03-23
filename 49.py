# 101. Symmetric Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if root is None:
            return True

        left_root = root.left
        right_root = root.right

        def check(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            if left_node is None:
                return False
            if right_node is None:
                return False
            if left_node.val != right_node.val:
                return False
            return check(left_node.left, right_node.right) and check(left_node.right, right_node.left)

        return check(left_root, right_root)