#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        i, j, n = 0, 0, len(s)
        while j < n:
            if s[i] == " ":
                i += 1
            if s[j] == " ":
                if i < j:
                    stack.append(s[i:j])
                    i = j
            j += 1
        if i < n and s[i] != " ":
            stack.append(s[i:])
        return " ".join(reversed(stack))


# @lc code=end

if __name__ == "__main__":
    print("" == Solution().reverseWords(""))
    print("" == Solution().reverseWords(" "))
    print("" == Solution().reverseWords("  "))
    print("blue is sky the" == Solution().reverseWords("the sky is blue"))
    print("world! hello" == Solution().reverseWords("  hello world!  "))
    print("example good a" == Solution().reverseWords("a good   example"))
