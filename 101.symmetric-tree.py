from __TreeNode import *

#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recursive(root.left, root.right)

    def recursive(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.recursive(left.left, right.right) and self.recursive(
            left.right, right.left
        )

    def v1(self, root):
        # 完全二叉树
        if not root:
            return True
        left = self.dfs(root.left, False)
        right = self.dfs(root.right, True)
        return left == right

    def dfs(self, node, reverse):
        if not node:
            return [None]
        path = [node.val]
        if reverse:
            path += self.dfs(node.right, reverse)
            path += self.dfs(node.left, reverse)
        else:
            path += self.dfs(node.left, reverse)
            path += self.dfs(node.right, reverse)
        return path


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print(Solution().isSymmetric(create([])))
    print(Solution().isSymmetric(create([1])))
    print(not Solution().isSymmetric(create([1, 1])))
    print(Solution().isSymmetric(create([1, 2, 2, 3, 4, 4, 3])))
    print(not Solution().isSymmetric(create([1, 2, 2, None, 3, None, 3])))
