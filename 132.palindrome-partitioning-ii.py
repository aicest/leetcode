#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        # F[n] = min{F[n-1]+S[n:n], F[n-2]+S[n-1:n], ..., F[1]+S[2:n], F[0]+S[1:n], F[-1]+S[0:n]}
        n = len(s)
        dp = [float("inf")] * (n + 1)
        dp[0:2] = [-1, 0]
        dp2 = []  # palindrome
        for i in range(n):
            dp2.append([False] * n)
            for j in range(i, -1, -1):
                if s[j] == s[i] and (j + 1 >= i - 1 or dp2[j + 1][i - 1]):
                    dp2[j][i] = True
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    print(0, Solution().minCut(""))
    print(0, Solution().minCut("a"))
    print(1, Solution().minCut("ab"))
    print(1, Solution().minCut("aab"))
    print(0, Solution().minCut("abba"))
    print(0, Solution().minCut("abcba"))
    print(3, Solution().minCut("abaabbbbabababababbabab"))
    print(5, Solution().minCut("ababbbbabbbaaababbbabaaaababab"))
