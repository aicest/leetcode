from __TreeNode import *

#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.dfs(root, sum)

    def dfs(self, node, sum):
        found = False
        if node:
            sum -= node.val
            found = not node.left and not node.right and sum == 0
            found = found or self.dfs(node.left, sum)
            found = found or self.dfs(node.right, sum)
        return found


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print(not Solution().hasPathSum(create([]), 0))
    print(not Solution().hasPathSum(create([]), 1))
    print(not Solution().hasPathSum(create([1, 1, None, 1]), 2))
    print(not Solution().hasPathSum(create([1, 1, None, None, 1]), 2))
    # fmt: off
    print(Solution().hasPathSum(create([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22))
    # fmt: on
