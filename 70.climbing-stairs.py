#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # F[n] = F[n-1] + F[n-2]
        dp = 1, 1
        while n := n - 1:
            dp = dp[1], dp[0] + dp[1]
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    print(1 == Solution().climbStairs(1))
    print(2 == Solution().climbStairs(2))
    print(3 == Solution().climbStairs(3))
    print(1836311903 == Solution().climbStairs(45))
