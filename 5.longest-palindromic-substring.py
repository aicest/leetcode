#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # F[n] = max{F[n-1], P[0->n], P[1->n], ..., P[n->n]}
        best = ""
        dp = []
        n = len(s)
        for i in range(n):
            dp.append([False] * n)
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 >= i - 1 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    best = s[j : i + 1] if i + 1 - j > len(best) else best
        return best


# @lc code=end

if __name__ == "__main__":
    print("" == Solution().longestPalindrome(""))
    print("a" == Solution().longestPalindrome("a"))
    print("aaaa" == Solution().longestPalindrome("aaaa"))
    print("bab" == Solution().longestPalindrome("babad"))
    print("bb" == Solution().longestPalindrome("cbbd"))
    print("aababbbabaa" == Solution().longestPalindrome("abbabaababbbabaaabaabaabbaab"))
