from typing import *

#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 核心：
        # 1. 找到一个极小数，存在更大数，说明需要排序，记录位置
        # 2. 继续查找，发现更小数，取其为极小数，但不用记录位置
        low, high = float("inf"), float("-inf")
        lowIndex, highIndex = 0, -1
        for i in reversed(range(len(nums))):
            if nums[i] > low:
                lowIndex = i
            else:
                low = nums[i]
        for i in range(len(nums)):
            if nums[i] < high:
                highIndex = i
            else:
                high = nums[i]
        return highIndex + 1 - lowIndex

    def v1(self, nums):
        asc = []
        n = len(nums)
        for i in range(n):
            pos = self.bs(nums, asc, 0, i, nums[i])
            asc.insert(pos, i)
        i, j = 0, n - 1
        while i <= j and asc[i] == i:
            i += 1
        while i <= j and asc[j] == j:
            j -= 1
        return j + 1 - i

    def bs(self, nums, asc, start, end, target):
        if start == end:
            return start
        pivot = (start + end) >> 1
        if target < nums[asc[pivot]]:
            return self.bs(nums, asc, start, pivot, target)
        else:
            return self.bs(nums, asc, pivot + 1, end, target)


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().findUnsortedSubarray([]))
    print(0 == Solution().findUnsortedSubarray([1]))
    print(0 == Solution().findUnsortedSubarray([1, 2, 3]))
    print(0 == Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))
    print(5 == Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(8 == Solution().findUnsortedSubarray([2, 3, 4, 1, 5, 10, 6, 7]))
