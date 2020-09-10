from typing import *

#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.bs(nums, 0, len(nums) - 1)

    def bs(self, nums, start, end):
        if start == end:
            return start
        pivot = (start + end) >> 1
        if nums[pivot] > nums[pivot + 1]:
            return self.bs(nums, start, pivot)
        else:
            return self.bs(nums, pivot + 1, end)


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().findPeakElement([1]))
    print(1 == Solution().findPeakElement([1, 2]))
    print(2 == Solution().findPeakElement([1, 2, 3]))
    print(2 == Solution().findPeakElement([1, 2, 3, 1]))
    print(5 == Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    print(4 == Solution().findPeakElement([7, 8, 9, 4, 5, 4, 3]))
