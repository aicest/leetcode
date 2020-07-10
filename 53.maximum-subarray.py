#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
import math


class Solution:
    def maxSubArray(self, nums):
        return self.dac(nums, 0, len(nums) - 1)

    def dac(self, nums, start, end):
        if start == end:
            return nums[start]

        if start + 1 == end:
            return max(nums[start], nums[start] + nums[end], nums[end])

        pivot = math.floor((start + end) / 2)
        leftSum = rightSum = 0
        maxLeftSum = maxRightSum = float("-inf")

        for i in range(pivot, start - 1, -1):
            leftSum += nums[i]
            maxLeftSum = max(maxLeftSum, leftSum)

        for i in range(pivot + 1, end + 1):
            rightSum += nums[i]
            maxRightSum = max(maxRightSum, rightSum)

        return max(
            self.dac(nums, start, pivot),
            maxLeftSum + maxRightSum,
            self.dac(nums, pivot, end),
        )


# @lc code=end
