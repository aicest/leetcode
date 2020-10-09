#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = ""
        count = 0
        for c in reversed(str(n)):
            if count == 3:
                result += "."
                count = 0
            result += c
            count += 1
        return result[::-1]


# @lc code=end

if __name__ == "__main__":
    print("987" == Solution().thousandSeparator(987))
    print("1.234" == Solution().thousandSeparator(1234))
    print("123.456.789" == Solution().thousandSeparator(123456789))
    print("0" == Solution().thousandSeparator(0))
