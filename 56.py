# 1302. Deepest Leaves Sum

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = -1
        self.sum_depth = 0

        def dfs(node, depth=0):
            if node is None:
                return
            if self.max_depth == depth:
                self.sum_depth += node.val
            elif self.max_depth < depth:
                self.max_depth = depth
                self.sum_depth = node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth + 1)
        dfs(root)
        return self.sum_depth


root = TreeNode(0, TreeNode(1), TreeNode(2))
s = Solution()
print(s.deepestLeavesSum(root))