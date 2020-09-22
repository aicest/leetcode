#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return True


# @lc code=end

if __name__ == "__main__":
    print(Solution().checkInclusion("ab", "eidbaooo"))
    print(Solution().checkInclusion("ab", "eidabooo"))
    print(not Solution().checkInclusion("ab", "eidboaoo"))
