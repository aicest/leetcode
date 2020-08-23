from typing import *

#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
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
