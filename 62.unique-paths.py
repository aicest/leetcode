#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # F[m][n] = F[m-1][n] + F[m][n-1]
        dp = []
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp.append(1)
                elif j != 0:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    print(1 == Solution().uniquePaths(1, 1))
    print(1 == Solution().uniquePaths(1, 5))
    print(1 == Solution().uniquePaths(5, 1))
    print(3 == Solution().uniquePaths(3, 2))
    print(28 == Solution().uniquePaths(7, 3))
