#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # F[n] = F[n-1] + F[n-2]
        ht = set(map(str, range(1, 27)))
        prev = curr = 1 if s[0] in ht else 0
        for i in range(1, len(s)):
            prev, curr = (
                curr,
                (curr if s[i] in ht else 0) + (prev if s[i - 1 : i + 1] in ht else 0),
            )
        return curr


# @lc code=end

if __name__ == "__main__":
    print(0, Solution().numDecodings("0"))
    print(1, Solution().numDecodings("10"))
    print(2, Solution().numDecodings("12"))
    print(3, Solution().numDecodings("226"))
    print(120, Solution().numDecodings("12145241161715"))
    print(150, Solution().numDecodings("1121202012120121210121020"))
    print(0, Solution().numDecodings("11212020121201212101210200"))
