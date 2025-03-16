# 938. Range Sum of BST


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """

        def recur(node, low, high):
            if node is None:
                return 0
            if low > node.val:
                return recur(node.right, low, high)
            if high < node.val:
                return recur(node.left, low, high)
            return node.val + recur(node.right, low, high) + recur(node.left, low, high)

        return recur(root, low, right)

