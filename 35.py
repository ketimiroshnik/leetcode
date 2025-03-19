# 236. Lowest Common Ancestor of a Binary Tree

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        RECURSION!!!
        """
        depth = dict()
        parent = dict()

        depth[root.val] = 0
        parent[root.val] = None
        def depth_search(before, node):
            if node is None:
                return
            parent[node.val] = before
            depth[node.val] = depth[before.val] + 1
            depth_search(node, node.left)
            depth_search(node, node.right)


        depth_search(root, root.left)
        depth_search(root, root.right)

        one = p
        two = q
        while True:
            if one == two:
                return one
            if one == root or two == root:
                return root
            if depth[one.val] > depth[two.val]:
                one = parent[one.val]
            elif depth[one.val] < depth[two.val]:
                two = parent[two.val]
            else:
                one = parent[one.val]
                two = parent[two.val]




s = Solution()
root = TreeNode(3)
five = TreeNode(5)
one = TreeNode(1)
root.left = five
root.right = one

print(s.lowestCommonAncestor(root, five, one).val)