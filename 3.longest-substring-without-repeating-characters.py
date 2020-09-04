#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        i, j, n = 0, 0, len(s)
        best = 0
        while j < n:
            c = s[j]
            ht[c] = ht[c] + 1 if c in ht else 1
            while ht[c] != 1:
                ht[s[i]], i = ht[s[i]] - 1, i + 1
            j += 1
            best = max(best, j - i)
        return best


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().lengthOfLongestSubstring(""))
    print(1 == Solution().lengthOfLongestSubstring("a"))
    print(1 == Solution().lengthOfLongestSubstring("bbbbb"))
    print(3 == Solution().lengthOfLongestSubstring("abcabcbb"))
    print(3 == Solution().lengthOfLongestSubstring("mississippi"))
    print(3 == Solution().lengthOfLongestSubstring("pwwkew"))
