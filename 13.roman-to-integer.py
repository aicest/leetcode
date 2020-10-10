#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        b = None
        for c in reversed(s):
            if (
                False
                or (c == "I" and b in ["V", "X"])
                or (c == "X" and b in ["L", "C"])
                or (c == "C" and b in ["D", "M"])
            ):
                result -= ht[c]
            else:
                result += ht[c]
                b = c
        return result


# @lc code=end
if __name__ == "__main__":
    print(3 == Solution().romanToInt("III"))
    print(4 == Solution().romanToInt("IV"))
    print(9 == Solution().romanToInt("IX"))
    print(58 == Solution().romanToInt("LVIII"))
    print(1994 == Solution().romanToInt("MCMXCIV"))
