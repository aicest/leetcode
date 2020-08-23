from typing import *

#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums) if nums else 0
        return max(self.dp(nums, 0, n - 1), self.dp(nums, 1, n))

    def dp(self, nums, i, n):
        dp = [0] * 3
        while i < n:
            dp[0], dp[1], dp[2] = dp[1], dp[2], max(dp[0], dp[1]) + nums[i]
            i += 1
        return max(dp)


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().rob([]))
    print(1 == Solution().rob([1]))
    print(2 == Solution().rob([1, 2]))
    print(3 == Solution().rob([1, 2, 3]))
    print(3 == Solution().rob([2, 3, 2]))
    print(4 == Solution().rob([1, 2, 3, 1]))
