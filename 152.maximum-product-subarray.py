from typing import *

#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # F[n] = max{F[n-1], min(F[n-1])*A[n], max(F[n-1])*A[n], A[n]}
        best = float("-inf")
        low, high = 1, 1
        for x in nums:
            low, high = low * x, high * x
            low, high = min(low, high, x), max(low, high, x)
            best = max(best, high)
        return best


# @lc code=end

if __name__ == "__main__":
    print(-1 == Solution().maxProduct([-1]))
    print(2 == Solution().maxProduct([-1, -2]))
    print(16 == Solution().maxProduct([-2, 2, -1, -2, 1, -2]))
    print(6 == Solution().maxProduct([2, 3, -2, 4]))
    print(0 == Solution().maxProduct([-2, 0, -1]))
