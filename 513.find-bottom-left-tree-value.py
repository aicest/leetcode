#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
class Solution:
    def findBottomLeftValue(self, root):
        return self.dfs(root, [])[-1]

    def dfs(self, node, path):
        path = path + [node.val]
        result = path
        if node.left:
            leftPath = self.dfs(node.left, path)
            result = result if len(result) >= len(leftPath) else leftPath
        if node.right:
            rightPath = self.dfs(node.right, path)
            result = result if len(result) >= len(rightPath) else rightPath
        return result


# @lc code=end

from __TreeNode import *

if __name__ == "__main__":
    create = TreeNode.create
    print(1, Solution().findBottomLeftValue(create([2, 1, 3])))
    print(7, Solution().findBottomLeftValue(create([1, 2, 3, 4, None, 5, 6, 7])))
