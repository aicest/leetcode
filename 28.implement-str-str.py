#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        i = j = 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        if j == n:
            return i - j
        else:
            return -1


# @lc code=end

if __name__ == "__main__":
    print(0, Solution().strStr("", ""))
    print(0, Solution().strStr("abc", ""))
    print(-1, Solution().strStr("", "a"))
    print(1, Solution().strStr("aab", "ab"))
    print(2, Solution().strStr("hello", "ll"))
    print(-1, Solution().strStr("aaaaa", "bba"))
    print(4, Solution().strStr("mississippi", "issip"))
