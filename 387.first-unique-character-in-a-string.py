#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = {}
        for c in s:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        for i in range(len(s)):
            if ht[s[i]] == 1:
                return i
        return -1


# @lc code=end

if __name__ == "__main__":
    print(-1 == Solution().firstUniqChar(""))
    print(-1 == Solution().firstUniqChar("abba"))
    print(4 == Solution().firstUniqChar("abbac"))
    print(6 == Solution().firstUniqChar("abbaccd"))
    print(0 == Solution().firstUniqChar("leetcode"))
    print(2 == Solution().firstUniqChar("loveleetcode"))
