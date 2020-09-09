from typing import *

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = set()
        m, n = len(grid), len(grid[0]) if grid else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = curr = {"axis": (i, j), "size": 1}
                    curr["parent"] = root = curr
                    adjacent = []
                    if i == 0 and j == 0:
                        adjacent.append(None)
                    elif i == 0:
                        adjacent.append(grid[i][j - 1])
                    elif j == 0:
                        adjacent.append(grid[i - 1][j])
                    else:
                        adjacent.append(grid[i][j - 1])
                        adjacent.append(grid[i - 1][j])
                    for node in filter(bool, adjacent):
                        axis = self.find(grid, node)["axis"]
                        if axis in result:
                            result.remove(axis)
                        root = self.union(grid, curr, node)
                    result.add(root["axis"])
                else:
                    grid[i][j] = None
        return len(result)

    def union(self, tree, src, dst):
        src, dst = self.find(tree, src), self.find(tree, dst)
        if src == dst:
            return src
        elif src["size"] <= dst["size"]:
            src["parent"] = dst
            dst["size"] += src["size"]
            return dst
        else:
            dst["parent"] = src
            src["size"] += dst["size"]
            return src

    def find(self, tree, target):
        i, j = target["axis"]
        while tree[i][j]["parent"] != tree[i][j]:
            target = tree[i][j]["parent"] = tree[i][j]["parent"]["parent"]
            i, j = target["axis"]
        return tree[i][j]


# @lc code=end

if __name__ == "__main__":
    grid = [
        ["1", "0"],
        ["0", "1"],
    ]
    print(2 == Solution().numIslands(grid))
    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"],
    ]
    print(1 == Solution().numIslands(grid))
    grid = [
        ["1", "1", "1"],
        ["0", "0", "1"],
        ["1", "1", "1"],
    ]
    print(1 == Solution().numIslands(grid))
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(1 == Solution().numIslands(grid))
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(3 == Solution().numIslands(grid))
    grid = [
        ["1", "1", "1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "1", "0", "1"],
        ["1", "0", "1", "0", "1", "0", "1"],
        ["1", "0", "1", "1", "1", "0", "1"],
        ["1", "1", "1", "1", "1", "1", "1"],
    ]
    print(1 == Solution().numIslands(grid))
