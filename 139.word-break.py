from typing import *

#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # F[n] = F[n-1]S[n:n] + F[n-2]S[n-1:n] + ... + F[1]S[2:n] + F[0]:S[0:n]
        wordDict = dict(zip(wordDict, wordDict))
        dp = [""]
        for i in range(len(s)):
            for j in range(len(dp) - 1, -1, -1):
                if s[len(dp[j]) : i + 1] in wordDict:
                    dp.append(s[0 : i + 1])
                    break
        return dp[-1] == s


# @lc code=end

if __name__ == "__main__":
    print(Solution().wordBreak("", []))
    print(Solution().wordBreak("", [""]))
    print(Solution().wordBreak("abc", ["a", "bc"]))
    print(Solution().wordBreak("abc", ["a", "abc"]))
    print(not Solution().wordBreak("abc", ["ab", "bc"]))
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
    print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
    print(not Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
