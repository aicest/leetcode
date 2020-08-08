from typing import *

#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.qs(nums, 0, len(nums) - 1)

    def qs(self, nums, start, end):
        i, j = start + 1, end
        while True:
            while i <= j and nums[i] < nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                break
        if start != j:
            nums[start], nums[j] = nums[j], nums[start]
        if start < j - 1:
            self.qs(nums, start, j - 1)
        if j + 1 < end:
            self.qs(nums, j + 1, end)


# @lc code=end

if __name__ == "__main__":
    Solution().sortColors(nums := [2, 1, 3])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 3, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 0, 2, 1, 1, 0])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [1, 0, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 0, 2])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [1, 2, 1, 0])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 1, 1, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 1, 1, 1, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [1, 2, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [1, 2, 0, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [1, 2, 0, 2])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 1, 0, 1])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 1, 0, 2])
    print(sorted(nums) == nums)
    Solution().sortColors(nums := [2, 1, 0, 0, 2, 1, 2, 1, 0, 2, 1, 1])
    print(sorted(nums) == nums)
