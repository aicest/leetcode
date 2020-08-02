#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s):
        VOWEL = set("aeoiuAEOIU")
        arr = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in VOWEL:
                i += 1
            elif s[j] not in VOWEL:
                j -= 1
            else:
                arr[i], arr[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(arr)


# @lc code=end

if __name__ == "__main__":
    print("" == Solution().reverseVowels(""))
    print("a" == Solution().reverseVowels("a"))
    print("b" == Solution().reverseVowels("b"))
    print("ea" == Solution().reverseVowels("ae"))
    print("ab" == Solution().reverseVowels("ab"))
    print("ba" == Solution().reverseVowels("ba"))
    print("holle" == Solution().reverseVowels("hello"))
    print("leotcede" == Solution().reverseVowels("leetcode"))
