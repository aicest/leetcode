from typing import *

#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        best = 0
        while pool:
            x, count = pool.pop(), 0
            while x - 1 in pool:
                pool.remove(x - 1)
                x, count = x - 1, count + 1
            x = x + count
            while x + 1 in pool:
                pool.remove(x + 1)
                x, count = x + 1, count + 1
            best = max(best, count + 1)
            if best >= len(pool):
                return best
        return best

    def uf(self, nums):
        best = 0
        tree = {}
        for x in nums:
            tree[x] = {"parent": x, "size": 1}
        for x in nums:
            best = max(best, tree[x]["size"])
            if x - 1 in tree:
                best = max(best, self.union(tree, x, x - 1)["size"])
            if x + 1 in tree:
                best = max(best, self.union(tree, x, x + 1)["size"])
        return best

    def union(self, tree, src, dest):
        srcRoot, destRoot = self.find(tree, src), self.find(tree, dest)
        if srcRoot == destRoot:
            return srcRoot
        if srcRoot["size"] <= destRoot["size"]:
            srcRoot["parent"] = destRoot["parent"]
            destRoot["size"] += srcRoot["size"]
            return destRoot
        else:
            destRoot["parent"] = srcRoot["parent"]
            srcRoot["size"] += destRoot["size"]
            return srcRoot

    def find(self, tree, target):
        while tree[target]["parent"] != target:
            target, tree[target]["parent"] = (
                tree[target]["parent"],
                tree[tree[target]["parent"]]["parent"],
            )
        return tree[target]


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().longestConsecutive([]))
    print(1 == Solution().longestConsecutive([1]))
    print(1 == Solution().longestConsecutive([1, 3]))
    print(4 == Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(4 == Solution().longestConsecutive([100, 4, 200, 2, 1, 3]))
