#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        ht = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in ht:
                return [ht[b], i]
            else:
                ht[a] = i


# @lc code=end

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([2, 7, 2, 15], 4))
