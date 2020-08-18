from typing import *

#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # F[m][n] = min{F[m-1][n], F[m][n-1]} + A[m][n]
        dp = [0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    dp[0] = grid[0][0]
                elif i == 0:
                    dp.append(dp[j - 1] + grid[0][j])
                elif j == 0:
                    dp[0] = dp[0] + grid[i][0]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().minPathSum([]))
    print(1 == Solution().minPathSum([[1]]))
    print(2 == Solution().minPathSum([[1, 1]]))
    print(7 == Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
