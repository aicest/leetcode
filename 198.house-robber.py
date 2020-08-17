from typing import *

#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # F[n] = max{F[n-2]+A[n], F[n-3]+A[n]}
        dp = [0] * 3
        for x in nums:
            dp[0], dp[1], dp[2] = dp[1], dp[2], max(dp[0] + x, dp[1] + x)
        return max(dp[1], dp[2])


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().rob([]))
    print(0 == Solution().rob([0]))
    print(1 == Solution().rob([1]))
    print(4 == Solution().rob([1, 2, 3, 1]))
    print(4 == Solution().rob([2, 1, 1, 2]))
    print(12 == Solution().rob([2, 7, 9, 3, 1]))
