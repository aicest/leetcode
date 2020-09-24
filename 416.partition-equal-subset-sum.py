from typing import *

#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # F[n] = { ...F[n-1], F[n-1][i]+A[j] }
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total >> 1
        dp = {0: True}
        for a in nums:
            for b in list(dp.keys()):
                if a + b == half:
                    return True
                if a + b not in dp:
                    dp[a + b] = True
        return False


# @lc code=end

if __name__ == "__main__":
    print(not Solution().canPartition([1]))
    print(Solution().canPartition([1, 1]))
    print(not Solution().canPartition([1, 2]))
    print(not Solution().canPartition([1, 1, 1]))
    print(Solution().canPartition([1, 5, 11, 5]))
    print(Solution().canPartition([1, 5, 5, 6, 5]))
    print(not Solution().canPartition([1, 2, 3, 5]))
