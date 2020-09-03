#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().addDigits(0))
    print(9 == Solution().addDigits(9))
    print(1 == Solution().addDigits(10))
    print(9 == Solution().addDigits(18))
    print(1 == Solution().addDigits(37))
    print(2 == Solution().addDigits(38))
    print(3 == Solution().addDigits(39))
