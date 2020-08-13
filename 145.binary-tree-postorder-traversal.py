from typing import *
from __TreeNode import *

#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.iterative(root)

    def iterative(self, node):
        result = []
        stack = [node]
        while stack:
            node = stack.pop()
            if node:
                result.insert(0, node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result

    def recursive(self, node):
        result = []
        if node:
            result += self.recursive(node.left)
            result += self.recursive(node.right)
            result.append(node.val)
        return result


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print([] == Solution().postorderTraversal(create([])))
    print([3, 2, 1] == Solution().postorderTraversal(create([1, None, 2, 3])))
    print([3, 4, 1, 5, 2, 0] == Solution().postorderTraversal(create(list(range(6)))))
