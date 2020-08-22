from __TreeNode import *

#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p, q = (p, q) if p.val <= q.val else (q, p)
        return self.bs(root, p, q)

    def bs(self, node, p, q):
        if not node:
            return None
        if q.val < node.val:
            return self.bs(node.left, p, q)
        elif node.val < p.val:
            return self.bs(node.right, p, q)
        else:
            return node


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    root = create([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(6 == Solution().lowestCommonAncestor(root, create([2]), create([8])).val)
    root = create([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(2 == Solution().lowestCommonAncestor(root, create([2]), create([4])).val)
    root = create([2, 1])
    print(2 == Solution().lowestCommonAncestor(root, create([2]), create([1])).val)
