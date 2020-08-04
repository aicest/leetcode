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
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[k] == 2:
                k -= 1
            elif nums[j] == nums[k]:
                if j != k:
                    nums[j + 1], nums[k] = nums[k], nums[j + 1]
                j += 2
            else:
                nums[j], nums[k] = nums[k], nums[j]


# @lc code=end

if __name__ == "__main__":
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
