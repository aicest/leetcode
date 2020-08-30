from __TreeNode import *

#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        nodeList = [root] if root else []
        count = 0
        while nodeList:
            count += 1
            nextLevel = []
            while nodeList:
                node = nodeList.pop()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            nodeList = nextLevel
        return count

    def dfs(self, node):
        best = 0
        if node:
            best = 1 + max(self.dfs(node.left), self.dfs(node.right))
        return best


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    tree = create([])
    print(0 == Solution().maxDepth(tree))
    tree = create([1])
    print(1 == Solution().maxDepth(tree))
    tree = create([3, 9, 20, None, None, 15, 7])
    print(3 == Solution().maxDepth(tree))
