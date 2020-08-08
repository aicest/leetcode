from typing import List
from __TreeNode import *

#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root] if root else []
        stack = []
        result = []
        while queue:
            arr = []
            while queue:
                node = queue.pop(0)
                arr.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if arr:
                result.append(arr)
            arr = []
            while stack:
                node = stack.pop()
                arr.append(node.val)
                if node.right:
                    queue.insert(0, node.right)
                if node.left:
                    queue.insert(0, node.left)
            if arr:
                result.append(arr)
        return result


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print([] == Solution().zigzagLevelOrder(create([])))
    print([[0]] == Solution().zigzagLevelOrder(create([0])))
    # fmt: off
    print([[3], [20, 9], [15, 7]] == Solution().zigzagLevelOrder(create([3, 9, 20, None, None, 15, 7])))
    print([[3], [20, 9], [1, 2, 15, 7]] == Solution().zigzagLevelOrder(create([3, 9, 20, 1, 2, 15, 7])))
    # fmt: on
