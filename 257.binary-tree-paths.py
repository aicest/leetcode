#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        return self.dfs(root, str(root.val))

    def dfs(self, node, path):
        if not node.left and not node.right:
            return [path]
        result = []
        if node.left:
            result += self.dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            result += self.dfs(node.right, path + "->" + str(node.right.val))
        return result


# @lc code=end

from __TreeNode import *

if __name__ == "__main__":
    print(Solution().binaryTreePaths(TreeNode.create([1, 2, 3, None, 5])))
