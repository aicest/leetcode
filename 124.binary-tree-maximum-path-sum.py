#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
class Solution:
    def maxPathSum(self, root):
        return self.dfs(root)[1]

    def dfs(self, node):
        if node == None:
            return (float("-inf"), float("-inf"))
        leftPath, leftFull = self.dfs(node.left)
        rightPath, rightFull = self.dfs(node.right)
        path = max(node.val, node.val + leftPath, node.val + rightPath)
        full = max(path, leftFull, rightFull, node.val + leftPath + rightPath)
        return (path, full)


# @lc code=end

from __TreeNode import *

if __name__ == "__main__":
    create = TreeNode.create
    print(1, Solution().maxPathSum(create([1, -2, -3])))
    print(3, Solution().maxPathSum(create([1, 2, -3])))
    print(4, Solution().maxPathSum(create([1, -2, 3])))
    print(4, Solution().maxPathSum(create([-1, 2, 3])))
    print(3, Solution().maxPathSum(create([-2, 2, 3])))
    print(3, Solution().maxPathSum(create([-3, 2, 3])))
    print(3, Solution().maxPathSum(create([-4, 2, 3])))
    print(11, Solution().maxPathSum(create([1, 2, 3, 4, 5])))
    print(6, Solution().maxPathSum(create([1, 2, 3])))
    print(42, Solution().maxPathSum(create([-10, 9, 20, None, None, 15, 7])))
    print(5, Solution().maxPathSum(create([-6, None, 3, 2])))
    # fmt: off
    print(48, Solution().maxPathSum(create([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])))
    # fmt: on
