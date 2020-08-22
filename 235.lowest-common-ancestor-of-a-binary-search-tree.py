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
        A, B = self.dfs(root, p, []), self.dfs(root, q, [])
        i, n = 0, min(len(A), len(B))
        while i < n and A[i] == B[i]:
            i += 1
        return A[i - 1]

    def dfs(self, node, target, path):
        if not node:
            return None
        curr = path + [node]
        result = curr if node.val == target.val else None
        result = result or self.dfs(node.left, target, curr)
        result = result or self.dfs(node.right, target, curr)
        return result


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    root = create([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(6 == Solution().lowestCommonAncestor(root, create([2]), create([8])).val)
    root = create([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(2 == Solution().lowestCommonAncestor(root, create([2]), create([4])).val)
