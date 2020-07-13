#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        # https://zh.wikipedia.org/wiki/%E5%A4%9A%E6%95%B0%E6%8A%95%E7%A5%A8%E7%AE%97%E6%B3%95
        m = None
        i = 0
        for x in nums:
            if i == 0:
                m = x
            if m == x:
                i += 1
            else:
                i -= 1
        return m


# @lc code=end

if __name__ == "__main__":
    print(Solution().majorityElement([8, 8, 7, 7, 7]))
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
