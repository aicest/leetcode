#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n if n != 0 else 0
        if k == 0:
            return
        copy = nums.copy()
        for i in range(n):
            nums[i] = copy[((n + i) - k) % n]


# @lc code=end

if __name__ == "__main__":
    Solution().rotate(nums := [], 3)
    print([] == nums)
    Solution().rotate(nums := [1, 2, 3, 4, 5, 6, 7], 3)
    print([5, 6, 7, 1, 2, 3, 4] == nums)
    Solution().rotate(nums := [-1, -100, 3, 99], 2)
    print([3, 99, -1, -100] == nums)
