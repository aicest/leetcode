from typing import *

#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dp = {0: 1}  # 0!
        for a in nums:
            for b in list(dp.keys()):
                if a + b in dp:
                    pass
                else:
                    dp[a + b] = dp[a]
        return count


# @lc code=end

if __name__ == "__main__":
    print(4 == Solution().subarraySum([1, -1, 1, 2, -2], 0))
    print(2 == Solution().subarraySum([1, 1, 1], 2))
    print(
        7
        == Solution().subarraySum(
            [1, 1, 1, 2, 6, 4, 4, 2, 3, 3, 2, 4, 5, 2, 4, 2, 2, 2, 2, 1, 1], 10
        )
    )
