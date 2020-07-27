#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, input):
        result = input.split(" ")
        result = map(lambda partial: partial[::-1], result)
        return " ".join(result)


# @lc code=end

if __name__ == "__main__":
    # fmt: off
    print("s'teL ekat edoCteeL tsetnoc" == Solution().reverseWords("Let's take LeetCode contest"))
    # fmt: on
    print("" == Solution().reverseWords(""))
    print(" " == Solution().reverseWords(" "))
    print("  " == Solution().reverseWords("  "))
    print(" a " == Solution().reverseWords(" a "))
    print(" ba " == Solution().reverseWords(" ab "))
