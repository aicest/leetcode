#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = []
        n = len(s)
        for i in range(n):
            dp.append([False] * n)
            dp[i][i] = True
            count += 1
            for j in range(i):
                if s[j] == s[i] and (j + 1 >= i - 1 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    print(3 == Solution().countSubstrings("abc"))
    print(6 == Solution().countSubstrings("aaa"))
    print(58 == Solution().countSubstrings("ababaabaabaababbbabab"))
    print(41 == Solution().countSubstrings("eaawaeeeaeaeeseaezeaes"))
