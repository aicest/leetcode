from typing import *

#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1

    def v1(self, nums):
        i, j, n = 0, 0, len(nums)
        while i < n and j < n:
            while i < n and nums[i] != 0:
                i += 1
            j = max(i + 1, j)
            while j < n and nums[j] == 0:
                j += 1
            if j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1


# @lc code=end

if __name__ == "__main__":
    Solution().moveZeroes(nums := [0, 1, 0, 3, 12])
    print(nums == [1, 3, 12, 0, 0])
    Solution().moveZeroes(nums := [0, 1, 0, 0, 0, 3, 12])
    print(nums == [1, 3, 12, 0, 0, 0, 0])
