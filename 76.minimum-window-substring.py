#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return ""


# @lc code=end

if __name__ == "__main__":
    print("" == Solution().minWindow("", ""))
    print("" == Solution().minWindow("", "A"))
    print("" == Solution().minWindow("ADOBECODEBANC", "ABCDEF"))
    print("BANC" == Solution().minWindow("ADOBECODEBANC", "ABC"))
