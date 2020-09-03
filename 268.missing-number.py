from typing import *

#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            j = nums[i]
            while j != i and j != n:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i]
        for i in range(n):
            if nums[i] != i:
                return i
        return n


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().missingNumber([]))
    print(1 == Solution().missingNumber([0]))
    print(0 == Solution().missingNumber([1]))
    print(3 == Solution().missingNumber([2, 0, 1]))
    print(2 == Solution().missingNumber([3, 0, 1]))
    print(8 == Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
