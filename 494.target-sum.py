from typing import *

#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        count = 0
        n = len(nums)
        for i in range(1 << n):
            acc = 0
            for j in range(n):
                if i & 1 << j:
                    acc += nums[j]
                else:
                    acc -= nums[j]
            if acc == S:
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    print(5 == Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    # fmt: off
    print(2760 == Solution().findTargetSumWays([2, 3, 2, 1, 6, 2, 5, 2, 1, 5, 2, 6, 7, 4, 3, 1], 10))
    print(6606 == Solution().findTargetSumWays([10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46], 45))
    # fmt: on
