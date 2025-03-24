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
        sum_layer = 0
        cur_layer = [root]
        next_layer = []

        while cur_layer:
            sum_layer = 0
            next_layer = []
            for node in cur_layer:
                sum_layer += node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            cur_layer = next_layer
        return sum_layer


root = TreeNode(0, TreeNode(1), TreeNode(2))
s = Solution()
print(s.deepestLeavesSum(root))