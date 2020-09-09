from __TreeNode import *

#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        result = {target: 0}
        stack = [(root, {})] if root else []
        while stack:
            node, pathList = stack.pop()
            curr = {}
            for path, count in pathList.items():
                path = path + node.val
                curr[path] = count
                result[path] = result[path] + count if path in result else count
            curr[node.val] = curr[node.val] + 1 if node.val in curr else 1
            result[node.val] = result[node.val] + 1 if node.val in result else 1
            if node.right:
                stack.append((node.right, curr))
            if node.left:
                stack.append((node.left, curr))
        return result[target]

    def dfs(self, node, pathList):
        result = {}
        if node:
            curr = {}
            for path, count in pathList.items():
                curr[path + node.val] = count
            curr[node.val] = curr[node.val] + 1 if node.val in curr else 1
            result = {**curr}
            for path, count in self.dfs(node.left, curr).items():
                result[path] = result[path] + count if path in result else count
            for path, count in self.dfs(node.right, curr).items():
                result[path] = result[path] + count if path in result else count
        return result


# @lc code=end

if __name__ == "__main__":
    create = TreeNode.create
    print(0 == Solution().pathSum(create([]), 0))
    print(1 == Solution().pathSum(create([0]), 0))
    print(0 == Solution().pathSum(create([1]), 0))
    print(1 == Solution().pathSum(create([1, 2, 0]), 3))
    # fmt: off
    print(3 == Solution().pathSum(create([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))
    print(4 == Solution().pathSum(create([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, 0]), 8))
    print(5 == Solution().pathSum(create([10, 5, -3, 3, 2, None, 11, 0, 0, None, 1]), 8))
    print(500500 == Solution().pathSum(create([0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0]), 0))
    # fmt: on
