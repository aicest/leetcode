#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        i, j = 0, 1
        while j < n:
            if nums[i] == nums[j]:
                del nums[j]
                n -= 1
            else:
                i, j = j, j + 1
        return n


# @lc code=end
if __name__ == "__main__":
    Solution().removeDuplicates(nums := [1, 1, 2])
    print([1, 2] == nums)
    Solution().removeDuplicates(nums := [0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print([0, 1, 2, 3, 4] == nums)
