from typing import *

#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [
            self.bs(nums, 0, len(nums) - 1, target, False),
            self.bs(nums, 0, len(nums) - 1, target, True),
        ]

    def bs(self, arr, start, end, target, reverse):
        if start == end:
            return start if arr[start] == target else -1
        pivot = (start + end) >> 1
        if target <= arr[pivot] and (not reverse or target < arr[pivot + 1]):
            return self.bs(arr, start, pivot, target, reverse)
        else:
            return self.bs(arr, pivot + 1, end, target, reverse)


# @lc code=end

if __name__ == "__main__":
    print([-1, -1] == Solution().searchRange([], 1))
    print([-1, -1] == Solution().searchRange([0], 1))
    print([0, 0] == Solution().searchRange([0], 0))
    print([0, 1] == Solution().searchRange([0, 0], 0))
    print([3, 4] == Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print([-1, -1] == Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
