from typing import *

#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 + 1 + 2 + ... + n-2 + n-1 + n = n * (n + 1) / 2 - x
        n = len(nums)
        x = n * (n + 1) // 2 - sum(nums)
        return x


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().missingNumber([]))
    print(1 == Solution().missingNumber([0]))
    print(0 == Solution().missingNumber([1]))
    print(3 == Solution().missingNumber([2, 0, 1]))
    print(2 == Solution().missingNumber([3, 0, 1]))
    print(8 == Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
