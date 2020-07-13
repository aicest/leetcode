#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        return self.dac(nums, 0, len(nums) - 1)

    def dac(self, nums, start, end):
        if start == end:
            return nums[start]
        pivot = (start + end) // 2
        left = self.dac(nums, start, pivot)
        right = self.dac(nums, pivot + 1, end)
        if left == None:
            return right
        if right == None:
            return left
        if left == right:
            return left
        leftCount, rightCount = self.count(nums, start, end, left, right)
        if leftCount > rightCount:
            return left
        elif leftCount < rightCount:
            return right
        else:
            return None

    def count(self, nums, start, end, left, right):
        leftCount = rightCount = 0
        for i in range(start, end + 1):
            if nums[i] == left:
                leftCount += 1
            elif nums[i] == right:
                rightCount += 1
        return leftCount, rightCount


# @lc code=end

if __name__ == "__main__":
    print(Solution().majorityElement([8, 8, 7, 7, 7]))
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
