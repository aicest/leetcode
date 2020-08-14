from typing import *

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.dfs(candidates, 0, len(candidates), [], target)

    def dfs(self, candidates, start, end, path, target):
        result = []
        for i in range(start, end):
            currPath = path + [candidates[i]]
            currTarget = target - candidates[i]
            if currTarget > 0:
                result += self.dfs(candidates, i, end, currPath, currTarget)
            elif currTarget == 0:
                result.append(currPath)
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
    print(Solution().combinationSum([5, 3, 2], 8))
