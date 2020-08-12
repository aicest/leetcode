from __TreeNode import *

#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.iterative(root, float("-inf"))

    def iterative(self, node, prev):
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev >= node.val:
                    return False
                prev = node.val
                node = node.right
        return True

    def recursive(self, node, prev):
        valid = True
        if node:
            if valid and node.left:
                valid, prev = self.recursive(node.left, prev)
            if valid:
                valid, prev = prev < node.val, node.val
            if valid and node.right:
                valid, prev = self.recursive(node.right, prev)
        return valid, prev


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print(Solution().isValidBST(create([])))
    print(Solution().isValidBST(create([2])))
    print(Solution().isValidBST(create([2, 1])))
    print(not Solution().isValidBST(create([2, 2])))
    print(not Solution().isValidBST(create([2, None, 2])))
    print(Solution().isValidBST(create([2, None, 3])))
    print(Solution().isValidBST(create([2, 1, 3])))
    print(not Solution().isValidBST(create([5, 1, 4, None, None, 3, 6])))
