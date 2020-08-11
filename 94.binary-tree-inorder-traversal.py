from typing import *
from __TreeNode import *

#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 左 -> 根 -> 右
        return self.recursive(root)

    def recursive(self, node):
        result = []
        if node:
            result += self.recursive(node.left)
            result.append(node.val)
            result += self.recursive(node.right)
        return result


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print([] == Solution().inorderTraversal(create([])))
    print([1] == Solution().inorderTraversal(create([1])))
    print([1, 3, 2] == Solution().inorderTraversal(create([1, None, 2, 3])))
