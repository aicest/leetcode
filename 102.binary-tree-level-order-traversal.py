from typing import *
from __TreeNode import *

#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        currLevel = [root]
        while True:
            visited = []
            nextLevel = []
            while currLevel:
                node = currLevel.pop(0)
                if node:
                    visited.append(node.val)
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
            if visited:
                result.append(visited)
            if nextLevel:
                currLevel = nextLevel
            else:
                break
        return result


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print([] == Solution().levelOrder(create([])))
    print([[3], [9]] == Solution().levelOrder(create([3, 9])))
    print([[3], [9]] == Solution().levelOrder(create([3, None, 9])))
    # fmt: off
    print([[3], [9, 20], [15, 7]] == Solution().levelOrder(create([3, 9, 20, None, None, 15, 7])))
    # fmt: on
