from typing import *

#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


# @lc code=end

if __name__ == "__main__":
    print(1 == Solution().firstMissingPositive([]))
    print(1 == Solution().firstMissingPositive([-1]))
    print(1 == Solution().firstMissingPositive([0]))
    print(2 == Solution().firstMissingPositive([1]))
    print(4 == Solution().firstMissingPositive([3, 2, 1]))
    print(3 == Solution().firstMissingPositive([1, 2, 0]))
    print(4 == Solution().firstMissingPositive([1, 2, 3]))
    print(2 == Solution().firstMissingPositive([3, 4, -1, 1]))
    print(2 == Solution().firstMissingPositive([3, 4, 1, -1]))
    print(5 == Solution().firstMissingPositive([3, 4, 2, 1]))
    print(1 == Solution().firstMissingPositive([7, 8, 9, 11, 12]))
    print(2 == Solution().firstMissingPositive([7, 8, 5, 4, 11, 9, 3, 10, 1]))
    # fmt: off
    print(6 == Solution().firstMissingPositive([-3, 9, 16, 4, 5, 16, -4, 9, 26, 2, 1, 19, -1, 25, 7, 22, 2, -7, 14, 2, 5, -6, 1, 17, 3, 24, -4, 17, 15]))
    print(100 == Solution().firstMissingPositive([99, 94, 96, 11, 92, 5, 91, 89, 57, 85, 66, 63, 84, 81, 79, 61, 74, 78, 77, 30, 64, 13, 58, 18, 70, 69, 51, 12, 32, 34, 9, 43, 39, 8, 1, 38, 49, 27, 21, 45, 47, 44, 53, 52, 48, 19, 50, 59, 3, 40, 31, 82, 23, 56, 37, 41, 16, 28, 22, 33, 65, 42, 54, 20, 29, 25, 10, 26, 4, 60, 67, 83, 62, 71, 24, 35, 72, 55, 75, 0, 2, 46, 15, 80, 6, 36, 14, 73, 76, 86, 88, 7, 17, 87, 68, 90, 95, 93, 97, 98]))
    print(99 == Solution().firstMissingPositive([98, 93, 95, 10, 91, 4, 90, 88, 56, 84, 65, 62, 83, 80, 78, 60, 73, 77, 76, 29, 63, 12, 57, 17, 69, 68, 50, 11, 31, 33, 8, 42, 38, 7, 0, 37, 48, 26, 20, 44, 46, 43, 52, 51, 47, 18, 49, 58, 2, 39, 30, 81, 22, 55, 36, 40, 15, 27, 21, 32, 64, 41, 53, 19, 28, 24, 9, 25, 3, 59, 66, 82, 61, 70, 23, 34, 71, 54, 74, -1, 1, 45, 14, 79, 5, 35, 13, 72, 75, 85, 87, 6, 16, 86, 67, 89, 94, 92, 96, 97]))
    # fmt: on
