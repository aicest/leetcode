#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i, j = i + 1, j - 1
            else:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    print(Solution().isPalindrome(""))
    print(Solution().isPalindrome("a"))
    print(Solution().isPalindrome("Aa"))
    print(Solution().isPalindrome("Aba"))
    print(Solution().isPalindrome("AbBa"))
    print(Solution().isPalindrome("01 a 2 a 10"))
    print(not Solution().isPalindrome("0P"))
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(not Solution().isPalindrome("race a car"))
