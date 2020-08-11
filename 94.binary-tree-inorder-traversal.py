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
        #   1
        #  / \
        # 2   3
        # |\  |\
        # 4 5 6 7
        result = []
        stack = []  # pending
        node = root
        while node or stack:
            if node:
                stack.append(node)  # d. push 5 | h. push 3 | i. push 6
                node = node.left
            else:
                node = stack.pop()  # a. pop 4 | b. pop 2 | e. pop 5 | f. pop 1
                result.append(node.val)
                node = node.right  # c. move 5 | g. move 3
        return result

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
    print([4, 2, 5, 1, 6, 3] == Solution().inorderTraversal(create(list(range(1, 7)))))
