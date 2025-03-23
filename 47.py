# 98. Validate Binary Search Tree

from math import inf

# Definition for a binary tree node.

okay = True
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        global okay
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        okay = True

        def dfs(node, left_side, right_side):
            global okay
            if node is None:
                return
            if node.val < left_side or node.val > right_side:
                okay = False
                return
            dfs(node.left, left_side, node.val-1)
            dfs(node.right, node.val+1, right_side)

        dfs(root, -inf, inf)
        return okay


s = Solution()
root = TreeNode(5, TreeNode(1), TreeNode(4))
print(s.isValidBST(root))
