from __TreeNode import *

#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
        return None

    def recursive(self, node, count):
        result = None
        if node:
            result, count = self.recursive(node.left, count)
            count -= 1
            if count == 0:
                result = node
            if not result:
                result, count = self.recursive(node.right, count)
        return result, count


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    tree = create([3, 1, 4, None, 2])
    print(1 == Solution().kthSmallest(tree, 1))
    tree = create([5, 3, 6, 2, 4, None, None, 1])
    print(3 == Solution().kthSmallest(tree, 3))
